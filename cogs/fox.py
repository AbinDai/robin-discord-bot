import discord, requests
from discord.ext import commands

class Fox(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("fox.py siap")

    @commands.command(aliases=["rubah"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fox(self, ctx):
        api = requests.get("https://randomfox.ca/floof/").json()
        gambar = api["image"]

        embed = discord.Embed(
            title = "🦊 Rubah", 
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_image(url=gambar)
        embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fox(client))