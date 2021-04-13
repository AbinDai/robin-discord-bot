import discord, os, requests
from discord.ext import commands

class Sepia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("sepia.py siap!")
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sepia(self, ctx, member: discord.Member=None):
        member = ctx.author if not member else member

        response = requests.get(f"https://some-random-api.ml/canvas/sepia?avatar={member.avatar_url_as(format='png', size=4096)}")

        file = open("sepia.png", "wb")
        file.write(response.content)
        file.close()

        await ctx.send(file=discord.File("sepia.png"))

        os.remove("sepia.png")

def setup(client):
    client.add_cog(Sepia(client))
