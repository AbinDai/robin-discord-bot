import discord, os, requests
from discord.ext import commands

class Treshold(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("threshold.py siap!")
        
    @commands.command(aliases=["thrsld", "thr"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def threshold(self, ctx, member: discord.Member=None):
        member = ctx.author if not member else member
        
        response = requests.get(f"https://some-random-api.ml/canvas/threshold?avatar={member.avatar_url_as(format='png', size=4096)}")

        file = open("threshold.png", "wb")
        file.write(response.content)
        file.close()

        await ctx.send(file=discord.File("threshold.png"))

        os.remove("threshold.png")

def setup(client):
    client.add_cog(Treshold(client))
