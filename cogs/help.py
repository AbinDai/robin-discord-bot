#include <iostream>
import discord, DiscordUtils, random
from discord.ext import commands

def bikin_embed_cmd(nama_command:str, kategori:str, alias:str, cooldown:int, desc:str, \
cara_pakai:str, contoh:str, warna, foto_bot, requester):
    """
    Template Embed untuk command2
    """
    embed = discord.Embed(
        colour  = warna
    )
    embed.set_author(name=f"Help > {nama_command.capitalize()}", icon_url=foto_bot)
    embed.set_footer(text=f'Di-Request oleh {requester.name}', icon_url=requester.avatar_url)
    embed.add_field(name='Nama Command:', value=f'`{nama_command.lower()}`')
    embed.add_field(name='Kategori:', value=f'`{kategori.capitalize()}`')
    embed.add_field(name='Alias:', value=f'`{alias}`')
    embed.add_field(name="Cooldown", value=f"{cooldown} detik", inline=False)
    embed.add_field(name='Deskripsi:', value=desc, inline=False)
    embed.add_field(name='Cara Menggunakan:', value=cara_pakai, inline=False)
    embed.add_field(name='Contoh:', value=f'`{contoh}`', inline=False)
    return embed

def bikin_embed_kategori(kategori:str, halaman_saat_ini:int, halaman_akhir:int, isi:str, warna_embed, requester, foto_bot):
    embedaoa = discord.Embed(
        description = isi,
        color = warna_embed
    )
    embedaoa.set_author(name=f'Daftar Command dalam Kategori "{kategori}"', icon_url=foto_bot.avatar_url)
    embedaoa.set_footer(text=f"Halaman {halaman_saat_ini}/{halaman_akhir} • Di-Request oleh {requester.display_name}", icon_url=requester.avatar_url)
    return embedaoa

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
    @commands.group(aliases=["help"], invoke_without_command=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def h(self, ctx):
        embed = discord.Embed(
            title = f"Daftar Command {self.client.user.name}",
            description = 'Prefiks: `r!` dan `robin `\n'
                          'Gunakan `r!help [nama command]` untuk melihat detail command.\n'
                          'Gunakan `r!help [nama kategori]` untuk melihat daftar command yang berada di kategori tersebut.\n'
                          'Jika menemukan bug atau ingin memberikan masukan/saran, laporkan degan command `r!saran [isi masukan/saran/laporan]`.\n'
                          'Atau [gabung di serverku](https://discord.gg/rZqsvrMdwR) untuk diskusi langsung :v\n'
                          '[Vote bot ini di top.gg](https://top.gg/bot/805876219647361053/vote/) kalau kamu suka dengan fitur-fiturnya :)',
            colour = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_thumbnail(url=self.client.user.avatar_url_as(format="png",size=4096))
        embed.set_footer(text=f'Di-Requset oleh {ctx.author.name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name=':hammer: Moderasi', value='`kick, ban, unban, changenick, clear, newrole, giverole, removerole, deleterole, slowmode, createchannel, deletetextchannel, deletevoicechannel, renametextchannel, renamevoicechannel, editchanneltopic`', inline=False)
        embed.add_field(name=':grin: Fun', value='`titit, lovecalc, _8ball, keqing, tes, geh, kaori, tabok, bonk, saygoodbye, say, sayy, sayem, rate, poll, acakangka, acakhuruf, face, kancuttext, wangytext`', inline=False)
        embed.add_field(name=":video_game: Minigame", value="`tebakangka, tebakkarakter, tebaksurahjuz30`", inline=False)
        embed.add_field(name=":musical_note: Musik", value="`join, leave, play, search, pause, resume, skip, remove, clearqueue, queue, nowplaying, volume, lyrics`", inline=False)
        embed.add_field(name=':speaking_head: Interaksi', value='`blush, kiss, lick, nom, pout, cry, poke, punch, slap, sleep, smug, tickle, hug, pat, wink`', inline=False)
        embed.add_field(name=':frame_photo: Gambar', value='`cat, dog, bird, panda, pikachu, kopi, youtubecomment, duck, wasted, hitamputih, invert, bright, threshold, sepia, redtint, greentint, bluetint, gun, lgbt, grab, truth, simp, glitch, hearts, spongebobtimecard, hitlernews, like, dislike, rip, jokeoverhead, jail, beauty, communist, triggered, changemymind, clyde, trash, fox, minecraftcompleted, emergencymeeting, firsttime, imspeed, heaven, stonks, notstonks, tableflip, wolverine, neko, animeavatars, animetraps, animewallpapers`', inline=False)
        embed.add_field(name=":wrench: Utilitas", value="`avatar, serverinfo, servericon, userinfo, roleinfo, emoji, biner, binertxt, afk, color, kbbi, corona, gempa, kodepos, translate, batik, youtube, youtubeplaylist, youtubechannel, youtubesearch, wikipedia, anime, kalender, snipe`", inline=False)
        embed.add_field(name=':question: Command Rahasia', value='||`???`||', inline=False)
        embed.add_field(name=':candle: Lain-Lain:', value='`about, invite, ping, vote`', inline=False)
        embed.add_field(name="⠀",value="Dibuat dengan <:Python:845156521972596757> [Python](https://www.python.org/) dan <:discordpy:849276562469945385> [discord.py](https://discordpy.readthedocs.io/en/stable/).",inline=False)
        await ctx.send(embed = embed)

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
        embed1 = bikin_embed_kategori(
            kategori="Moderasi",
            halaman_saat_ini=1,
            halaman_akhir=2,
            isi="`r!ban`: Mem-Ban seseorang.\n"
                "`r!clear`: Menghapus pesan.\n"
                "`r!kick`: Menendang keluar seorang member.\n"
                "`r!unban`: Melepas Ban seseorang.\n"
                "`r!changenick`: Mengubah nickname seorang user.\n"
                "`r!newrole`: Membuat Role baru.\n"
                "`r!deleterole`: Menghapus Role.\n"
                "`r!giverole`: Memberikan Role kepada user.\n"
                "`r!removerole`: Mencabut Role dari seorang user.\n"
                "`r!slowmode`: Mengatur mode lambat untuk sebuah text channel.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )
        
        embed2 = bikin_embed_kategori(
            kategori="Moderasi",
            halaman_saat_ini=2,
            halaman_akhir=2,
            isi="`r!createchannel`: Membuat channel baru.\n"
                "`r!deletetextchannel`: Menghapus sebuah text channel.\n"
                "`r!deletevoicechannel`: Menghapus sebuah voice channel.\n"
                "`r!renametextchannel`: Mengubah nama sebuah text channel.\n"
                "`r!renamevoicechannel`: Mengubah nama sebuah voice channel.\n"
                "`r!editchanneltopic`: Mengubah topik sebuah text channel.",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")
        embed_embed = [embed1, embed2]
        await paginator.run(embed_embed)

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fun(self, ctx):
        embed1 = bikin_embed_kategori(
            kategori="Fun",
            halaman_saat_ini=1,
            halaman_akhir=2,
            isi="`r!8ball`: Menjawab pertanyaan kamu yang bertema Ya/Tidak dengan jawaban acak.\n"
                "`r!keqing`: Menampilkan teks \"KEQING WANGY WANGY\" lengkap.\n"
                "`r!tes`: Memeberitahu bahwa tes berhasil.\n"
                "`r!geh`: Menampilkan GIF Pepe Julian Onzeima.\n"
                "`r!kaori`: Menampilkan GIF Kaori Miyazono.\n"
                "`r!tabok`: Menampilkan 2 foto orang *nabok* secara acak.\n"
                "`r!bonk`: Menampilkan foto meme doge \"bonk\"\n"
                "`r!saygoodbye`: Menampilkan GIF parodi video Rickroll\n"
                "`r!say`: Mengikuti apa yang dikatakan user (tapi dengan nama).\n"
                "`r!sayy`: Mengikuti kata user (tapi tanpa nama).",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        embed2 = bikin_embed_kategori(
            kategori="Fun",
            halaman_saat_ini=2,
            halaman_akhir=2,
            isi="`r!sayem`: Mengikuti apa kata user (tapi diisi dalam embed).\n"
                "`r!rate`: Menilai objek.\n"
                "`r!poll`: Membuat jajak pendapat.\n"
                "`r!lovecalc`: Menghitung persentase tingkat kecintaan, ||eeeaaaa :v||.\n"
                "`r!titit`: Mengukur panjang t*tit orang yang kamu mention :v (jgn dibawa serius awokawok)\n"
                "`r!acakhuruf`: Mengacak huruf dari A sampai Z dan mengirimkan hasilnya ke ruangan chat.\n"
                "`r!acakangka`: Mengacak angka sesuai *range* yang diberikan.\n"
                "`r!face`: Menampilkan emot wajah secara acak.\n"
                "`r!kancuttext`: Membuat teks kancut.\n"
                "`r!wangytext`: Membuat teks WANGY WANGY HU HU HA HA.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")

        embed_embed = [embed1, embed2]

        await paginator.run(embed_embed)

    @h.command(aliases=["minigames"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def minigame(self, ctx):
        await ctx.send(embed=bikin_embed_kategori(
            kategori="Minigame",
            halaman_saat_ini=1,
            halaman_akhir=1,
            isi="`r!tebakangka`: Permainan Tebak Angka.\n"
                "`r!tebakkarakter`: Bermain tebak karakter.\n"
                "`r!tebaksurahjuz30`: Bermain tebak Surah Al-Quran yang ada di Juz 30.",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        ))

    @h.command(aliases=["music"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def musik(self, ctx):
        embed =  bikin_embed_kategori(
            kategori="Musik",
            halaman_saat_ini=1,
            halaman_akhir=2,
            isi="`r!join`: Memasuki Voice Channel.\n"
                "`r!play`: Memainkan Audio.\n"
                "`r!search`: Mencari lagu di YouTube untuk diputar.\n"
                "`r!pause`: Menjeda Audio.\n"
                "`r!resume`: Melanjutkan playback Audio yang sedang terjeda.\n"
                "`r!skip`: Melompat ke lagu selanjutnya.\n"
                "`r!remove`: Menghapus lagu dalam antrean sesuai dengan nomor lagu yang diberikan.\n"
                "`r!clearqueue`: Menghapus seluruh lagu dalam antrean.\n"
                "`r!queue`: Menampilkan daftar antrean lagu.\n"
                "`r!nowplaying`: Menampilkan judul lagu yang sedang dimainkan.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        embed2 = bikin_embed_kategori(
            kategori="Musik",
            halaman_saat_ini=2,
            halaman_akhir=2,
            isi="`r!volume`: Mengatur volume pemutar.\n"
                "`r!leave`: Mengeluarkan bot dari Voice Channel.\n"
                "`r!lyrics`: Mencari lirik lagu.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")
        embed_embed = [embed, embed2]
        await paginator.run(embed_embed)

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def interaksi(self, ctx):
        embed1 = bikin_embed_kategori(
            kategori="Interaksi",
            halaman_saat_ini=1,
            halaman_akhir=2,
            isi="`r!hug`: Memeluk seorang user yang kamu mention.\n"
                "`r!pat`: Menepuk seorang user yang kamu mention.\n"
                "`r!wink`: Berkedip.\n"
                "`r!kiss`: Mencium seorang user yang kamu mention.\n"
                "`r!cry`: *Mengsedih*.\n"
                "`r!blush`: Malu :v\n"
                "`r!lick`: Menjilat.\n"
                '`r!nom`: Menggigit.\n'
                "`r!pout`: Ngambek.\n"
                "`r!poke`: Colek pipi.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )
        
        embed2 = bikin_embed_kategori(
            kategori="Interaksi",
            halaman_saat_ini=2,
            halaman_akhir=2,
            isi="`r!punch`: Tinju orang.\n"
                "`r!slap`: Nampar.\n"
                "`r!sleep`: Tidur.\n"
                "`r!smug`: Nyombong.\n"
                "`r!tickle`: Nggelitik.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")

        embed_embed = [embed1, embed2]

        await paginator.run(embed_embed)
        

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gambar(self, ctx):
        embed1 = bikin_embed_kategori(
            kategori="Gambar",
            halaman_saat_ini=1,
            halaman_akhir=6,
            isi="`r!cat`: Menampilkan foto-foto kucing secara acak.\n"
                "`r!dog`: Menampilkan foto-foto anjing secara acak.\n"
                "`r!bird`: Menampilkan foto-foto burung secara acak.\n"
                "`r!panda`: Menampilkan foto-foto Panda secara acak.\n"
                "`r!pikachu`: Menampilkan GIF-GIF Pikachu secara acak.\n"
                "`r!kopi`: Menampilkan foto-foto kopi secara acak.\n"
                "`r!duck`: Menampilkan gambar-gambar bebek secara acak.\n"
                "`r!wasted`: Menampilkan *overlay* \"wasted\" ke foto profil seseorang.\n"
                "`r!hitamputih`: Membuat foto profil seseorang menjadi hitam putih.\n"
                "`r!invert`: Membalik warna foto profil seseorang.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        embed2 = bikin_embed_kategori(
            kategori="Gambar",
            halaman_saat_ini=2,
            halaman_akhir=6,
            isi="`r!bright`: Menerangkan foto profil seseorang.\n"
                "`r!threshold`: Membuat foto profil seseorang menjadi dua warna.\n"
                "`r!sepia`: Membuat foto profil seseorang menguning.\n"
                "`r!redtint`: Memerahkan foto profil seseorang.\n"
                "`r!greentint`: Menghijaukan foto profil seseorang.\n"
                "`r!bluetint`: Membirukan foto profil seseorang.\n"
                "`r!gun`: Menambahkan overlay pistol ke foto profil seseorang.\n"
                "`r!lgbt`: Menambahkan efek bendera LGBT pada foto profil seseorang.\n"
                "`r!grab`: Menambahkan overlay tangan pada foto profil seseorang.\n"
                "`r!truth`: Menambahkan teks pada temmplate meme.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )
        
        embed3 = bikin_embed_kategori(
            kategori="Gambar",
            halaman_saat_ini=3,
            halaman_akhir=6,
            isi="`r!simp`: Menambahkan overlay \"SIMP\" ke foto profil seseorang.\n"
                "`r!glitch`: Menambahkan efek glitch pada foto profil seseorang.\n"
                "`r!hearts`: Menambahkan overlay hati pada foto profil seseorang.\n"
                "`r!spongebobtimecard`: Menambahkan teks pada kartu waktu serial Spongebob.\n"
                "`r!hitlernews`: Menambahkan gambar foto profil sesoerang pada sebuah template berita di kartun Simpsons.\n"
                "`r!like`: Menambahkan foto preofil sesoerand pada sebuah template.\n"
                "`r!dislike`: Menambahkan foto preofil sesoerand pada sebuah template.\n"
                "`r!rip`: Menambahkan foto profil seorang user pada template batu nisan.\n"
                "`r!jokeoverhead`: Menambahkan foto profil seorang user pada template meme.\n"
                "`r!jail`: Menambahkan efek jeruji besi pada foto profil seseorang.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        embed4 = bikin_embed_kategori(
            kategori="Gambar",
            halaman_saat_ini=4,
            halaman_akhir=6,
            isi="`r!beauty`: Menambahkan foto profil sesoerang pada sebuah template meme.\n"
                "`r!communist`: Menambahkan overlay palu arit ke foto profil seorang user.\n"
                "`r!youtubecomment`: Membuat foto komentar YouTube palsu.\n"
                '`r!triggered`: Menambahkan efek *triggered* pada foto profil seseorang.\n'
                "`r!changemymind`: Menabahkan teks pada template *change my mind*.\n"
                "`r!clyde`: Menambahkan teks pada chat Clyde.\n"
                "`r!trash`: Menambahkan foto profil seseorang pada sebuah template meme.\n"
                "`r!fox`: Menampilkan gambar-gambar rubah secara acak.\n"
                "`r!minecraftcompleted`: Menampilkan foto Challenge Completed dari game Minecraft.\n"
                "`r!emergencymeeting`: Menampilkan template meme Emergency Meeting dari game Among Us.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )
        
        embed5 = bikin_embed_kategori(
            kategori="Gambar",
            halaman_saat_ini=5,
            halaman_akhir=6,
            isi="`r!firsttime`: Menampilkan template First Time.\n"
                "`r!imspeed`: Menampilkan template I'm Speed dari film Cars.\n"
                "`r!heaven`: Menampilkan template surga.\n"
                "`r!stonks`: Menampilkan template Meme Man Stonks.\n"
                "`r!notstonks`: Menampilkan template Meme Man Not Stonks.\n"
                "`r!tableflip`: Menampilkan template Stick Man yang sedang melempar meja.\n"
                "`r!wolverine`: Menampilkan template meme orang guling lagi liat foto.\n"
                "`r!neko`: Menampilkan foto-foto karakter gadis kucing Anime secara acak.\n"
                "`r!animeavatars`: Menampilkan foto-foto profil Anime secara acak.\n"
                "`r!animetraps`: Menampilkan foto-foto karakter *trap* secara acak.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        embed6 = bikin_embed_kategori(
            kategori="Gambar",
            halaman_saat_ini=6,
            halaman_akhir=6,
            isi="`r!animewallpapers`: Menampilkan wallpaper-wallpaper Anime secara acak.",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")

        embed_embed = [embed1, embed2, embed3, embed4, embed5, embed6]

        await paginator.run(embed_embed)
        

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def utilitas(self, ctx):
        embed1 = bikin_embed_kategori(
            kategori="Utilitas",
            halaman_saat_ini=1,
            halaman_akhir=3,
            isi="`r!color`: Menampilkan informasi warna.\n"
                "`r!kbbi`: Menampilkan arti kata dalam KBBI.\n"
                "`r!corona`: Menampilkan statistik virus Corona di Indonesia.\n"
                "`r!gempa`: Menampilkan statistik gempa terkini yang terjadi di Indonesia.\n"
                "`r!kodepos`: Menampilkan info kode pos.\n"
                "`r!translate`: Menerjemahkan kata/kalimat.\n"
                "`r!batik`: Menampilkan info batik.\n"
                "`r!afk`:  Mengatur status AFK.\n"
                "`r!biner`: Mengonversi tulisan biasa menjadi angka biner.\n"
                "`r!binertxt`: Mengonversi angka biner menjadi teks biasa.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        embed2 = bikin_embed_kategori(
            kategori="Utilitas",
            halaman_saat_ini=2,
            halaman_akhir=3,
            isi="`r!avatar`: Menampilkan foto profil seorang user.\n"
                "`r!serverinfo`: Menampilkan informasi server.\n"
                "`r!servericon`: Menampilkan foto server.\n"
                "`r!userinfo`: Menampilkan informasi seorang user.\n"
                "`r!roleinfo`: Menampilkan informasi Role.\n"
                "`r!emoji`: Menampilkan informasi Emoji.\n"
                "`r!youtube`: Menampilkan video YouTube sesuai dengan kata kunci yang diberikan.\n"
                "`r!youtubeplaylist`: Menampilkan playlist YouTube sesuai dengan kata kunci.\n"
                "`r!youtubechannel`: Menampilkan channel YouTube.\n"
                "`r!youtubesearch`: Menampilkan 10 daftar video sesuai dengan kata kunci pencarian.\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        embed3 = bikin_embed_kategori(
            kategori="Utilitas",
            halaman_saat_ini=3,
            halaman_akhir=3,
            isi="`r!wikipedia`: Menampilkan informasi dari Wikipedia.\n"
                "`r!anime`: Mencari dan menampilkan info Anime dari MyAnimeList.\n"
                "`r!kalender`: Menampilkan kalender.\n"
                "`r!snipe`: Menangkap pesan yang baru dihapus 5 menit yang lalu pada channel tersebut.",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        )

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction("◀", "back")
        paginator.add_reaction("▶", "next")

        embed_embed = [embed1, embed2, embed3]

        await paginator.run(embed_embed)

    @h.command(name="lain-lain")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lain_lain(self, ctx):
        await ctx.send(embed=bikin_embed_kategori(
            kategori="Utilitas",
            halaman_saat_ini=1,
            halaman_akhir=1,
            isi="`r!about`: Menampilkan info bot.\n"
                "`r!invite`: Menampilkan link invite bot.\n"
                "`r!ping`: Menampilkan latensi bot.\n"
                "`r!vote`: Menampilkan link untuk nge-Vote saya di [top.gg](https://top.gg/).\n",
            warna_embed=ctx.guild.get_member(self.client.user.id).color,
            requester=ctx.author,
            foto_bot=self.client.user
        ))

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
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="ban",
            kategori="Moderasi",
            alias="Tidak ada",
            cooldown=5,
            desc="Mem-Ban seseorang dari server.",
            cara_pakai="Tulis command nya kemudian mention orang yang mau kamu ban.",
            contoh="r!ban @Nathz#6498",
            warna=ctx.guild.get_member(self.client.user.id).color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))
    @h.command(aliases=["clr", "purge"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clear(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="clear",
            kategori="Moderasi",
            alias="clr, purge",
            cooldown=5,
            desc="Menghapus pesan sebanyak jumlah yang diberikan.",
            cara_pakai="Tulis command nya kemudian tuliskan jumlah pesan yang ingin kamu hapus.",
            contoh="r!clr 5",
            warna=ctx.guild.get_member(self.client.user.id).color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))
    @h.command(aliases=["kck", "hus", "usir", "keluarkan", "tendang"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="kick",
            kategori="Moderasi",
            alias="kck, hus, usir, keluarkan, tendang",
            cooldown=5,
            desc="Mengeluarkan seorang user dari server.",
            cara_pakai="Tulis command nya kemudian tuliskan mention orang yang mau kamu kick.",
            contoh="r!kck @Abin#4405",
            warna=ctx.guild.get_member(self.client.user.id).color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unban(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="unban",
            kategori="Moderasi",
            alias="Tidak ada",
            cooldown=5,
            desc="Melepas ban seseorang yang pernah di-ban.",
            cara_pakai="Tulis command nya kemudian tuliskan ID orang yang mau kamu unban.",
            contoh="r!unban 550953412489904129",
            warna=ctx.guild.get_member(self.client.user.id).color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))
    @h.command(aliases=["nickname", "nick", "changename"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def changenick(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="changenick",
            kategori="Moderasi",
            alias="nickname, nick, changename",
            cooldown=5,
            desc="Mengubah nickname seseorang.",
            cara_pakai="Tulis command nya, sebut orang yang nick nya mau kamu ganti, dan tuliskan nickname apa yang mau kamu berikan padanya.",
            contoh="r!changenick @Abin#4405 si abin",
            warna=ctx.guild.get_member(self.client.user.id).color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))
    @h.command(aliases=["createrole", "bikinrole", "makerole", "addrole"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def newrole(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="newrole",
            kategori="Moderasi",
            alias="createrole, bikinrole, makerole, addrole",
            cooldown=5,
            desc="Membuat Role baru.",
            cara_pakai="Tulis command nya, tulis nama role nya (apit menggunakan tanda ""), kemudian tuliskan kode HEX untuk warna role nya (opsional) (tanpa diawali dengan `#`atau `0x`).",
            contoh="r!newrole \"anak rajin\" 00ff00",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command(aliases=["hapusrole"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def deleterole(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="deleterole",
            kategori="Moderasi",
            alias="hapusrole",
            cooldown=5,
            desc="Menghapus role",
            cara_pakai="Tulis command nya kemuidian sebutkan role yang mau kamu hapus.",
            contoh="r!deleterole @anak rajin",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def giverole(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="giverole",
            kategori="Moderasi",
            alias="Tidak ada",
            cooldown=5,
            desc="Memberikan role kepada seorang user.",
            cara_pakai="Tulis command nya, sebutkan orang yang akan kalian berikan role, kemudian sebutkan role mana yang akan kamu kasih.",
            contoh="r!giverole @Abin @anak rajin",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))
          
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def removerole(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="removerole",
            kategori="Moderasi",
            alias="Tidak ada",
            cooldown=5,
            desc="Mencabut role dari seorang user.",
            cara_pakai="Tulis command nya, sebutkan orang yang akan kalian cabut role nya, kemudian sebutkan role mana yang akan kamu cabut.",
            contoh="r!removerole @Abin @anak rajin",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slowmode(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Slowmode", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`slowmode`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengatur mode lambat untuk sebuah text channel.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, sebutkan durasi detiknya, dan sebut channelnya.', inline=False)
        embed.add_field(name='Contoh:', value='`r!slowmdoe 5` (untuk channel ini)\n`r!slowmode 5 #welcome` (untuk channel tertentu)\n`r!slowmode [disable/off]` (untuk channel saat ini)\n`r!slowmode [disable/off] #bots` (untuk channel tertentu)', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["newchannel"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def createchannel(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > CreateChannel", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`createchannel`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='`newchannel`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Membuat channel baru.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, sebutkan jenis channel-nya, dan sebutkan namanya.', inline=False)
        embed.add_field(name='Contoh:', value='`r!createchannel text bots`\n`r!createchannel voice music1`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def deletetextchannel(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > DeleteTextChannel", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`deletetextchannel`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menghapus sebuah text channel.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, kemudian sebut text channel mana yang mau kamu hapus.', inline=False)
        embed.add_field(name='Contoh:', value='`r!deletetextchannel #gaming`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def deletevoicechannel(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > DeleteVoiceChannel", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`deletevoicechannel`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menghapus sebuah voice channel.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, kemudian sebut voice channel mana yang mau kamu hapus.', inline=False)
        embed.add_field(name='Contoh:', value='`r!deletevoicechannel music1`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def renametextchannel(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > RenameTextChannel", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`renametextchannel`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengganti nama sebuah text channel.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, sebut text channel mana yang mau kamu ganti nama, terus sebutkan nama barunya.', inline=False)
        embed.add_field(name='Contoh:', value='`r!renametextchannel #gaming "gaming chat"`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def renamevoicechannel(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > RenameVoicwChannel", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`renametextchannel`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengganti nama sebuah voice channel.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, sebut voice channel mana yang mau kamu ganti nama, terus sebutkan nama barunya.', inline=False)
        embed.add_field(name='Contoh:', value='`r!renamevoicechannel music1 "dengar lagu 1"`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def editchanneltopic(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > EditChannelTopic", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`editchanneltopic`')
        embed.add_field(name='Kategori:', value='`Moderasi`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Mengganti topik sebuah text channel.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command nya, sebut text channel mana yang mau kamu ganti topik, terus sebutkan topik barunya.', inline=False)
        embed.add_field(name='Contoh:', value='`r!editchanneltopic #gaming-chat "Tempat chatting seputar game."`', inline=False)
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
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poll(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Poll", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`poll`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='Tidak ada')
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
    @h.command(aliases=["kancut"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kancuttext(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > KancutText", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`kancuttext`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`kancut`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Membuat text kancut sesuai dengan nama yang dimasukkan.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command-nya kemudian tulis nama.', inline=False)
        embed.add_field(name='Contoh:', value='`r!kancut alpi`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["wangy"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wangytext(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > WangyText", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`wangytext`')
        embed.add_field(name='Kategori:', value='`Fun`')
        embed.add_field(name='Alias:', value='`wangy`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Membuat text WANGY WANGY HU HA HA AWOKAWOK :V sesuai dengan nama yang dimasukkan :v.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command-nya kemudian tulis nama.', inline=False)
        embed.add_field(name='Contoh:', value='`r!wangy keqing`', inline=False)
        await ctx.send(embed=embed)
    



















    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tebakangka(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > TebakAngka", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`tebakangka`')
        embed.add_field(name='Kategori:', value='`Minigame`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Bermain tebak angka bersama saya.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Tulis command-nya, kemudian tuliskan batas awal dan akhir yang akan dimainkan (opsional).', inline=False)
        embed.add_field(name='Contoh:', value='`r!tebakangka` (default: 1 sampai 10)\n`r!tebakangka 20 30` (bermain tebak angka dari angka 20 sampai 30)', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["akinator", "akn"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tebakkarakter(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > TebakKarakter", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`tebakkarakter`')
        embed.add_field(name='Kategori:', value='`Minigame`')
        embed.add_field(name='Alias:', value='`akinator, akn`')
        embed.add_field(name="Cooldown", value="Tidak ada", inline=False)
        embed.add_field(name='Deskripsi:', value='Bermain tebak karakter bersama saya.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini tidak butuh argumen tambahan.', inline=False)
        embed.add_field(name='Contoh:', value='`r!tebakkarakter`\n`r!tebakkarakter start` (untuk memulai permainan)', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tebaksurahjuz30(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > TebakSurahJuz30", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`tebaksurahjuz30`')
        embed.add_field(name='Kategori:', value='`Minigame`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="Tidak ada", inline=False)
        embed.add_field(name='Deskripsi:', value='Bermain tebak surah Al-Quran yang ada di Juz 30.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value='Command ini tidak butuh argumen tambahan.', inline=False)
        embed.add_field(name='Contoh:', value='`r!tebaksurahjuz30` (untuk saat ini masih juz 30 yang tersedia :\'v)', inline=False)
        await ctx.send(embed=embed)
























    @h.command(aliases=["connect","j"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def join(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
                nama_command="join",
                kategori="Musik",
                alias="connect, j",
                cooldown=0,
                desc="Memasukkan bot ke voice channel.",
                cara_pakai="Command ini tidak butuh argumen tambahan, tapi bisa juga ada argumen tambahannya, yaitu nama voice channel.",
                contoh="r!j` (untuk memasuki voice channel yang sama denganmu)\n`r!j [nama voice channel]` (memasuki voice channel sesuai dengan yang ditunjuk).]",
                warna=ctx.guild.me.color,
                foto_bot=self.client.user.avatar_url,
                requester=ctx.author
            ))

    @h.command(aliases=["p"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def play(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="play",
            kategori="Musik",
            alias="p",
            cooldown=0,
            desc="Memutar Audio.",
            cara_pakai="Tulis command-nya kemudian masukkan judul lagu atau link lagu dari YouTube yang ingin kalian putar.",
            contoh="r!p [link video youtube/judul lagu]",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def search(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="search",
            kategori="Musik",
            alias="Tidak ada",
            cooldown=0,
            desc="Mencari video di YouTube untuk diputar di voice channel.",
            cara_pakai="Tulis command-nya kemudian masukkan kata kunci pencarian.",
            contoh="r!search [kata kucnci]",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))  

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pause(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="pause",
            kategori="Musik",
            alias="Tidak ada",
            cooldown=0,
            desc="Menjeda Audio",
            cara_pakai="Command ini tidak butuh argumen tambahan.",
            contoh="r!pause",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command(aliases=["remus"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def resume(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="resume",
            kategori="Musik",
            alias="remus",
            cooldown=0,
            desc="Melanjutkan Audio yang sedang dijeda.",
            cara_pakai="Command ini tidak butuh argumen tambahan.",
            contoh="r!resume",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def skip(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="skip",
            kategori="Musik",
            alias="Tidak ada",
            cooldown=0,
            desc="Melompati ke Audio selanjutnya.",
            cara_pakai="Command ini tidak butuh argumen tambahan.",
            contoh="r!skip",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def remove(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="remove",
            kategori="Musik",
            alias="Tidak ada",
            cooldown=0,
            desc="Menghapus lagu dalam antrean sesuai nomor.",
            cara_pakai="Tulis command-nya kemudian tulis posisi lagu.",
            contoh="r!remove 7",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clearqueue(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="clearqueue",
            kategori="Musik",
            alias="Tidak ada",
            cooldown=0,
            desc="Menghapus semua lagu dalam antrean.",
            cara_pakai="Command ini tidak butuh argumen tambahan.",
            contoh="r!clearqueue",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command(aliases=["q", "ququ"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def queue(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="queue",
            kategori="Musik",
            alias="q, ququ",
            cooldown=0,
            desc="Menampilkan daftar antrean lagu.",
            cara_pakai="Command ini tidak butuh argumen tambahan.",
            contoh="r!q",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command(aliases=["now", "current", "currentsong", "playing", "np"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nowplaying(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="nowplaying",
            kategori="Musik",
            alias="now, current, currentsong, playing, np",
            cooldown=0,
            desc="Menampilkan judul lagu yang sedang diputar.",
            cara_pakai="Command ini tidak butuh argumen tambahan.",
            contoh="r!np",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command(aliases=["vol", "v"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def volume(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="volume",
            kategori="Musik",
            alias="v, vol",
            cooldown=0,
            desc="Mengatur volume Audio.",
            cara_pakai="Tulis command-nya kemudian besar/kecil volumenya.\nUntuk melihat volume saat ini, ketikkan `r!volume` saja tanpa argumen.",
            contoh="r!v\nr!v 100",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command(aliases=["dc", "disconnect"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def leave(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="leave",
            kategori="Musik",
            alias="dc, disconnect",
            cooldown=0,
            desc="Mengeluarkan bot dari voice channel.",
            cara_pakai="Command ini tidak butuh argumen tambahan.",
            contoh="r!dc",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))

    @h.command(aliases=["ly", "lirik"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lyrics(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="lyrics",
            kategori="Musik",
            alias="ly, lirik",
            cooldown=0,
            desc="Menampilkan lirik.",
            cara_pakai="Command ini tidak butuh argumen tambahan dan akan langsung menampilkan lirik lagu dari lagu yang sedang diputar. Tapi jika sedang tidak ada lagu yang diputar, maka masukkan judul lagu yang mau kamu lihat liriknya.",
            contoh="r!ly\nr!ly [judul lagu]",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))













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
    @h.command(aliases=["nekogirl", "catgirl"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def neko(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Neko", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`neko`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`nekogirl, catgirl`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto-foto gadis kucing Anime secara random.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!neko`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["ppanime", "fotoprofilanime"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def animeavatars(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > AnimeAvatars", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`animeavatars`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='`ppanime, fotoprofilanime`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto-foto profil Anime secara random.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!animeavatars`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def animetraps(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > AnimeTraps", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`animetraps`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada.')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan foto-foto Trap secara acak.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!animetraps`', inline=False)
        await ctx.send(embed=embed)
    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def animewallpapers(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > AnimeWallpapers", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`animewallpapers`')
        embed.add_field(name='Kategori:', value='`Gambar`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan Wallpaper-Wallpaper Anime secara random.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!animewallpapers`', inline=False)
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
        embed.add_field(name='Deskripsi:', value='Menampilkan video dari YouTube sesuai hasil pencarian.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis kata kunci pencarian.", inline=False)
        embed.add_field(name='Contoh:', value='`r!yt rickroll`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["ytplaylist"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtubeplaylist(self, ctx):
        embed = discord.Embed(
            colour  = 0xff0000
        )
        embed.set_author(name="Help > YouTubePlaylist", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`youtubeplaylist`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`ytplaylist`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan playlist dari YouTube sesuai hasil pencarian.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis kata kunci pencarian.", inline=False)
        embed.add_field(name='Contoh:', value='`r!ytplaylist rick astley songs`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["ytchannel"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtubechannel(self, ctx):
        embed = discord.Embed(
            colour  = 0xff0000
        )
        embed.set_author(name="Help > YouTubeChannel", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`youtubechannel`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`ytchannel`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan channel dari YouTube sesuai hasil pencarian.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis kata kunci pencarian.", inline=False)
        embed.add_field(name='Contoh:', value='`r!ytchannel PewDiePie`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["ytsearch"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtubesearch(self, ctx):
        embed = discord.Embed(
            colour  = 0xff0000
        )
        embed.set_author(name="Help > YouTubeSearch", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`youtubesearch`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`ytsearch`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan 10 daftar video dari YouTube sesuai hasil pencarian.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis kata kunci pencarian.", inline=False)
        embed.add_field(name='Contoh:', value='`r!ytsearch rickroll`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["wiki"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wikipedia(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > YouTubeSearch", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`wikipedia`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`wiki`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan artikel dari Wikipedia sesuai dengan kata kunci pencarian.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis kata kunci pencarian.", inline=False)
        embed.add_field(name='Contoh:', value='`r!wiki kota gorontalo`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["nimek"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def anime(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Anime", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`anime`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`nimek`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan info Anime dari MyAnimeList sesuai dengan kata kunci pencarian.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis kata kunci pencarian.", inline=False)
        embed.add_field(name='Contoh:', value='`r!anime One Piece`', inline=False)
        await ctx.send(embed=embed)
    @h.command(aliases=["calendar","calender"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kalender(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Kalender", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`kalender`')
        embed.add_field(name='Kategori:', value='`Utilitas`')
        embed.add_field(name='Alias:', value='`calendar, calender`')
        embed.add_field(name="Cooldown", value="5 detik", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan kalender.', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Tulis command nya kemudian tulis tahun-nya, dan tulis bulannya (opsional).", inline=False)
        embed.add_field(name='Contoh:', value='`r!kalender 2021` (kalau mau melihat 1 tahun kalender)\n`r!kalender 2021 juni` (untuk melihat 1 bulan kalender)\n`r!kalender 2021 6` (sama aja, tapi pake angka utk bulannya).', inline=False)
        await ctx.send(embed=embed)

    @h.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def snipe(self, ctx):
        await ctx.send(embed=bikin_embed_cmd(
            nama_command="snipe",
            kategori="Utilitas",
            alias="Tidak ada",
            cooldown=0,
            desc="Menangkap pesan yang baru dihapus 5 menit yang lalu.",
            cara_pakai="Command ini tidak butuh argumen tambahan.",
            contoh="r!snipe",
            warna=ctx.guild.me.color,
            foto_bot=self.client.user.avatar_url,
            requester=ctx.author
        ))




















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
    async def vote(self, ctx):
        embed = discord.Embed(
            colour  = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_author(name="Help > Upvote", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Command:', value='`vote`')
        embed.add_field(name='Kategori:', value='`Lain-Lain`')
        embed.add_field(name='Alias:', value='Tidak ada')
        embed.add_field(name="Cooldown", value="Tidak ada", inline=False)
        embed.add_field(name='Deskripsi:', value='Menampilkan link Vote bot ini di [top.gg](https://top.gg).', inline=False)
        embed.add_field(name='Cara Menggunakan:', value="Command ini tidak butuh argumen tambahan.", inline=False)
        embed.add_field(name='Contoh:', value='`r!upvote`', inline=False)
        await ctx.send(embed=embed)


    
            

def setup(client):
    client.add_cog(Help(client))
