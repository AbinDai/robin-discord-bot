import discord, requests
from discord.ext import commands

class Anime(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["nimek"])
    async def anime(self, ctx, *pencarian):
        if not pencarian:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan judul Anime yang mau kamu cari!\nContoh: `r!anime One Piece`")
        else:
            cari = "%20".join(pencarian)
            api = requests.get(f"https://api.jikan.moe/v3/search/anime?q={cari}&limit=1").json()

            try:
                url = api["results"][0]["url"]
                gambar = api["results"][0]["image_url"]
                judul = api["results"][0]["title"]
                status_penayangan = api["results"][0]["airing"]
                sinopsis = api["results"][0]["synopsis"]
                tipe = api["results"][0]["type"]
                jumlah_episode = api["results"][0]["episodes"]
                skor_penilaian = api["results"][0]["score"]
                tanggal_mulai_menguadara = api["results"][0]["start_date"]
                tanggal_tamat = api["results"][0]["end_date"]
                rating_usia = api["results"][0]["rated"]

                embed = discord.Embed(
                    title = judul,
                    url = url,
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed.set_thumbnail(url=gambar)
                embed.set_footer(text=f"Diberdayakan oleh MyAnimeList  |   Di-Request oleh {ctx.author.name}",icon_url=ctx.author.avatar_url)
                embed.add_field(name="Sinopsis",value=sinopsis,inline=False)
                embed.add_field(name="Tipe",value=tipe)
                embed.add_field(name="Masih Mengudara?",value=status_penayangan)
                embed.add_field(name="Jumlah Episode",value=jumlah_episode)
                embed.add_field(name="Skor Penilaian",value=skor_penilaian)
                embed.add_field(name="Rating Usia",value=rating_usia)
                embed.add_field(name="Mulai Tayang",value=tanggal_mulai_menguadara,inline=False)
                embed.add_field(name="Selesai Tanggal",value=tanggal_tamat,inline=True)
                await ctx.send(embed=embed)
            except:
                await ctx.reply("❌ Anime tidak ditemukan.")

def setup(client):
    client.add_cog(Anime(client))