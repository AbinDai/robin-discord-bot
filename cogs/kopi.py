import discord, requests
from discord.ext import commands

class Kopi(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("kopi.py siap")

    @commands.command(aliases=["coffee"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kopi(self, ctx):
        api = requests.get("https://coffee.alexflipnote.dev/random.json").json()
        gambar = api["file"]

        embed = discord.Embed(
            title = ":coffee: Kopi",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_image(url=gambar)
        embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Kopi(client))
