import discord, os, requests
from discord.ext import commands

class RedTint(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("redtint.py siap!")
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def redtint(self, ctx, member: discord.Member=None):
        member = ctx.author if not member else member
        
        response = requests.get(f"https://some-random-api.ml/canvas/red?avatar={member.avatar_url_as(format='png', size=4096)}")

        file = open("redtint.png", "wb")
        file.write(response.content)
        file.close()

        await ctx.send(file=discord.File("redtint.png"))

        os.remove("redtint.png")

def setup(client):
    client.add_cog(RedTint(client))
