import requests
from discord.ext import commands

class Fun2(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("fun2.py siap")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def face(self, ctx):
        api = requests.get("https://api.toxy.ga/api/face").json()
        hasil = api["face"]

        await ctx.send(hasil)

def setup(client):
    client.add_cog(Fun2(client))