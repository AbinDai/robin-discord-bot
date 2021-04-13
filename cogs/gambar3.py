import discord, requests, os
import discord, os, requests
from discord.ext import commands

class Gambar3(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("gambar3.py siap")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def triggered(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        response = requests.get(f"https://api.toxy.ga/api/triggered?avatar={member.avatar_url_as(format='png', size=4096)}")

        async with ctx.typing():
            file = open("triggered.gif", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("triggered.gif"))

            os.remove("triggered.gif")

    @commands.command(aliases=["cmm"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def changemymind(self, ctx, *teks):
        if not teks:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak menyertakan teks!\nContoh: `r!cmm discord pc has a better audio than mobile`")
        else:
            async with ctx.typing():
                text = "%20".join(teks)
                response = requests.get(f"https://api.toxy.ga/api/changemymind?text={text}")
                file = open("change-my-mind.png", "wb")
                file.write(response.content)
                file.close()

                await ctx.send(file=discord.File("change-my-mind.png"))

                os.remove("change-my-mind.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clyde(self, ctx, *teks):
        if not teks:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak menyertakan teks!\nContoh: `r!cmm kamu tidak dapat menggunakan emoji ini karena ia tidak berasal dari server ini!`")
        else:
            async with ctx.typing():
                text = "%20".join(teks)
                response = requests.get(f"https://api.toxy.ga/api/clyde?text={text}")
                file = open("clyde.png", "wb")
                file.write(response.content)
                file.close()

                await ctx.send(file=discord.File("clyde.png"))

                os.remove("clyde.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def trash(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.toxy.ga/api/trash?avatar={member.avatar_url_as(format='png', size=4096)}")
            file = open("trash.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("trash.png"))

            os.remove("trash.png")

def setup(client):
    client.add_cog(Gambar3(client))