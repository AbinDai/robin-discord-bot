import discord, os, requests
from discord.ext import commands

class BlueTint(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("bluetint.py siap!")
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bluetint(self, ctx, member: discord.Member=None):
        member = ctx.author if not member else member
        
        response = requests.get(f"https://some-random-api.ml/canvas/blue?avatar={member.avatar_url_as(format='png',size=4096)}")

        file = open("bluetint.png", "wb")
        file.write(response.content)
        file.close()

        await ctx.send(file=discord.File("bluetint.png"))

        os.remove("bluetint.png")

def setup(client):
    client.add_cog(BlueTint(client))
