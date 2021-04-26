import discord, DiscordUtils#, hus
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("HELP.PY SIAP!")

    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #==================================================[ help ]====================================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    @commands.group(invoke_without_command=True, aliases=["help"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def h(self, ctx):
        embed1 = discord.Embed(
            title = "Daftar Command Bot Robin Lengkap",
            description = """
            Halo! Prefiksku adalah `r!` dan `robin ` :)
            
            Bot ini memilki beragam command yang terdiri atas beberapa kategori. Untuk melihat daftar command yang tersedia, silahkan navigasikan embed ini ke halaman-halaman selanjutnya. Kamu juga bisa gunakan `r!help [nama command]` untuk mengetahui rincian dari sebuah command, juga kamu bisa menggunakan `r!help [nama kategori]` untuk melihat daftar-daftar command yang berada pada sebuah kategori. Ketik `r!help allcommands` untuk melihat daftar command FULL.

            Punya kendala atau bug saat menggunakan bot ini? Kirimkan masukan Anda dengan mengeksekusi command `r!saran [isi saran/masukan]`, atau bisa dengan gabung ke help server nya langsung. Link [disini](https://discord.gg/rZqsvrMdwR).

            Pertama kali main bot di Discord? Nonton [disini](https://www.youtube.com/watch?v=-51AfyMqnpI) untuk melihat video tutorial cara menggunakan bot di Discord.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed1.set_thumbnail(url=self.client.user.avatar_url)
        embed1.add_field(name="Berikut kategori-kategori command yang tersedia :)", value="```py\n'Moderasi' • 'Fun' • 'Interaksi' • 'Gambar' • 'Utilitas' • 'Lain-Lain'\n```")
        embed1.set_footer(text=f"Halaman 1/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        embed2 = discord.Embed(
            description = "Berikut command-command yang tersedia pada kategori `Moderasi`.\n```py\n'kick' • 'ban' • 'unban' • 'clear' • 'changenick' • 'newrole' • 'deleterole' • 'giverole' • 'removerole'\n```",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed2.set_author(name='Kategori "Moderasi"', icon_url=self.client.user.avatar_url)
        embed2.set_footer(text=f"Halaman 2/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        embed3 = discord.Embed(
            description = "Berikut command-command yang tersedia pada kategori `Fun`.\n```py\n'titit' • 'lovecalc' • '_8ball' • 'keqing' • 'tes' • 'geh' • 'kaori' • 'tabok' • 'bonk' • 'saygoodbye' • 'say' • 'sayy' • 'sayem' • 'rate' • 'poll' • 'acakhuruf' • 'acakangka' • 'face'\n```",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed3.set_author(name='Kategori "Fun"', icon_url=self.client.user.avatar_url)
        embed3.set_footer(text=f"Halaman 3/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        embed4 = discord.Embed(
            description = "Berikut command-command yang tersedia pada kategori `Interaksi`.\n```py\n'blush' • 'lick' • 'cry' • 'nom' • 'pout' • 'poke' • 'kiss' • 'punch' • 'slap' • 'sleep' • 'smug' • 'tickle' • 'hug' • 'pat' • 'wink'\n```",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed4.set_author(name='Kategori "Interaksi"', icon_url=self.client.user.avatar_url)
        embed4.set_footer(text=f"Halaman 4/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        embed5 = discord.Embed(
            description = "Berikut command-command yang tersedia pada kategori `Gambar`.\n```py\n'cat' • 'dog' • 'bird' • 'panda' • 'pikachu' • 'kopi' • 'duck' • 'wasted' • 'hitamputih' • 'invert' • 'bright' • 'threshold' • 'sepia' • 'redtint' • 'greentint' • 'bluetint' • 'youtubecomment' • 'gun' • 'lgbt' • 'grab' • 'truth' • 'simp' • 'glitch' • 'hearts' • 'spongebobtimecard' • 'hitlernews' • 'like' • 'dislike' • 'rip' • 'jokeoverhead' • 'jail' • 'beauty' • 'communist' • 'triggeered' • 'changemymind' • 'clyde' • 'trash' • 'respect' • 'disgusting' • 'ferbtv' • 'graph' • 'judul' • 'disconnected' • 'chapta' • 'burn' • 'swirl' • 'implode' • 'wave' • 'pixelate' • 'fox' • 'trumppost' • 'minecraftcompleted' • 'emergencymeeting' • 'firsttime' • 'imspeed' • 'heaven' • 'stonks' • 'notstonks' • 'tableflip' • 'wolverine' • 'neko' • 'avatars' • 'trap' • 'wallpapers'\n```",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed5.set_author(name='Kategori "Gambar"', icon_url=self.client.user.avatar_url)
        embed5.set_footer(text=f"Halaman 5/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        embed6 = discord.Embed(
            description = "Berikut command-command yang tersedia pada kategori `Utilias`.\n```py\n'avatar' • 'serverinfo' • 'servericon' • 'userinfo' • 'roleinfo' • 'emoji' • 'binertxt' • 'biner' • 'afk' • 'color' • 'kbbi' • 'corona' • 'gempa' • 'kodepos' • 'translate' • 'batik' • 'youtube'\n```",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed6.set_author(name='Kategori "Utilitas"', icon_url=self.client.user.avatar_url)
        embed6.set_footer(text=f"Halaman 6/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        embed7 = discord.Embed(
            description = "Berikut command-command yang tersedia pada kategori `Lain-Lain`.\n```py\n'about' • 'invite' • 'ping' • 'uptime' • 'upvote'\n```",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed7.set_author(name='Kategori "Lain-Lain"', icon_url=self.client.user.avatar_url)
        embed7.set_footer(text=f"Halaman 7/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("⏪", "first")
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")
        paginator.add_reaction("⏩", "last")
        embed_embed = [embed1, embed2, embed3, embed4, embed5, embed6, embed7]
        await paginator.run(embed_embed)

    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #===============================================[ help kategori ]==============================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def moderasi(self, ctx):
        embed = discord.Embed(
            description = 
            """
            `r!ban`: Mem-Ban seseorang.
            `r!clear`: Menghapus pesan.
            `r!kick`: Menendang keluar seorang member.
            `r!unban`: Melepas Ban seseorang.
            `r!changenick`: Mengubah nickname seorang user.
            `r!newrole`: Membuat Role baru.
            `r!deleterole`: Menghapus Role.
            `r!giverole`: Memberikan Role kepada user.
            `r!removerole`: Mencabut Role dari seorang user.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name='Daftar Command dalam Kategori "Moderasi"', icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f"Halaman 1/1 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fun(self, ctx):
        embed1 = discord.Embed(
            description = 
            """
            `r!8ball`: Menjawab pertanyaan kamu yang bertema Ya/Tidak dengan jawaban acak.
            `r!keqing`: Menampilkan teks "KEQING WANGY WANGY" lengkap.
            `r!tes`: Memeberitahu bahwa tes berhasil.
            `r!geh`: Menampilkan GIF Pepe Julian Onzeima.
            `r!kaori`: Menampilkan GIF Kaori Miyazono.
            `r!tabok`: Menampilkan 2 foto orang *nabok* secara acak.
            `r!bonk`: Menampilkan foto meme doge "bonk"
            `r!saygoodbye`: Menampilkan GIF parodi video Rickroll
            `r!say`: Mengikuti apa yang dikatakan user (tapi dengan nama).
            `r!sayy`: Mengikuti kata user (tapi tanpa nama).
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed1.set_author(name='Daftar Command dalam Kategori "Fun"', icon_url=self.client.user.avatar_url)
        embed1.set_footer(text=f"Halaman 1/2 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        
        embed2 = discord.Embed(
            description = 
            """
            `r!sayem`: Mengikuti apa kata user (tapi diisi dalam embed).
            `r!rate`: Menilai objek.
            `r!poll`: Membuat jajak pendapat.
            `r!lovecalc`: Menghitung persentase tingkat kecintaan, ||eeeaaaa :v||.
            `r!titit`: Mengukur panjang t*tit orang yang kamu mention :v (jgn dibawa serius awokawok)
            `r!acakhuruf`: Mengacak huruf dari A sampai Z dan mengirimkan hasilnya ke ruangan chat.
            `r!acakangka`: Mengacak angka sesuai *range* yang diberikan.
            `r!face`: Menampilkan emot wajah secara acak.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed2.set_author(name='Daftar Command dalam Kategori "Fun"', icon_url=self.client.user.avatar_url)
        embed2.set_footer(text=f"Halaman 2/2 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")

        embed_embed = [embed1, embed2]

        await paginator.run(embed_embed)

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def interaksi(self, ctx):
        embed1 = discord.Embed(
            description = 
            """
            `r!hug`: Memeluk seorang user yang kamu mention.
            `r!pat`: Menepuk seorang user yang kamu mention.
            `r!wink`: Berkedip.
            `r!kiss`: Mencium seorang user yang kamu mention.
            `r!cry`: *Mengsedih*.
            `r!blush`: Malu :v
            `r!lick`: Menjilat.
            `r!nom`: Menggigit.
            `r!pout`: Ngambek.
            `r!poke`: Colek pipi.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed1.set_author(name='Daftar Command dalam Kategori "Interaksi"', icon_url=self.client.user.avatar_url)
        embed1.set_footer(text=f"Halaman 1/2 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        
        embed2 = discord.Embed(
            description = """
            `r!punch`: Tinju orang.
            `r!slap`: Nampar.
            `r!sleep`: Tidur.
            `r!smug`: Nyombong.
            `r!tickle`: Nggelitik.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed2.set_author(name='Daftar Command dalam Kategori "Interaksi"', icon_url=self.client.user.avatar_url)
        embed2.set_footer(text=f"Halaman 2/2 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")

        embed_embed = [embed1, embed2]

        await paginator.run(embed_embed)
        

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gambar(self, ctx):
        embed1 = discord.Embed(
            description = 
            """
            `r!cat`: Menampilkan foto-foto kucing secara acak.
            `r!dog`: Menampilkan foto-foto anjing secara acak.
            `r!bird`: Menampilkan foto-foto burung secara acak.
            `r!panda`: Menampilkan foto-foto Panda secara acak.
            `r!pikachu`: Menampilkan GIF-GIF Pikachu secara acak.
            `r!kopi`: Menampilkan foto-foto kopi secara acak.
            `r!duck`: Menampilkan gambar-gambar bebek secara acak.
            `r!wasted`: Menampilkan *overlay* "wasted" ke foto profil seseorang.
            `r!hitamputih`: Membuat foto profil seseorang menjadi hitam putih.
            `r!invert`: Membalik warna foto profil seseorang.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed1.set_author(name='Daftar Command dalam Kategori "Gambar"', icon_url=self.client.user.avatar_url)
        embed1.set_footer(text=f"Halaman 1/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        
        embed2 = discord.Embed(
            description = 
            """
            `r!bright`: Menerangkan foto profil seseorang.
            `r!threshold`: Membuat foto profil seseorang menjadi dua warna.
            `r!sepia`: Membuat foto profil seseorang menguning.
            `r!redtint`: Memerahkan foto profil seseorang.
            `r!greentint`: Menghijaukan foto profil seseorang.
            `r!bluetint`: Membirukan foto profil seseorang.
            `r!gun`: Menambahkan overlay pistol ke foto profil seseorang.
            `r!lgbt`: Menambahkan efek bendera LGBT pada foto profil seseorang.
            `r!grab`: Menambahkan overlay tangan pada foto profil seseorang.
            `r!truth`: Menambahkan teks pada temmplate meme.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed2.set_author(name='Daftar Command dalam Kategori "Gambar"', icon_url=self.client.user.avatar_url)
        embed2.set_footer(text=f"Halaman 2/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        
        embed3 = discord.Embed(
            description = 
            """
            `r!simp`: Menambahkan overlay "SIMP" ke foto profil seseorang.
            `r!glitch`: Menambahkan efek glitch pada foto profil seseorang.
            `r!hearts`: Menambahkan overlay hati pada foto profil seseorang.
            `r!spongebobtimecard`: Menambahkan teks pada kartu waktu serial Spongebob.
            `r!hitlernews`: Menambahkan gambar foto profil sesoerang pada sebuah template berita di kartun Simpsons.
            `r!like`: Menambahkan foto preofil sesoerand pada sebuah template.
            `r!dislike`: Menambahkan foto preofil sesoerand pada sebuah template.
            `r!rip`: Menambahkan foto profil seorang user pada template batu nisan.
            `r!jokeoverhead`: Menambahkan foto profil seorang user pada template meme.
            `r!jail`: Menambahkan efek jeruji besi pada foto profil seseorang.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed3.set_author(name='Daftar Command dalam Kategori "Gambar"', icon_url=self.client.user.avatar_url)
        embed3.set_footer(text=f"Halaman 3/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        
        embed4 = discord.Embed(
            description = 
            """
            `r!beauty`: Menambahkan foto profil sesoerang pada sebuah template meme.
            `r!communist`: Menambahkan overlay palu arit ke foto profil seorang user.
            `r!youtubecomment`: Membuat foto komentar YouTube palsu.
            `r!triggered`: Menambahkan efek *triggered* pada foto profil seseorang.
            `r!changemymind`: Menabahkan teks pada template *change my mind*.
            `r!clyde`: Menambahkan teks pada chat Clyde.
            `r!trash`: Menambahkan foto profil seseorang pada sebuah template meme.
            `r!respect`: Hormat.
            `r!disgusting`: Jijik.
            `r!ferbtv`: Menambahkan foto profil seseorang pada sebuah template.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed4.set_author(name='Daftar Command dalam Kategori "Gambar"', icon_url=self.client.user.avatar_url)
        embed4.set_footer(text=f"Halaman 4/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        embed5 = discord.Embed(
            description = 
            """
            `r!graph`: Meletakkan foto profil seseorang pada sebuah template.
            `r!jadul`: Menambahkan efek jadul pada foto profil seseorang.
            `r!disconnected`: Menambahkan teks pada layar *disconnect* di game Minecraft.
            `r!chapta`: Mengubah teks menjadi tulisan chapta.
            `r!burn`: Bakar.
            `r!swirl`: Menambahkan efek putar pada foto profil seseorang.
            `r!implode`: Menambahkan efek "ngumpul di tengah" pada foto profil seorang user.
            `r!wave`: Menambahkan efek gelombang pada foto profil seorang user.
            `r!pixelate`: Mengubah foto profil seseorang menjadi *burik* awokawok.
            `r!fox`: Menampilkan gambar-gambar rubah secara acak.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed5.set_author(name='Daftar Command dalam Kategori "Gambar"', icon_url=self.client.user.avatar_url)
        embed5.set_footer(text=f"Halaman 5/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        embed6 = discord.Embed(
            description = 
            """
            `r!trumppost`: Menampilkan foto postingan presiden Trump di Twitter.
            `r!minecraftcompleted`: Menampilkan foto Challenge Completed dari game Minecraft.
            `r!emergencymeeting`: Menampilkan template meme Emergency Meeting dari game Among Us.
            `r!firsttime`: Menampilkan template First Time.
            `r!imspeed`: Menampilkan template I'm Speed dari film Cars.
            `r!heaven`: Menampilkan template surga.
            `r!stonks`: Menampilkan template Meme Man Stonks.
            `r!notstonks`: Menampilkan template Meme Man Not Stonks.
            `r!tableflip`: Menampilkan template Stick Man yang sedang melempar meja.
            `r!wolverine`: Menampilkan template meme orang guling lagi liat foto.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed6.set_author(name='Daftar Command dalam Kategori "Gambar"', icon_url=self.client.user.avatar_url)
        embed6.set_footer(text=f"Halaman 6/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        embed7 = discord.Embed(
            description = 
            """
            `r!neko`: Menampilkan foto-foto karakter gadis kucing Anime secara acak.
            `r!avatars`: Menampilkan foto-foto profil Anime secara acak.
            `r!trap`: Menampilkan foto-foto karakter *trap* secara acak.
            `r!wallpapers`: Menampilkan wallpaper-wallpaper Anime secara acak.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed7.set_author(name='Daftar Command dalam Kategori "Gambar"', icon_url=self.client.user.avatar_url)
        embed7.set_footer(text=f"Halaman 7/7 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")

        embed_embed = [embed1, embed2, embed3, embed4, embed5, embed6, embed7]

        await paginator.run(embed_embed)
        

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def utilitas(self, ctx):
        embed1 = discord.Embed(
            description = 
            """
            `r!color`: Menampilkan informasi warna.
            `r!kbbi`: Menampilkan arti kata dalam KBBI.
            `r!corona`: Menampilkan statistik virus Corona di Indonesia.
            `r!gempa`: Menampilkan statistik gempa terkini yang terjadi di Indonesia.
            `r!kodepos`: Menampilkan info kode pos.
            `r!translate`: Menerjemahkan kata/kalimat.
            `r!batik`: Menampilkan info batik.
            `r!afk`:  Mengatur status AFK.
            `r!biner`: Mengonversi tulisan biasa menjadi angka biner.
            `r!binertxt`: Mengonversi angka biner menjadi teks biasa.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed1.set_author(name='Daftar Command dalam Kategori "Utilitas"', icon_url=self.client.user.avatar_url)
        embed1.set_footer(text=f"Halaman 1/2 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        embed2 = discord.Embed(
            description = 
            """
            `r!avatar`: Menampilkan foto profil seorang user.
            `r!serverinfo`: Menampilkan informasi server.
            `r!servericon`: Menampilkan foto server.
            `r!userinfo`: Menampilkan informasi seorang user
            `r!roleinfo`: Menampilkan informasi Role.
            `r!emoji`: Menampilkan informasi Emoji.
            `r!youtube`: Menampilkan informasi channel YouTube.
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed2.set_author(name='Daftar Command dalam Kategori "Utilitas"', icon_url=self.client.user.avatar_url)
        embed2.set_footer(text=f"Halaman 2/2 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")

        embed_embed = [embed1, embed2]

        await paginator.run(embed_embed)

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lain_lain(self, ctx):
        embed = discord.Embed(
            description = 
            """
            `r!about`: Menampilkan info bot.
            `r!invite`: Menampilkan link invite bot.
            `r!ping`: Menampilkan latensi bot.
            `r!uptime`: Menampilkan waktu aktif bot.
            `r!upvote`: Menampilkan link untuk nge-Vote saya di [top.gg](https://top.gg/).
            """,
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name='Daftar Command dalam Kategori "Utilitas"', icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f"Halaman 1/1 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #=============================================[ help command ]=================================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ban(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Ban", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`ban`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mem-Ban seseorang dari server.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang mau kamu ban.', inline=False)
        embed.add_field(name='Contoh:', value='`r!ban @Nathz#6498`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["clr", "purge"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clear(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Clear", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`clear`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='`clr, purge`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menghapus pesan sebanyak jumlah yang diberikan.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian tuliskan jumlah pesan yang ingin kamu hapus.', inline=False)
        embed.add_field(name='Contoh:', value='`r!clr 5`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["kck", "hus", "usir", "keluarkan", "tendang"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Kick", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`kick`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='`kck, hus, usir, keluarkan, tendang, kck`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengeluarkan seorang user dari server.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian tuliskan mention orang yang mau kamu kick.', inline=False)
        embed.add_field(name='Contoh:', value='`r!kck @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unban(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Unban", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`unban`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Melepas ban seseorang yang pernah di-ban.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian tuliskan ID orang yang mau kamu unban.', inline=False)
        embed.add_field(name='Contoh:', value='`r!unban 550953412489904129`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["nickname", "nick", "changename"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def changenick(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Changenick", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`changenick`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='`nickname, nick, changename`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengubah nickname seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, sebut orang yang nick nya mau kamu ganti, dan tuliskan nickname apa yang mau kamu berikan padanya.', inline=False)
        embed.add_field(name='Contoh:', value='`r!changenick @Abin#4405 si abin`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["createrole", "bikinrole", "makerole", "addrole"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def newrole(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Newrole", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`newrole`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='`createrole, bikinrole, makerole, addrole`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Membuat Role baru.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, tulis nama role nya (apit menggunakan tanda ""), kemudian tuliskan kode HEX untuk warna role nya (opsional) (tanpa diawali dengan `#`atau `0x`).', inline=False)
        embed.add_field(name='Contoh:', value='`r!newrole "anak rajin" 00ff00`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["hapusrole"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def deleterole(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Deleterole", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`deleterole`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='`hapusrole`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menghapus role.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemuidian sebutkan role yang mau kamu hapus.', inline=False)
        embed.add_field(name='Contoh:', value='`r!deleterole @anak rajin`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def giverole(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Giverole", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`giverole`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Memberikan role kepada seorang user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, sebutkan orang yang akan kalian berikan role, kemudian sebutkan role mana yang akan kamu kasih.', inline=False)
        embed.add_field(name='Contoh:', value='`r!giverole @Abin @anak rajin`', inline=False)
        await ctx.send(embed=embed)   
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def removerole(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Removerole", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`removerole`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mencabut role dari seorang user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, sebutkan orang yang akan kalian cabut role nya, kemudian sebutkan role mana yang akan kamu cabut.', inline=False)
        embed.add_field(name='Contoh:', value='`r!removerole @Abin @anak rajin`', inline=False)
        await ctx.send(embed=embed)     














    
    
    @h.command(aliases=["kntl", "dicksize"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def titit(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > T*tit", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`titit`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`kntl, dicksize`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengukur panjang t*t1t orang yang kamu mention :v jgn baper btw.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention/tuliskan nama dua orang yang mau kamu ukur tititnya :V.', inline=False)
        embed.add_field(name='Contoh:', value='`r!titit @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["lc", "kalkcinta"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lovecalc(self, ctx):
        embed = discord.Embed(
            colour  = 0xff0000
        )
        embed.set_author(name="Help > Lovecalc", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`lovecalc`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`lc, kalkcinta`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menghitung presentase rasa cinta, ||eeeaaaaa :v||.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention/tuliskan nama dua orang yang mau kamu jodohkan.', inline=False)
        embed.add_field(name='Contoh:', value='`r!lovecalc indri udin`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _8ball(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > 8ball", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`8ball`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`8b, 8ball`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menjawab pertanyaanmu yang bertema ya/tidak dengan jawaban random. (Jgn dibawa serius :v)', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian tuliskan pertanyaan yang mau kamu tanyakan.', inline=False)
        embed.add_field(name='Contoh:', value='`r!8b gw ganteng ga? :v`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def keqing(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Keqing", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`keqing`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan teks "KEQING WANGY WANGY" lengkap beserta gambar.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini tidak memerlukan argumen tambahan, jadi kamu cukup menuliskan command nya saja.', inline=False)
        embed.add_field(name='Contoh:', value='`r!keqing`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["test"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tes(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Tes", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`tes`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`test`')
        embed.add_field(name="Cooldown", value="Tidak ada", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan tulisan `Tes Anda berhasil`.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini tidak memerlukan argumen tambahan, jadi kamu cukup menuliskan command nya saja.', inline=False)
        embed.add_field(name='Contoh:', value='`r!tes`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["gay", "gei", "gae"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def geh(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Geh", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`geh`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`gay, gei, gae`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan GIF dan foto-foto Pepe Julian Onzeima pada sebuah interview gay di salah satu stasiun TV di Afrika.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian kamu bisa tag orang yang mau kamu jadikan sasaran, atau bisa juga tidak menambahkan argumen tambahan.', inline=False)
        embed.add_field(name='Contoh:', value='`r!geh`\n`r!geh @Ryn#7700`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kaori(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Kaori", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`kaori`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan GIF Kaori Miyazono dari Anime Shigatsu wa Kimi no Uso.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini juga tidak membutuhkan argumen tambahan, jadi kamu tinggal tulis nama command nya saja.', inline=False)
        embed.add_field(name='Contoh:', value='`r!kaori`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["thortaapo", "taapo"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tabok(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Tabok", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`tabok`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`taapo, thortaapo`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan dua gambar orang mau *nabok* secara acak.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini juga tidak membutuhkan argumen tambahan, jadi kamu tinggal tulis nama command nya saja.', inline=False)
        embed.add_field(name='Contoh:', value='`r!taapo`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bonk(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Bonk", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`bonk`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan meme doge "bonk".', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini juga tidak membutuhkan argumen tambahan, jadi kamu tinggal tulis nama command nya saja.', inline=False)
        embed.add_field(name='Contoh:', value='`r!bonk`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def saygoodbye(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Saygoodbye", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`saygoodbye`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan GIF ||Om Rick Astley bilang "say goodbye" versi animasi <:keanu_nunjuk:799114521347751996>||.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini juga tidak membutuhkan argumen tambahan, jadi kamu tinggal tulis nama command nya saja.', inline=False)
        embed.add_field(name='Contoh:', value='`r!saygoodbye`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def say(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Say", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`say`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengikuti apa kata user. Pesan asli si author akan dihapus tapi nama author akan tertera.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian tulis apa yang mau kamu katakan.', inline=False)
        embed.add_field(name='Contoh:', value='`r!say ketika kamu mengantuk, ya tidur lah! :V`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sayy(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Sayy", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`sayy`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengikuti apa yang dikatakan user, tapi nama author tidak akan tertera, dan pesan asli si author akan dihapus.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian tulis apa yang mau kamu katakan.', inline=False)
        embed.add_field(name='Contoh:', value='`r!sayy konnichiwa`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sayem(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Sayem", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`sayem`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengikuti apa yang dikatakan user, tapi perkataannya akan diletakkan di dalam sebuah embed. Pesan asli si author akan dihapus dan nama author tidak akan tertera.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian tulis apa yang mau kamu katakan.', inline=False)
        embed.add_field(name='Contoh:', value='`r!sayyem <--- ini adalah garis yang berwarna`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["nilai"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rate(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Rate", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`rate`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`nilai`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menilai sesuatu dengan nilai acak antara 1 sampai 10 (jgn dibawa serius oi :v).', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian tulis objek yang akan dinilai.', inline=False)
        embed.add_field(name='Contoh:', value='`r!rate nasi goreng`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["vote"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poll(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Poll", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`poll`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`vote`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Membuat jajak pendapat.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian tuliskan pendapatmu.', inline=False)
        embed.add_field(name='Contoh:', value='`r!poll tar mlm nobar anime?`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["randomletter"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def acakhuruf(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > AcakHuruf", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`acakhuruf`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`randomletter`')
        embed.add_field(name="Cooldown", value="10 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengacak huruf  dari A sampai Z.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini tidak butuh argumen tambahan.', inline=False)
        embed.add_field(name='Contoh:', value='`r!acakhuruf`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["randomnumber"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def acakangka(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > AcakAngka", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`acakangka`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`randomnumber`')
        embed.add_field(name="Cooldown", value="10 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengacak angka sesuai *range* yang diberikan.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian masukkan range yang kamu mau.', inline=False)
        embed.add_field(name='Contoh:', value='`r!acakangka 1 100` (maksudnya dari 1 sampai 100)', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def face(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Face", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`face`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan emot wajah secara acak.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini tidak butuh argumen tambahan..', inline=False)
        embed.add_field(name='Contoh:', value='`r!face`', inline=False)
        await ctx.send(embed=embed)














        

        

    
    
    @h.command(aliases=["menangis", "nangid", "nangis", "nyedih", "menyedih", "mengsad", "mengsedih"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cry(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Cry", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`cry`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Alias:', value='`menangis, nangid, nangis, nyedih, menyedih, mengsad, mengsedih`')
        embed.add_field(name='Deskripsi:', value='Nangis.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Bisa tanpa mention user, bisa juga iya.', inline=False)
        embed.add_field(name='Contoh:', value='`r!cry` (untuk diri sendiri)\n`r!cry @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["cium"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kiss(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Kiss", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`kiss`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`cium`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mencium seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention nama orang yang mau kamu cium.', inline=False)
        embed.add_field(name='Contoh:', value='`r!kiss @???#????`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["peluk"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hug(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Hug", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`hug`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`peluk`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Memeluk seorang userrrrrr uuuuuuuuu >/////<.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang mau kamu peluk <3.', inline=False)
        embed.add_field(name='Contoh:', value='`r!hug @[AFK] NakMon#3750`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["tepuk", "nepuk"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pat(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Nepuk", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`pat`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`tepuk, nepuk`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menepuk seorang userrrrrr uuuuuuuuu >/////<.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang mau kamu tepuk <3.', inline=False)
        embed.add_field(name='Contoh:', value='`r!pat @[AFK] NakMon#3750`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["kedip"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wink(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Wink", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`wink`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`kedip`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Berkedip.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini tidak butuh argumen tambahan, jadi tidak ada yang perlu ditambahkan.', inline=False)
        embed.add_field(name='Contoh:', value='`r!wink`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["blushed"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def blush(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Blush", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`blush`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`blushed`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Malu.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini punya argumen tamabahan **opsional**, yaitu member.', inline=False)
        embed.add_field(name='Contoh:', value='`r!blush`\n`r!blush @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["jilat"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lick(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Lick", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`lick`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`jilat`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menjilat seorang user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command-nya kemudian sebutkan orang yang mau kamu jilat.', inline=False)
        embed.add_field(name='Contoh:', value='`r!lick @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nom(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Nom", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`nom`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menggigit.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command-nya kemudian mention orang yang mau kamu gigit.', inline=False)
        embed.add_field(name='Contoh:', value='`r!nom @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pout(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Pout", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`pout`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mencibir.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini bisa dieksekusi dengan argumen tambahan yang opsional, yaitu member.', inline=False)
        embed.add_field(name='Contoh:', value='`r!pout`\n`r!pout @Abin#4405`', inline=False)
        await ctx.send(embed=embed)      
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poke(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Poke", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`poke`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mencolek pipi.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command-nya kemudian mention orang yang mau kamu colek di pipi.', inline=False)
        embed.add_field(name='Contoh:', value='`r!poke @Abin#4405`', inline=False)
        await ctx.send(embed=embed)  
    @h.command(aliases=["tinju"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def punch(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Punch", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`punch`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`tinju`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Meninju.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command-nya kemudian mention orang yang mau kamu tinju.', inline=False)
        embed.add_field(name='Contoh:', value='`r!punch @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["tampar"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Slap", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`slap`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`tampar`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampar.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command-nya kemudian mention orang yang mau kamu tampar.', inline=False)
        embed.add_field(name='Contoh:', value='`r!slap @Abin#4405`', inline=False)
        await ctx.send(embed=embed)  
    @h.command(aliases=["tidur"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sleep(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Sleep", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`sleep`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`tidur`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Yaaaa tidur...', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini tidak butuh argumen tambahan, tapi bisa kamu tambahkan member.', inline=False)
        embed.add_field(name='Contoh:', value='`r!sleep`\n`r!sleep @Abin#4405`', inline=False)
        await ctx.send(embed=embed)  
    @h.command(aliases=["sombong"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def smug(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Smug", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`smug`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`sombong`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menyombongkan diri...', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini tidak butuh argumen tambahan, tapi bisa kamu tambahkan member.', inline=False)
        embed.add_field(name='Contoh:', value='`r!smug`\n`r!smug @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["gelitik"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tickle(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Tickle", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`tickle`')
        embed.add_field(name='Kategori:', value='`Interaksi`')
        embed.add_field(name='Alias:', value='`gelitik`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menggelitik.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command-nya kemudian mention orang yang mau kamu gelitik.', inline=False)
        embed.add_field(name='Contoh:', value='`r!tickle @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    














    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wasted(self, ctx):
        embed = discord.Embed(
            colour  = 0x9d9d9d
        )
        embed.set_author(name="Help > Wasted", icon_url=f"https://some-random-api.ml/canvas/wasted?avatar={self.client.user.avatar_url_as(format='png', size=4096)}")
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`wasted`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek "wasted" GTA ke foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang foto profilnya mau kamu taruh efek ini.', inline=False)
        embed.add_field(name='Contoh:', value='`r!wasted @FebrieWhite#0233`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["htmpth", "grayscale"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hitamputih(self, ctx):
        embed = discord.Embed(
            colour  = 0x9d9d9d
        )
        embed.set_author(name="Help > HitamPutih", icon_url=f"https://some-random-api.ml/canvas/greyscale?avatar={self.client.user.avatar_url_as(format='png', size=4096)}")
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`hitamputih`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`htmpth, grayscale`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek hitam putih ke foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang foto profilnya mau kamu taruh efek ini.', inline=False)
        embed.add_field(name='Contoh:', value='`r!htmpth @FebrieWhite#0233`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invert(self, ctx):
        embed = discord.Embed(
            colour  = 0xd6cdb5
        )
        embed.set_author(name="Help > Invert", icon_url=f"https://some-random-api.ml/canvas/threshold?avatar={self.client.user.avatar_url_as(format='png', size=4096)}")
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`invert`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek warna terbalik ke foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang foto profilnya mau kamu taruh efek ini.', inline=False)
        embed.add_field(name='Contoh:', value='`r!invert @FebrieWhite#0233`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bright(self, ctx):
        embed = discord.Embed(
            colour  = 0xfffffa
        )
        embed.set_author(name="Help > Bright", icon_url=f"https://some-random-api.ml/canvas/threshold?avatar={self.client.user.avatar_url_as(format='png', size=4096)}")
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`bright`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek warna TERANG ke foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang foto profilnya mau kamu taruh efek ini.', inline=False)
        embed.add_field(name='Contoh:', value='`r!bright @FebrieWhite#0233`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["thr", "thrsld"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def threshold(self, ctx):
        embed = discord.Embed(
            colour  = 0xfffffa
        )
        embed.set_author(name="Help > Threshold", icon_url=f"https://some-random-api.ml/canvas/threshold?avatar={self.client.user.avatar_url_as(format='png', size=4096)}")
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`threshold`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`thr, thrsld`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek dua warna ke foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang foto profilnya mau kamu taruh efek ini.', inline=False)
        embed.add_field(name='Contoh:', value='`r!thr @FebrieWhite#0233`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sepia(self, ctx):
        embed = discord.Embed(
            colour  = 0xd3bc92
        )
        embed.set_author(name="Help > Sepia", icon_url=f"https://some-random-api.ml/canvas/sepia?avatar={self.client.user.avatar_url_as(format='png', size=4096)}")
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`sepia`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek warna kuning ke foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang foto profilnya mau kamu taruh efek ini.', inline=False)
        embed.add_field(name='Contoh:', value='`r!sepia @FebrieWhite#0233`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def redtint(self, ctx):
        embed = discord.Embed(
            colour  = 0xff0000
        )
        embed.set_author(name="Help > Redtint", icon_url=f"https://some-random-api.ml/canvas/red?avatar={self.client.user.avatar_url_as(format='png', size=4096)}")
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`redtint`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek warna merah ke foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang foto profilnya mau kamu taruh efek ini.', inline=False)
        embed.add_field(name='Contoh:', value='`r!redtint @FebrieWhite#0233`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def greentint(self, ctx):
        embed = discord.Embed(
            colour  = 0x00FF10
        )
        embed.set_author(name="Help > Greentint", icon_url=f"https://some-random-api.ml/canvas/green?avatar={self.client.user.avatar_url_as(format='png', size=4096)}")
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`greentint`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek warna hijau ke foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang foto profilnya mau kamu taruh efek ini.', inline=False)
        embed.add_field(name='Contoh:', value='`r!greentint @FebrieWhite#0233`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bluetint(self, ctx):
        embed = discord.Embed(
            colour  = 0x0000E4
        )
        embed.set_author(name="Help > Greentint", icon_url=f"https://some-random-api.ml/canvas/blue?avatar={self.client.user.avatar_url_as(format='png', size=4096)}")
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`bluetint`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek warna biru ke foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian mention orang yang foto profilnya mau kamu taruh efek ini.', inline=False)
        embed.add_field(name='Contoh:', value='`r!bluetint @FebrieWhite#0233`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["kucing", "kuing", "meong", "koeching"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cat(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Cat", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`cat`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`kucing, kuing, meong, koeching`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto-foto kucing secara acak.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!cat`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["anjing", "ajg", "anjink", "anjyng", "anjng", "ajng", "anjg", "doge", "doggo"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Dog", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`dog`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`anjing, ajg, anjink, anjyng, anjng, ajng, anjg, doge, doggo`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto-foto anjing secara acak.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!dog`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def panda(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Panda", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`panda`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto-foto panda secara acak.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!panda`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pikachu(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Pikachu", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`pikachu`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan GIF-GIF Pikachu secara acak.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!pikachu`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["coffee"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kopi(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Kopi", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`kopi`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`coffee`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto-foto kopi secara acak.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!kopi`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["ytcmt", "cmtyt"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtubecomment(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Youtubecomment", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`youtubecomment`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`ytcmt, cmtyt`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Membuat foto komentar YouTube palsu.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya kemudian tulis isi komentar nya.', inline=False)
        embed.add_field(name='Contoh:', value='`r!ytcmt ini adalah komentar`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["bebek"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def duck(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Duck", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`duck`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`bebek`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan gambar-gambar bebek secara acak.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!bebek`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["pistol"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gun(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Gun", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`gun`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`pistol`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan overlay pistol pada foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!gun @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lgbt(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > LGBT", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`lgbt`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan overlay bendera LGBT pada foto profil seorang user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!lbgt @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["pegang"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def grab(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Grab", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`grab`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`pegang`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan overlay tangan pada foto profil seorang user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!grab @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def truth(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Truth", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`truth`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan teks pada sebuah tempalate meme.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian masukkan teksnya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!truth ur mom gay`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def simp(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Simp", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`simp`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan overlay cap SIMP pada foto profil seorang user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!simp @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def glitch(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Glitch", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`glitch`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek glitch pada foto profil seorang user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!glitch @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hearts(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Hearts", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`hearts`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan overlay love2 pada foto profil seorang user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!hearts @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["spgbtcard"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def spongebobtimecard(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > SpongebobTimecard", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`spongebobtimecard`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`spgbtcard`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan teks pada gambar timecard kartun SpongeBob.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian masukkan teksnya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!spgbtcard 50 abad kemudian`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["htlrnews"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hitlernews(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > HitlerNews", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`hitlernews`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`htlrnews`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seseorang pada template berita di kartun Simpsons.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan pada template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!htlrnews @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def like(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Like", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`like`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seseorang pada sebuah template meme.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan pada template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!like @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dislike(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > HitlerNews", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`dislike`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seseorang pada sebuah template meme.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan pada template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!dislike @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rip(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Rip", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`rip`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Meninggoy :v', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan pada template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!rip @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["jokeovh"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def jokeoverhead(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > JokeOverHead", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`jokeoverhead`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`jokeovh`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seseorang pada sebuah template meme.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan pada template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!jokeovh @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["penjara"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def jail(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Jail", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`jail`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`penjara`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seseorang pada sebuah overlay jeruji besi.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan pada efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!jail @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["beautiful", "cantik", "indah"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def beauty(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Beauty", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`beauty`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`beautiful, cantik, indah`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seseorang pada sebuah template meme.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan pada template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!beauty @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["komunis"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def communist(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Communist", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`communist`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`komunis`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seseorang pada sebuah overlay palu arit.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan pada overlay ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!komunis @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def triggered(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Communist", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`triggered`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seseorang pada sebuah template *triggered*.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut user yang mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!triggered @Abin#4405`', inline=False)
        await ctx.send(embed=embed)   
    @h.command(aliases=["cmm"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def changemymind(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > ChangeMyMind", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`changemymind`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`cmm`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seseorang pada sebuah template *change my mind*.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian masukkan teks yang mau kamu masukkan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!cmm berak jongkok lebih naise daripada berak duduk.`', inline=False)
        await ctx.send(embed=embed) 
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clyde(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Clyde", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`clyde`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan template bot Clyde.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian masukkan teks yang mau kamu masukkan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!clyde emot ini gabisa lu pake karena haram :v.`', inline=False)
        await ctx.send(embed=embed) 
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def trash(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Trash", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`trash`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seorang user ke sebuah template meme tempat sampah.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu masukkan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!trash @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def respect(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Respect", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`respect`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seorang user ke sebuah template *respect* di game COD.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu masukkan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!respect @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["jijik"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def disgusting(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Disgusting", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`disgusting`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`jijik`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seorang user ke sebuah template meme "jijik".', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu masukkan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!jijik @Abin#4405`', inline=False)
        await ctx.send(embed=embed)      
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ferbtv(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > FerbTV", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`ferbtv`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seorang user ke sebuah template meme televisi.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu masukkan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!ferbtv @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def graph(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Graph", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`graph`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seorang user ke sebuah template meme.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu masukkan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!graph @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["primitif", "primitive"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def jadul(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Jadul", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`jadul`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`primitif, primitive`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek jadul pada foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!jadul @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["minecraftdisconnected", "mcdisconnect", "mcdc"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def disconnected(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Disconnected", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`disconnected`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Alias:', value='minecraftdisconnected, mcdisconnect, mcdc')
        embed.add_field(name='Deskripsi:', value='Menambahkan teks pada template layar *disconnect* di game Minecraft.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian masukkan teks nya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!mcdc karena elu noob :v`', inline=False)
        await ctx.send(embed=embed) 
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def chapta(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Chapta", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`chapta`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengubah teks menjadi kode chapta.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian masukkan teks yang mau kamu ubah jadi kode chapta.", inline=False)
        embed.add_field(name='Contoh:', value='`r!chapta slimcx`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["bakar"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def burn(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Burn", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`burn`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`bakar`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan foto profil seseorang pada template Spongbob yang hendak membakaar sebuah kertas.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu pakaikan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!burn @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def swirl(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Swirl", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`swirl`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek putar pada foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!swirl @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def implode(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Implode", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`implode`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek "masuk ke dalam" pada foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!implode @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["distort"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wave(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Wave", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`wave`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`distort`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek gelombang pada foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!wave @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["burik"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pixelate(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Pixelate", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`pixelate`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`burik`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menambahkan efek burik pada foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention/sebut orang yang foto profilnya mau kamu pakaikan efek ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!pixelate @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["rubah"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fox(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Fox", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`fox`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`rubah`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan gambar-gambar rubah secara acak..', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!fox`', inline=False)
        await ctx.send(embed=embed) 
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def trumppost(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Trumppost", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`trumppost`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan postingan Trump dengan teks sesuai masukan user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian masukkan teks nya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!trumppost this is a text`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["mcdone"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def minecraftcompleted(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > MinecraftCompleted", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`minecraftcompleted`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`mcdone`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan potret Challenge Done dari game Minecraft dengan konteks berdasarkan isi teks user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian masukkan teks nya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!mcdone Kamu mendapatkan Rp.4000 :v`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["emergency", "emergencymeet", "emergencym"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def emergencymeeting(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > EmergencyMeeting", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`emergencymeeting`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`emergency, emergencymeet, emergencym`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan template Emergency Meeting dari game Among Us dengan konteks sesuai dengan masukan user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian masukkan teks nya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!emergency ketika kamu ngekill tapi ternyata terdengar sama temanmu`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["1sttime"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def firsttime(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > FirstTime", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`firsttime`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`1sttime`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan template First Time dengan foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian sebut orang yang foto profilnya mau kamu pakaikan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!firsttime @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command(aliases=["iamspeed"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def imspeed(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > ImSpeed", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`imspeed`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`iamspeed`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan template I\'m Speed dari film Cars.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian sebut orang yang foto profilnya mau kamu pakaikan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!imspeed @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def heaven(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Heaven", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`heaven`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan template surga dengan foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian sebut orang yang foto profilnya mau kamu pakaikan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!heaven @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stonks(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Stonks", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`stonks`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan template Meme Man Stonks dengan foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian sebut orang yang foto profilnya mau kamu pakaikan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!stonks @Abin#4405`', inline=False)
        await ctx.send(embed=embed) 
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def notstonks(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > NotStonks", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`stonks`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan template Meme Man Not Stonks dengan foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian sebut orang yang foto profilnya mau kamu pakaikan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!notstonks @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tableflip(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > TableFlip", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`tableflip`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan template stickman sedang melempar meja dengan foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian sebut orang yang foto profilnya mau kamu pakaikan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!tableflip @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wolverine(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Wolverine", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`wolverine`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan template sebuah meme dengan foto profil seseorang.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian sebut orang yang foto profilnya mau kamu pakaikan di template ini.", inline=False)
        embed.add_field(name='Contoh:', value='`r!wolverine @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def neko(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Neko", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`neko`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto-foto gadis kucing Anime secara random.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!neko`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatars(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Avatars", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`avatars`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto-foto profil Anime secara random.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!avatars`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def trap(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Trap", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`trap`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto-foto Trap secara acak.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!trap`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["wallpaper"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wallpapers(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Wallpapers", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`wallpapers`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`wallpaper`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan Wallpaper-Wallpaper Anime secara random.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!wallapeprs`', inline=False)
        await ctx.send(embed=embed)











    @h.command(aliases=["avt", "pfp", "pp"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Avatar", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`avatar`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`avt, pfp, pp`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto profil seorang user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian mention (bisa juga tulis ID, bisa juga nama) orang yang mau kamu lihat foto profilnya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!pp @Hikari 光#7981`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["infoserver"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Serverinfo", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`serverinfo`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`infoserver`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan informasi server.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak membutuhkan argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!serverinfo`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servericon(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Servericon", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`servericon`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto server.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak membutuhkan argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!servericon`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Userinfo", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`userinfo`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan informasi seorang user.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian sebutkan orang yang info akunnya ingin kamu lihat.", inline=False)
        embed.add_field(name='Contoh:', value='`r!userinfo @Abin#4405`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def roleinfo(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Roleinfo", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`roleinfo`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan informasi dari sebuah role.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian sebutkan role yang info akunnya ingin kamu lihat.", inline=False)
        embed.add_field(name='Contoh:', value='`r!roleinfo @Owner`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["moji", "emj"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def emoji(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Emoji", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`emoji`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`moji, emj`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan informasi dari sebuah emoji.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian sebutkan emoji yang info akunnya ingin kamu lihat.", inline=False)
        embed.add_field(name='Contoh:', value='`r!emoji` <:k_ketawa:818894027318755370>', inline=False)
        await ctx.send(embed=embed)                         
    @h.command(aliases=["binarytxt"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def binertxt(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Binertxt", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`binertxt`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`binarytxt`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengonversi angka biner menjadi tulisan biasa.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis angka biner yang mau konversi menjadi tulisan biasa.", inline=False)
        embed.add_field(name='Contoh:', value='`r!binertxt 011010000110000101101001`', inline=False)
        await ctx.send(embed=embed)  
    @h.command(aliases=["binary"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def biner(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Biner", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`biner`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`binary`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengonversi tulisan biasa menjadi angka biner.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis teks yang mau kamu konversi menjadi angka biner.", inline=False)
        embed.add_field(name='Contoh:', value='`r!biner halo`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def afk(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > AFK", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`afk`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengatur status AFK.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis alasan kenapa kamu AFK.", inline=False)
        embed.add_field(name='Contoh:', value='`r!afk makan`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["hex", "colour", "warna"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def color(self, ctx):
        embed = discord.Embed(
            colour  = discord.Colour.random()
        )
        embed.set_author(name="Help > Color", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`color`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`hex, colour, warna`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan informasi warna.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis kode HEX dari warna yang ingin kamu ketahui infonya **tanpa tanda #**.", inline=False)
        embed.add_field(name='Contoh:', value='`r!color ffffff`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kbbi(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > KBBI", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`kbbi`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="7 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan arti kata sesuai yang ada di KBBI.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis kata yang mau kamu lihat artinya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!kbbi kursi`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["covid-19", "covid19", "coronavirus", "korona", "corona"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def covid(self, ctx):
        embed = discord.Embed(
            colour  = discord.Colour.red()
        )
        embed.set_author(name="Help > Covid", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`covid`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`covid-19, covid19, coronavirus, korona, corona`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan statistik COVID-19 di Indonesia (jika tidak ditambahkan argumen), dan di negara-negara tertentu.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian ketik negara yang statistik COVID-19 nya mau kamu lihat. Bisa juga hanya mengetik command nya, untuk memunculkan statistik yang di Indonesia.", inline=False)
        embed.add_field(name='Contoh:', value='`r!covid` (Cukup tulis ini kalau Indonesia)\n`r!covid russia`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gempa(self, ctx):
        embed = discord.Embed(
            colour  = 0xff0000
        )
        embed.set_author(name="Help > Covid", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`gempa`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan informasi gempa yang terakhir kali terjadi di tanah air.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!gempa`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kodepos(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Kodepos", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`kodepos`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="7 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan informasi kode pos.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis nama kota/tempat yang ingin kamu ketahui kode pos nya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!kodepos gorontalo`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["tr", "tl"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def translate(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Translate", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`translate`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`tr, tl`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menerjemahkan kata/kalimat.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis kode bahasa tujuan kalian, lalu tulis kata/kalimat yang ingin kamu terjemahkan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!translate [kode bahasa tujuan] [teks]`\n`r!translate id this is a test`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def batik(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Batik", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`batik`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="10 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan informasi batik.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis nama/jenis batik yang mau kamu ketahui infonya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!batik betawi`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["yt"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtube(self, ctx):
        embed = discord.Embed(
            colour  = 0xff0000
        )
        embed.set_author(name="Help > YouTube", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`youtube`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`yt`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan informasi channel di YouTube.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis nama channel yang mau kamu ketahui infonya.", inline=False)
        embed.add_field(name='Contoh:', value='`r!yt PewDiePie`', inline=False)
        await ctx.send(embed=embed)




















    @h.command(aliases=["tentangbot", "aboutme", "aboutbot", "tentang", "info", "infobot"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def about(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > About", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`about`')
        embed.add_field(name='Kategori:', value='`Lain-Lain`')
        embed.add_field(name='Alias:', value='`tentangbot, aboutme, aboutbot, tentang, info, infobot`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan informasi & statistik bot.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!about`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["undang"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invite(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Invite", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`invite`')
        embed.add_field(name='Kategori:', value='`Lain-Lain`')
        embed.add_field(name='Alias:', value='`undang`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan link invite bot.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!invite`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["pong", "ponggo", "latensi"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Ping", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`ping`')
        embed.add_field(name='Kategori:', value='`Lain-Lain`')
        embed.add_field(name='Alias:', value='`pong, ponggo, latensi`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan ping bot.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!ping`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def uptime(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Uptime", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`uptime`')
        embed.add_field(name='Kategori:', value='`Lain-Lain`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan waktu aktif bot.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!uptime`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def upvote(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Upvote", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`upvote`')
        embed.add_field(name='Kategori:', value='`Lain-Lain`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="Tidak ada", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan link Vote bot ini di [top.gg](https://top.gg).', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!upvote`', inline=False)
        await ctx.send(embed=embed)


    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #============================================[ help allcommands ]==============================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================
    #==============================================================================================================    
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def allcommands(self, ctx):
        embed = discord.Embed(
        description = 'Prefiks: `r!` dan `robin `',
        colour = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Daftar Semua Command Bot Robin", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Requset oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='>> Moderasi', value='`kick, ban, unban, changenick, clear, newrole, giverole, removerole, deleterole`', inline=False)
        embed.add_field(name='>> Fun', value='`titit, lovecalc, _8ball, keqing, tes, geh, kaori, tabok, bonk, saygoodbye, say, sayy, sayem, rate, poll, acakangka, acakhuruf, face`', inline=False)
        embed.add_field(name='>> Interaksi', value='`blush, kiss, lick, nom, pout, cry, poke, punch, slap, sleep, smug, tickle, hug, pat, wink`', inline=False)
        embed.add_field(name='>> Gambar', value='`cat, dog, bird, panda, pikachu, kopi, youtubecomment, duck, wasted, hitamputih, invert, bright, threshold, sepia, redtint, greentint, bluetint, gun, lgbt, grab, truth, simp, glitch, hearts, spongebobtimecard, hitlernews, like, dislike, rip, jokeoverhead, jail, beauty, communist, triggered, changemymind, clyde, trash, respect, disgusting, ferbtv, graph, jadul, disconnected, chapta, burn, swirl, implode, wave, pixelate, fox, trumppost, minecraftcompleted, emergencymeeting, firsttime, imspeed, heaven, stonks, notstonks, tableflip, wolverine, neko, avatars, trap, wallpapers`', inline=False)
        embed.add_field(name=">> Utilitas", value="`avatar, serverinfo, servericon, userinfo, roleinfo, emoji, biner, binertxt, afk, color, kbbi, corona, gempa, kodepos, translate, batik, youtube`", inline=False)
        embed.add_field(name='>> Command Rahasia', value='||`???`||', inline=False)
        embed.add_field(name='>> Lain-Lain:', value='`about, invite, ping, uptime, upvote`', inline=False)
        await ctx.send(embed = embed)
            

def setup(client):
    client.add_cog(Help(client))
