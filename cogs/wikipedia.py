import discord, wikipedia
from discord.ext import commands

class Wikipedia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["wiki"])
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
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title = f"❌ Tidak ditemukan hasil apapun dari __{pencarian}__",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Wikipedia(client))