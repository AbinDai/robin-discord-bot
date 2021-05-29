import discord, wikipedia
from discord.ext import commands

class Wikipedia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["wiki"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wikipedia(self, ctx, *, pencarian:str):
        try:
            wikipedia.set_lang("id")
            hasil = wikipedia.summary(pencarian)
            judul = wikipedia.page(pencarian)

            embed = discord.Embed(
                title = judul.title,
                url = f"{judul.url}",
                description = hasil,
                color = ctx.guild.get_member(self.client.user.id).color
            )
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
            embed.set_author(name="Wikipedia",icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Wikipedia_logo_v3.svg/1200px-Wikipedia_logo_v3.svg.png")
            embed.set_image(url=judul.images[0])
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title = f"❌ Tidak ditemukan hasil apapun dari __{pencarian}__",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Wikipedia(client))
