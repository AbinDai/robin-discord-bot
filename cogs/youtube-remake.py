import discord, asyncio
from youtubesearchpython import VideosSearch, PlaylistsSearch, ChannelsSearch
from discord.ext import commands

class YouTube(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["yt"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtube(self, ctx, *, pencarian:str):
        try:
            videosSearch = VideosSearch(pencarian, limit=1)
            hasil = videosSearch.result()
            link = hasil["result"][0]["link"]

            await ctx.send(f"<:YouTube:825017821200515083> **Hasil pencarian teratas __{pencarian}__ di YouTube:**\n{link}")
        except:
            embed = discord.Embed(title=f"❌ Tidak ditemukan Video apapun dengan kata kunci __{pencarian}__.", color=0xff0000)
            await ctx.reply(embed=embed)
    @youtube.error
    async def on_youtube_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan kata kunci pencarianmu!\nContoh: `r!yt rick astley never gonna give you up`")
        
    @commands.command(aliases=["ytplaylist"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtubeplaylist(self, ctx, *, playlist):
        try:
            playlistsSearch = PlaylistsSearch(playlist, limit=1)
            hasil = playlistsSearch.result()

            link = hasil["result"][0]["link"]
            nama_playlist = hasil["result"][0]["title"]
            jumlah_video = hasil["result"][0]["videoCount"]
            channel_pengunggah = hasil["result"][0]["channel"]["name"]
            link_channel_pengunggah = hasil["result"][0]["channel"]["link"]
            thumbnail = hasil["result"][0]["thumbnails"][0]["url"]

            embed = discord.Embed(
                title = f"<:YouTube:825017821200515083> Hasil Teratas Pencarian Playlist __{playlist}__ di YouTube",
                color = 0xff0000
            )
            embed.set_thumbnail(url=thumbnail)
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="Nama Playlist", value=f"[{nama_playlist}]({link})", inline=False)
            embed.add_field(name="Jumlah Video", value=jumlah_video, inline=False)
            embed.add_field(name="Channel Pengunggah", value=f"[{channel_pengunggah}]({link_channel_pengunggah})", inline=False)
            await ctx.send(link, embed=embed)
        except:
            embed = discord.Embed(title=f"❌ Tidak ditemukan Playlist apapun dengan kata kunci __{playlist}__.", color=0xff0000)
            await ctx.reply(embed=embed)
    @youtubeplaylist.error
    async def on_youtubeplaylist_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Tuliskan nama playlist yang mau kamu cari!\nContoh: `r!ytplaylist rick astley songs`")

    @commands.command(aliases=["ytchannel"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtubechannel(self, ctx, *, channel:str):
        try:
            channelsSearch = ChannelsSearch(channel, limit=1)
            hasil = channelsSearch.result()

            namachannel = hasil["result"][0]["title"]
            fotochannel = hasil["result"][0]["thumbnails"][0]["url"]
            jumlahvideo = hasil["result"][0]["videoCount"]
            deskripsich = hasil["result"][0]["descriptionSnippet"][0]["text"]
            subscribers = hasil["result"][0]["subscribers"]
            linkchannel = hasil["result"][0]["link"]

            embed = discord.Embed(
                title = f"<:YouTube:825017821200515083> Hasil Pencarian Channel Teratas __{channel}__ di YouTube",
                color = 0xff0000
            )
            embed.set_thumbnail(url=f"https:{fotochannel}")
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="Nama Channel", value=f"[{namachannel}]({linkchannel})", inline=False)
            embed.add_field(name="Deskripsi Channel", value=deskripsich, inline=False)
            embed.add_field(name="Subscribers", value=subscribers, inline=False)
            embed.add_field(name="Jumlah Video", value=jumlahvideo, inline=False)
            await ctx.send(linkchannel, embed=embed)
        except:
            embed = discord.Embed(title=f"❌ Tidak ditemukan channel apapun dengan kata kunci __{channel}__.", color=0xff0000)
            await ctx.reply(embed=embed)
    @youtubechannel.error
    async def on_youtubechannel_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Tuliskan channel yang mau kamu cari!\nContoh: `r!youtubechannel Rick Astley`")            

    @commands.command(aliases=["ytsearch"])
    async def youtubesearch(self, ctx, *, pencarian:str):
        try:
            videosSearch = VideosSearch(pencarian, limit=10)
            hasil = videosSearch.result()

            #kita cmn butuh judul, link, sama durasi
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
                title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                            f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                            f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                            f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                            f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                            f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                            f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                            f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                            f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                            f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                color = 0xff0000
            )
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name} | Balas dengan angka yang tertera pada daftar untuk mendapatkan videonya. Timeout dalam 30 detik.", icon_url=ctx.author.avatar_url)
            pesan_awal = await ctx.send(embed=embed)

            try:
                msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30)
                if msg.content.lower() == "1":
                    embed = discord.Embed(
                        title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                        description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                    f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                    f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                    f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                    f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                    f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                    f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                    f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                    f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                    f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                        color = 0xff0000
                    )
                    embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await pesan_awal.edit(embed=embed)

                    await ctx.send(link1)
                elif msg.content.lower() == "2":
                    embed = discord.Embed(
                        title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                        description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                    f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                    f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                    f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                    f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                    f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                    f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                    f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                    f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                    f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                        color = 0xff0000
                    )
                    embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await pesan_awal.edit(embed=embed)

                    await ctx.send(link2)
                elif msg.content.lower() == "3":
                    embed = discord.Embed(
                        title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                        description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                    f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                    f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                    f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                    f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                    f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                    f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                    f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                    f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                    f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                        color = 0xff0000
                    )
                    embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await pesan_awal.edit(embed=embed)

                    await ctx.send(link3)
                elif msg.content.lower() == "4":
                    embed = discord.Embed(
                        title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                        description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                    f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                    f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                    f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                    f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                    f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                    f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                    f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                    f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                    f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                        color = 0xff0000
                    )
                    embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await pesan_awal.edit(embed=embed)

                    await ctx.send(link4)
                elif msg.content.lower() == "5":
                    embed = discord.Embed(
                        title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                        description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                    f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                    f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                    f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                    f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                    f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                    f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                    f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                    f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                    f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                        color = 0xff0000
                    )
                    embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await pesan_awal.edit(embed=embed)

                    await ctx.send(link5)
                elif msg.content.lower() == "6":
                    embed = discord.Embed(
                        title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                        description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                    f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                    f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                    f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                    f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                    f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                    f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                    f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                    f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                    f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                        color = 0xff0000
                    )
                    embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await pesan_awal.edit(embed=embed)

                    await ctx.send(link6)
                elif msg.content.lower() == "7":
                    embed = discord.Embed(
                        title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                        description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                    f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                    f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                    f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                    f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                    f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                    f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                    f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                    f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                    f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                        color = 0xff0000
                    )
                    embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await pesan_awal.edit(embed=embed)

                    await ctx.send(link7)
                elif msg.content.lower() == "8":
                    embed = discord.Embed(
                        title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                        description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                    f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                    f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                    f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                    f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                    f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                    f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                    f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                    f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                    f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                        color = 0xff0000
                    )
                    embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await pesan_awal.edit(embed=embed)

                    await ctx.send(link8)
                elif msg.content.lower() == "9":
                    embed = discord.Embed(
                        title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                        description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                    f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                    f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                    f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                    f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                    f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                    f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                    f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                    f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                    f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                        color = 0xff0000
                    )
                    embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await pesan_awal.edit(embed=embed)

                    await ctx.send(link9)
                elif msg.content.lower() == "10":
                    embed = discord.Embed(
                        title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                        description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                    f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                    f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                    f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                    f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                    f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                    f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                    f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                    f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                    f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                        color = 0xff0000
                    )
                    embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await pesan_awal.edit(embed=embed)

                    await ctx.send(link10)
            except asyncio.TimeoutError:
                embed = discord.Embed(
                    title = f"<:YouTube:825017821200515083> Mencari __{pencarian}__...",
                    description = f"`1` [{judul1}]({link1}) `{durasi1}`\n"
                                f"`2` [{judul2}]({link2}) `{durasi2}`\n"
                                f"`3` [{judul3}]({link3}) `{durasi3}`\n"
                                f"`4` [{judul4}]({link4}) `{durasi4}`\n"
                                f"`5` [{judul5}]({link5}) `{durasi5}`\n"
                                f"`6` [{judul6}]({link6}) `{durasi6}`\n"
                                f"`7` [{judul7}]({link7}) `{durasi7}`\n"
                                f"`8` [{judul8}]({link8}) `{durasi8}`\n"
                                f"`9` [{judul9}]({link9}) `{durasi9}`\n"
                                f"`10` [{judul10}]({link10}) `{durasi10}`\n",
                    color = 0xff0000
                )
                embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
                await pesan_awal.edit(embed=embed)
        except:
            embed = discord.Embed(
                title = f"❌ Tidak ditemukan hasil apapun dari __{pencarian}__.",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)
    @youtubesearch.error
    async def on_youtubesearch_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Tuliskan kata kunci pencarianmu!\nContoh: `r!youtubesearch rickroll`")

def setup(client):
    client.add_cog(YouTube(client))