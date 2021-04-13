import discord, requests
from discord.ext import commands

class Bebek(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("bebek.py siap")

    @commands.command(aliases=["bebek"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def duck(self, ctx):
        api = requests.get("https://random-d.uk/api/v2/random").json()
        gambar = api["url"]

        embed = discord.Embed(
            title = ":duck: Kwek Kwek",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_image(url=gambar)
        embed.set_footer(text="Diberdayakan oleh random-d.ck", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Bebek(client))
