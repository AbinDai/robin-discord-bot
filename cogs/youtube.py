import discord, requests
from discord.ext import commands

class YouTube(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("youtube.py siap")

    @commands.command(aliases=["yt"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtube(self, ctx, *channel):
        try:
            if not channel:
                await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak menyertakan nama channel!\nContoh: `r!youtube PewDiePie`")
            else:
                cenel = "%20".join(channel)
                api = requests.get(f"https://jastinch-api.ml/yt-channel?search={cenel}").json()
                nama_channel = api["name"]
                deskripsi = api["description"]
                tanggal_dibuat = api["dateCreated"]
                logo = api["logo"]
                jumlah_subscriber = api["statistics"]["subscriberCount"]
                jumlah_viewer = api["statistics"]["viewCount"]
                jumlah_video = api["statistics"]["videoCount"]
                link_channel = api["url"]

                chenel = " ".join(channel)
                embed = discord.Embed(
                    title = f'<:YouTube:825017821200515083> Hasil Pencarian Channel "{chenel}" di YouTube',
                    color = 0xff0000
                )
                embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(url=logo)
                embed.add_field(name="Nama Channel", value=f"{nama_channel}", inline=False)
                embed.add_field(name="Deskripsi", value=deskripsi, inline=False)
                embed.add_field(name="Tanggal Dibuat", value=tanggal_dibuat, inline=False)
                embed.add_field(name="Link Channel", value=f"[Disini]({link_channel})", inline=False)
                embed.add_field(name="Jumlah Subscriber", value=jumlah_subscriber)
                embed.add_field(name="Jumlah Viewer", value=jumlah_viewer)
                embed.add_field(name="Jumlah Video", value=jumlah_video)
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title = "<:YouTube:825017821200515083> Channel Tidak Ditemukan",
                description = "Channel yang Anda cari tidak ditemukan.",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(YouTube(client))