import discord, requests
from discord.ext import commands

class Batik(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("batik.py siap")

    @commands.command(aliases=["btk"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def batik(self, ctx, *batik):
        try:
            if not batik:
                await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak menuliskan nama batik!\nContoh: `r!batik abimanyu`")
            else:
                async with ctx.typing():
                    batique = "%20".join(batik)
                    api = requests.get(f"http://batikita.herokuapp.com/index.php/batik/{batique}").json()
                    nama_batik = api["hasil"][0]["nama_batik"]
                    daerah = api["hasil"][0]["daerah_batik"]
                    makna = api["hasil"][0]["makna_batik"]
                    gambar = api["hasil"][0]["link_batik"]

                    embed = discord.Embed(
                        title = "Info Batik",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_thumbnail(url=gambar)
                    embed.set_footer(text=f"Diberdayakan oleh BatiKita", icon_url=ctx.author.avatar_url)
                    embed.add_field(name="Nama", value=nama_batik)
                    embed.add_field(name="Daerah", value=daerah)
                    embed.add_field(name="Makna", value=makna, inline=False)
                    await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title = ":x: Terjadi error...",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Batik(client))
