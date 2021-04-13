import discord, requests, os
from discord.ext import commands

class HitamPutih(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("hitamputih.py siap!")
        
    @commands.command(aliases=["htmpth", "grayscale"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hitamputih(self, ctx, member: discord.Member=None):
        member = ctx.author if not member else member
        
        response = requests.get(f"https://some-random-api.ml/canvas/greyscale?avatar={member.avatar_url_as(format='png', size=4096)}")

        file = open("hitamputih.png", "wb")
        file.write(response.content)
        file.close()

        await ctx.send(file=discord.File("hitamputih.png"))

        os.remove("hitamputih.png")

def setup(client):
    client.add_cog(HitamPutih(client))
