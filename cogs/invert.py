import discord, os, requests
from discord.ext import commands

class Invert(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("kaca.py siap!")
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invert(self, ctx, member: discord.Member=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Mention orang yang ingin kamu balik warna foto profilnya!\nContoh: `r!invert @Abin#4405`")
        else:
            response = requests.get(f"https://some-random-api.ml/canvas/invert?avatar={member.avatar_url_as(format='png', size=4096)}")

            file = open("invert.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("invert.png"))

            os.remove("invert.png")

def setup(client):
    client.add_cog(Invert(client))
