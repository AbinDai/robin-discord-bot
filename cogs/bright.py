import discord, requests, os
from discord.ext import commands

class Brightness(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("bright.py siap!")
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bright(self, ctx, member: discord.Member=None):
        member = ctx.author if not member else member

        response = requests.get(f"https://some-random-api.ml/canvas/brightness?avatar={member.avatar_url_as(format='png',size=4096)}")

        file = open("bright.png", "wb")
        file.write(response.content)
        file.close()

        await ctx.send(file=discord.File("bright.png"))

        os.remove("bright.png")

def setup(client):
    client.add_cog(Brightness(client))
