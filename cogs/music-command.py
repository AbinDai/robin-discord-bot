import discord, random, asyncio, itertools, sys, traceback, youtube_dl, requests
from youtubesearchpython import VideosSearch
from discord.ext import commands
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL

# Redam suara bising soal penggunaan konsol dari error
youtube_dl.utils.bug_reports_message = lambda: ''

ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' #alamat ipv6 sering bermasalah kadang2
}

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = YoutubeDL(ytdlopts)


class VoiceConnectionError(commands.CommandError):
    """Kelas Pengecualian Kustom untuk koneksi error"""


class InvalidVoiceChannel(VoiceConnectionError):
    """Pengecualian untuk kasus Voice Channel yang tidak valid."""


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester
        self.title = data.get('title')
        self.web_url = data.get('webpage_url')
        self.duration = data.get('duration')

        # Info data dict YTDL memiliki beberapa informasi berguna yang mungkin mau kau pakai
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Memperbolehkan kita untuk mengakses atribut yang similar dengan dict.
        Ini hanya berguna jika kamu TIDAK sedang mengunduh.
        """
        return self.__getattribute__(item)
        

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # ambil item pertama dari playlist
            data = data['entries'][0]

        embed = discord.Embed(
            title="Ditambahkan ke Antrean",
            description=f"[{data['title']}]({data['webpage_url']}) [{ctx.author.mention}]"
        )
        await ctx.send(embed=embed)

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Digunakan untuk mempersiapkan streaming, daripada nge-download.
        Sejak link streaming yutub dah kadaluarsa."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url']), data=data, requester=requester)


class MusicPlayer:
    """Class yang dilampirkan buat masing2 server make si bot.
    Class ini mengimplementasikan antrean dan loop, yang memperbolehkan masing2 server utk mendengarkan ke playlist yg berbeda
    secara bersamaan.
    Ketika si bot keluar dari vc, instansinya bakal ilang.
    """

    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()

        self.np = None  # pesan nowplaying
        self.volume = .5
        self.current = None

        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        """Ngulang lagu."""
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            try:
                # Tunggu lagu selanjutnya. Kalo timeout, batalin player-nya trus keluar dri vc...
                async with timeout(300):  # 5 menit...
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                return self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                # Source-nya mungkin di-stream (gak di-download)
                # Jadi kita harus jaga buat menghindari kadaluarsanya stream
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as e:
                    await self._channel.send(f'Terjadi error saat sedang memproses.\n'
                                             f'```css\n[{e}]\n```')
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            embed = discord.Embed(
                title=source.title,
                url=source.web_url,
                description=f"Di-Request oleh {source.requester.mention}", 
                color=0x12098f
            )
            embed.set_author(name="Memutar", icon_url="https://i.giphy.com/media/JRCsHUHcD6v1NPfuYM/giphy.gif")
            self.np = await self._channel.send(embed=embed)
            await self.next.wait()

            # Pastikan proses FFmpeg bersih :v
            source.cleanup()
            self.current = None

    def destroy(self, guild):
        """Keluar dari vc dan menghapus semua lagu."""
        return self.bot.loop.create_task(self._cog.cleanup(guild))


class Music(commands.Cog):
    """Command2 musik."""

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass

    async def __local_check(self, ctx):
        """Pengecekan lokal yang berlaku untuk semua command yang ada di cog ini."""
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True

    async def __error(self, ctx, error):
        """Lokal error handler untuk semua error yang timbul dari command2 yang ada di cog ini."""
        if isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.send('❌ Command ini tidak dapat dijalankan di pesan DM!')
            except discord.HTTPException:
                pass
        elif isinstance(error, InvalidVoiceChannel):
            await ctx.send('Gagal menghubungkan ke voice channel. '
                           'Pastikan kamu berada di channel yang valid atau sebutkan nama channel yang mau kumasuki.')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    def get_player(self, ctx):
        """Bikin player server, ato tdk bikin yg baru."""
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    @commands.command(name='join', aliases=['connect', 'j'])
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                embed = discord.Embed(title="", description="Tidak ada channel untuk dimasuki. Coba eksekusi `join` ketika kamu sedang berada di vc.", color=0xff0000)
                await ctx.send(embed=embed)
                raise InvalidVoiceChannel('Tidak ada channel untuk dimasuki. Coba sebutkan channel-nya atau masuk ke salah satu.')

        player = self.get_player(ctx)
        if not player.current:
            vc = ctx.voice_client

            if vc:
                if vc.channel.id == channel.id:
                    return
                try:
                    await vc.move_to(channel)
                except asyncio.TimeoutError:
                    raise VoiceConnectionError(f'Timeout saat sedang berpindah ke channel {channel.mention}.')
            else:
                try:
                    await channel.connect()
                except asyncio.TimeoutError:
                    raise VoiceConnectionError(f'Timeout ketika sedang menghubungkan ke channel {channel.mention}.')
            if (random.randint(0, 1) == 0):
                await ctx.message.add_reaction('✅')
            await ctx.send(f'Terhubung ke {channel.mention}')
        elif player.current and ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
            await ctx.reply("Bot sudah berada di voice channel-nya kamu!")
        elif player.current and ctx.author.voice.channel != ctx.guild.get_member(self.bot.user.id).voice.channel:
            await ctx.reply("Seseorang sedang menggunakan bot ini di vc lain!")
        

    @commands.command(name='play', aliases=['p'])
    async def play_(self, ctx, *, search: str=None):
        if not search:
            return await ctx.reply("Sertakan lagu yang mau kamu putar!")

        player = self.get_player(ctx)
        if not player.current:   
            await ctx.trigger_typing()

            vc = ctx.voice_client

            if not vc:
                await ctx.invoke(self.connect_)

            player = self.get_player(ctx)

            
            source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)

            await player.queue.put(source)
        elif player.current and ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
            await ctx.trigger_typing()

            vc = ctx.voice_client

            if not vc:
                await ctx.invoke(self.connect_)

            player = self.get_player(ctx)

            
            source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)

            await player.queue.put(source)
        elif player.current and ctx.author.voice.channel != ctx.guild.get_member(self.bot.user.id).voice.channel:
            await ctx.reply("Seseorang sedang mendengarkan pakai bot ini di channel lain!")

    @commands.command()
    async def search(self, ctx, *, katakunci:str=None):
        if not katakunci:
            return await ctx.reply("Masukkan kata kunci pencarian!")

        vc = ctx.voice_client
        if not vc:
            await ctx.invoke(self.connect_)

        videosSearch = VideosSearch(katakunci, limit=10)
        hasil = videosSearch.result()

        judul1 = hasil["result"][0]["title"]
        link1 = hasil["result"][0]["link"]
        durasi1 = hasil["result"][0]["duration"]

        judul2 = hasil["result"][1]["title"]
        link2 = hasil["result"][1]["link"]
        durasi2 = hasil["result"][1]["duration"]

        judul3 = hasil["result"][2]["title"]
        link3 = hasil["result"][2]["link"]
        durasi3 = hasil["result"][2]["duration"]

        judul4 = hasil["result"][3]["title"]
        link4 = hasil["result"][3]["link"]
        durasi4 = hasil["result"][3]["duration"]

        judul5 = hasil["result"][4]["title"]
        link5 = hasil["result"][4]["link"]
        durasi5 = hasil["result"][4]["duration"]

        judul6 = hasil["result"][5]["title"]
        link6 = hasil["result"][5]["link"]
        durasi6 = hasil["result"][5]["duration"]

        judul7 = hasil["result"][6]["title"]
        link7 = hasil["result"][6]["link"]
        durasi7 = hasil["result"][6]["duration"]

        judul8 = hasil["result"][7]["title"]
        link8 = hasil["result"][7]["link"]
        durasi8 = hasil["result"][7]["duration"]

        judul9 = hasil["result"][8]["title"]
        link9 = hasil["result"][8]["link"]
        durasi9 = hasil["result"][8]["duration"]

        judul10 = hasil["result"][9]["title"]
        link10 = hasil["result"][9]["link"]
        durasi10 = hasil["result"][9]["duration"]

        embed = discord.Embed(
            title = f"Mencari __{katakunci}__",
            description = f"1. [{judul1}]({link1}) `{durasi1}`\n"
                        f"2. [{judul2}]({link2}) `{durasi2}`\n"
                        f"3. [{judul3}]({link3}) `{durasi3}`\n"
                        f"4. [{judul4}]({link4}) `{durasi4}`\n"
                        f"5. [{judul5}]({link5}) `{durasi5}`\n"
                        f"6. [{judul6}]({link6}) `{durasi6}`\n"
                        f"7. [{judul7}]({link7}) `{durasi7}`\n"
                        f"8. [{judul8}]({link8}) `{durasi8}`\n"
                        f"9. [{judul9}]({link9}) `{durasi9}`\n"
                        f"10. [{judul10}]({link10}) `{durasi10}`\n",
            color = ctx.guild.get_member(self.bot.user.id).color
        )
        embed.set_footer(text="Ambil angka 1-10 untuk mengambil video, atau balas 'batal' untuk membatalkan. Timeout dalam 30 detik.")
        pesan_pertama = await ctx.send(embed=embed)

        try:
            def check(msg):                         
                return msg.content.lower() in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "batal"] and msg.channel == ctx.channel

            msg = await self.bot.wait_for("message", check=check, timeout=30)
            if msg.content.lower() == "batal":
                await pesan_pertama.delete()
            elif msg.content.lower() == "1":
                if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
                    await ctx.trigger_typing()

                    vc = ctx.voice_client

                    if not vc:
                        await ctx.invoke(self.connect_)

                    player = self.get_player(ctx)

                    source = await YTDLSource.create_source(ctx, link1, loop=self.bot.loop, download=False)

                    await player.queue.put(source)
                    await pesan_pertama.delete()
                else:
                    await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
            elif msg.content.lower() == "2":
                if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
                    await ctx.trigger_typing()

                    vc = ctx.voice_client

                    if not vc:
                        await ctx.invoke(self.connect_)

                    player = self.get_player(ctx)

                    source = await YTDLSource.create_source(ctx, link2, loop=self.bot.loop, download=False)

                    await player.queue.put(source)
                    await pesan_pertama.delete()
                else:
                    await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
            elif msg.content.lower() == "3":
                if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
                    await ctx.trigger_typing()

                    vc = ctx.voice_client

                    if not vc:
                        await ctx.invoke(self.connect_)

                    player = self.get_player(ctx)

                    source = await YTDLSource.create_source(ctx, link3, loop=self.bot.loop, download=False)

                    await player.queue.put(source)
                    await pesan_pertama.delete()
                else:
                    await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
            elif msg.content.lower() == "4":
                if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
                    await ctx.trigger_typing()

                    vc = ctx.voice_client

                    if not vc:
                        await ctx.invoke(self.connect_)

                    player = self.get_player(ctx)

                    source = await YTDLSource.create_source(ctx, link4, loop=self.bot.loop, download=False)

                    await player.queue.put(source)
                    await pesan_pertama.delete()
                else:
                    await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
            elif msg.content.lower() == "5":
                if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
                    await ctx.trigger_typing()

                    vc = ctx.voice_client

                    if not vc:
                        await ctx.invoke(self.connect_)

                    player = self.get_player(ctx)

                    source = await YTDLSource.create_source(ctx, link5, loop=self.bot.loop, download=False)

                    await player.queue.put(source)
                    await pesan_pertama.delete()
                else:
                    await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
            elif msg.content.lower() == "6":
                if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
                    await ctx.trigger_typing()

                    vc = ctx.voice_client

                    if not vc:
                        await ctx.invoke(self.connect_)

                    player = self.get_player(ctx)

                    source = await YTDLSource.create_source(ctx, link6, loop=self.bot.loop, download=False)

                    await player.queue.put(source)
                    await pesan_pertama.delete()
                else:
                    await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
            elif msg.content.lower() == "7":
                if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
                    await ctx.trigger_typing()

                    vc = ctx.voice_client

                    if not vc:
                        await ctx.invoke(self.connect_)

                    player = self.get_player(ctx)

                    source = await YTDLSource.create_source(ctx, link7, loop=self.bot.loop, download=False)

                    await player.queue.put(source)
                    await pesan_pertama.delete()
                else:
                    await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
            elif msg.content.lower() == "8":
                if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
                    await ctx.trigger_typing()

                    vc = ctx.voice_client

                    if not vc:
                        await ctx.invoke(self.connect_)

                    player = self.get_player(ctx)

                    source = await YTDLSource.create_source(ctx, link8, loop=self.bot.loop, download=False)

                    await player.queue.put(source)
                    await pesan_pertama.delete()
                else:
                    await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
            elif msg.content.lower() == "9":
                if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
                    await ctx.trigger_typing()

                    vc = ctx.voice_client

                    if not vc:
                        await ctx.invoke(self.connect_)

                    player = self.get_player(ctx)

                    source = await YTDLSource.create_source(ctx, link9, loop=self.bot.loop, download=False)

                    await player.queue.put(source)
                    await pesan_pertama.delete()
                else:
                    await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
            elif msg.content.lower() == "10":
                if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
                    await ctx.trigger_typing()

                    vc = ctx.voice_client

                    if not vc:
                        await ctx.invoke(self.connect_)

                    player = self.get_player(ctx)

                    source = await YTDLSource.create_source(ctx, link10, loop=self.bot.loop, download=False)

                    await player.queue.put(source)
                    await pesan_pertama.delete()
                else:
                    await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
        except asyncio.TimeoutError:
            await pesan_pertama.delete()
    


    @commands.command(name='pause')
    async def pause_(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            embed = discord.Embed(title="", description="Tidak ada Audio yang sedang diputar.", color=0xff0000)
            return await ctx.send(embed=embed)
        elif vc.is_paused():
            return

        if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
            vc.pause()
            await ctx.send("⏸️ Audio dijeda.")
        else:
            await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")

    @commands.command(name='resume', aliases=["remus"])
    async def resume_(self, ctx):
        """Resume the currently paused song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Tidak sedang terhubung ke voice channel manapun.", color=0xff0000)
            return await ctx.send(embed=embed)
        elif not vc.is_paused():
            return

        if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
            vc.resume()
            await ctx.send("▶ Audio dilanjutkan.")
        else:
            await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")

    @commands.command(name='skip')
    async def skip_(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Tidak sedang terhubung ke voice channel manapun.", color=0xff0000)
            return await ctx.send(embed=embed)

        if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
            if vc.is_paused():
                pass
            elif not vc.is_playing():
                return

            vc.stop()
        else:
            await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")
    
    @commands.command(name='remove')
    async def remove_(self, ctx, pos : int=None):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Tidak sedang terhubung ke voice channel manapun.", color=0xff0000)
            return await ctx.send(embed=embed)

        if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
            player = self.get_player(ctx)
            if pos == None:
                player.queue._queue.pop()
            else:
                try:
                    s = player.queue._queue[pos-1]
                    del player.queue._queue[pos-1]
                    embed = discord.Embed(title="", description=f"Dikeluarkan [{s['title']}]({s['webpage_url']}) [{s['requester'].mention}]", color=ctx.guild.get_member(self.bot.user.id).color)
                    await ctx.send(embed=embed)
                except:
                    embed = discord.Embed(title="", description=f'Tidak dapat menemukan trek dari "{pos}"', color=0xff0000)
                    await ctx.send(embed=embed)
        else:
            await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")               
    
    @commands.command(name='clearqueue')
    async def clearqueue_(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Tidak sedang terhubung ke voice channel manapun.", color=0xff0000)
            return await ctx.send(embed=embed)

        if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
            player = self.get_player(ctx)
            player.queue._queue.clear()
            await ctx.send('Antrean dibersihkan.')
        else:
            await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")

    @commands.command(name='queue', aliases=['q', 'ququ'])
    async def queue_info(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Tidak sedang terhubung ke voice channel manapun.", color=0xff0000)
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if player.queue.empty():
            embed = discord.Embed(title="", description="Antrean kosong", color=ctx.guild.get_member(self.bot.user.id).color)
            return await ctx.send(embed=embed)

        seconds = vc.source.duration % (24 * 3600) 
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            duration = "%d:%02d:%02d" % (hour, minutes, seconds)
        else:
            duration = "%02d:%02d" % (minutes, seconds)

        # menuliskan daftar lagu ke antrean
        upcoming = list(itertools.islice(player.queue._queue, 0, int(len(player.queue._queue))))
        fmt = '\n'.join(f"`{(upcoming.index(_)) + 1}.` [{_['title']}]({_['webpage_url']})" for _ in upcoming)
        fmt = f"\n__Sedang diputar__:\n[{vc.source.title}]({vc.source.web_url})\n\n__Selanjutnya:__\n" + fmt + f"\n\n**{len(upcoming)} lagu dalam antrean.**"
        embed = discord.Embed(
            title=f'Antrean untuk Server Ini',
            description=fmt,
            color=ctx.guild.get_member(self.bot.user.id).color
        )
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='nowplaying', aliases=['now', 'current', 'currentsong', 'playing', "np"])
    async def now_playing_(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Tidak sedang terhubung ke voice channel manapun.", color=0xff0000)
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if not player.current:
            embed = discord.Embed(title="", description="Tidak ada Audio yang sedang diputar.", color=0xff0000)
            return await ctx.send(embed=embed)
        
        seconds = vc.source.duration % (24 * 3600) 
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            duration = "%d:%02d:%02d" % (hour, minutes, seconds)
        else:
            duration = "%02d:%02d" % (minutes, seconds)

        embed = discord.Embed(
            title=vc.source.title,
            url=vc.source.web_url,
            description=f"Di-Request oleh {vc.source.requester.mention} | `{duration}`", 
            color=ctx.guild.get_member(self.bot.user.id).color
        )
        embed.set_author(icon_url="https://i.giphy.com/media/JRCsHUHcD6v1NPfuYM/giphy.gif", name="Sedang Diputar")
        await ctx.send(embed=embed)

    @commands.command(name='volume', aliases=['vol', 'v'])
    async def change_volume(self, ctx, *, vol: float=None):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Tidak sedang terhubung ke voice channel manapun.", color=0xff0000)
            return await ctx.send(embed=embed)
        
        if not vol:
            embed = discord.Embed(title="", description=f"🔊 **{(vc.source.volume)*100}%**", color=ctx.guild.get_member(self.bot.user.id).color)
            return await ctx.send(embed=embed)

        if not 0 < vol < 101:
            embed = discord.Embed(title="", description="Mohon masukkan angka antara `0` sampai `100`", color=0xff0000)
            return await ctx.send(embed=embed)

        if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
            player = self.get_player(ctx)

            if vc.source:
                vc.source.volume = vol / 100

            player.volume = vol / 100
            embed = discord.Embed(title="", description=f'Volume diatur ke **{vol}%**', color=ctx.guild.get_member(self.bot.user.id).color)
            await ctx.send(embed=embed)
        else:
            await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")

    @commands.command(name='leave', aliases=["dc", "disconnect"])
    async def leave_(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Tidak sedang terhubung ke voice channel manapun.", color=0xff0000)
            return await ctx.send(embed=embed)

        

        if ctx.author.voice.channel == ctx.guild.get_member(self.bot.user.id).voice.channel:
            if (random.randint(0, 1) == 0):
                await ctx.message.add_reaction('⏏')
            await ctx.send('🚪 Keluar dari voice channel.')

            await self.cleanup(ctx.guild)
        else:
            await ctx.reply("Kamu harus berada di vc yang sama dengan bot untuk mengakses perintah ini!")

    @commands.command(aliases=["lirik", "ly"])
    async def lyrics(self, ctx, *judul):
        vc = ctx.voice_client
        player = self.get_player(ctx)
        if not player.current:
            if not judul:
                embed = discord.Embed(title="", description="Tidak ada Audio yang sedang diputar. Masukkan kata kunci pencarian!", color=0xff0000)
                return await ctx.send(embed=embed)
            else:
                carilirik = "%20".join(judul)
                api = requests.get(f"https://some-random-api.ml/lyrics?title={carilirik}").json()
                judullagu = api["title"]
                artis = api["author"]
                lirik = api["lyrics"]
                fotoalbum = api["thumbnail"]["genius"]
                links = api["links"]["genius"]

                embed = discord.Embed(
                    title = f"{artis} - {judullagu}",
                    url = links,
                    description = lirik,
                    color = ctx.guild.get_member(self.bot.user.id).color
                )
                embed.set_thumbnail(url=fotoalbum)
                embed.set_footer(text=f"Di-Request oleh {ctx.author.name}  |  Lirik diberdayakan oleh Genius", icon_url=ctx.author.avatar_url)
                return await ctx.send(embed=embed)
        elif not judul and player.current:
            #convert string jadi list
            def Convert(string): 
                li = list(string.split(" "))
                return li 
            
            str1 = vc.source.title
            judullaguh = Convert(str1)

            carilirik = "%20".join(judullaguh)
            print(carilirik)
            api = requests.get(f"https://some-random-api.ml/lyrics?title={carilirik}").json()
            judullagu = api["title"]
            artis = api["author"]
            lirik = api["lyrics"]
            fotoalbum = api["thumbnail"]["genius"]
            links = api["links"]["genius"]

            embed = discord.Embed(
                title = f"{artis} - {judullagu}",
                url = links,
                description = lirik,
                color = ctx.guild.get_member(self.bot.user.id).color
            )
            embed.set_thumbnail(url=fotoalbum)
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name}  |  Lirik diberdayakan oleh Genius", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=embed)
        else:
            carilirik = "%20".join(judul)
            api = requests.get(f"https://some-random-api.ml/lyrics?title={carilirik}").json()
            judullagu = api["title"]
            artis = api["author"]
            lirik = api["lyrics"]
            fotoalbum = api["thumbnail"]["genius"]
            links = api["links"]["genius"]

            embed = discord.Embed(
                title = f"{artis} - {judullagu}",
                url = links,
                description = lirik,
                color = ctx.guild.get_member(self.bot.user.id).color
            )
            embed.set_thumbnail(url=fotoalbum)
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name}  |  Lirik diberdayakan oleh Genius", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=embed)

        
        

        
        

        
        
        

def setup(bot):
    bot.add_cog(Music(bot))
