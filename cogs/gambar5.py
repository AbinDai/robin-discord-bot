import discord, requests, os
from discord.ext import commands

class Gambar5(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("gambar5.py siap")

    #skrip ini berisi 10 command, yaitu trumppost, minecraftcompleted, emergencymeeting, firsttime, imspeed, heaven, stonks, notstonks, tableflip, wolverine
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def trumppost(self, ctx, *text):
        if not text:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan teks!\nContoh: `r!trumppost make america great again`")
        else:
            async with ctx.typing():
                teks = "%20".join(text)

                response = requests.get(f"https://api.no-api-key.com/api/v2/trump?message={teks}")
                file = open("trump-on-twitter.png", "wb")
                file.write(response.content)
                file.close()

                await ctx.send(file=discord.File("trump-on-twitter.png"))

                os.remove("trump-on-twitter.png")

    @commands.command(aliases=["mcdone"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def minecraftcompleted(self, ctx, *text):
        if not text:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan teks!\nContoh: `r!mcdone you have 1 year of luck!`")
        else:
            async with ctx.typing():
                teks = "%20".join(text)

                response = requests.get(f"https://api.cool-img-api.ml/challenge?text={teks}")
                file = open("minecraft-challenge-done.png", "wb")
                file.write(response.content)
                file.close()

                await ctx.send(file=discord.File("minecraft-challenge-done.png"))

                os.remove("minecraft-challenge-done.png")

    @commands.command(aliases=["emergency", "emergencymeet", "emergencym"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def emergencymeeting(self, ctx, *text):
        if not text:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan teks!\nContoh: `r!emergency kamu ngekill tapi lupa matiin mic!`")
        else:
            async with ctx.typing():
                teks = "%20".join(text)

                response = requests.get(f"https://vacefron.nl/api/emergencymeeting?text={teks}")
                file = open("emergency-meeting.png", "wb")
                file.write(response.content)
                file.close()

                await ctx.send(file=discord.File("emergency-meeting.png"))

                os.remove("emergency-meeting.png")

    @commands.command(aliases=["1sttime"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def firsttime(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://vacefron.nl/api/firsttime?user={member.avatar_url_as(format='png', size=4096)}")
            file = open("first-time.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send('"Pertama kali?"', file=discord.File("first-time.png"))

            os.remove("first-time.png")

    @commands.command(aliases=["iamspeed"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def imspeed(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://vacefron.nl/api/iamspeed?user={member.avatar_url_as(format='png', size=4096)}")
            file = open("i-am-speed.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("i-am-speed.png"))

            os.remove("i-am-speed.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def heaven(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://vacefron.nl/api/heaven?user={member.avatar_url_as(format='png', size=4096)}")
            file = open("heaven.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("heaven.png"))

            os.remove("heaven.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stonks(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://vacefron.nl/api/stonks?user={member.avatar_url_as(format='png', size=4096)}&notstonks=False")
            file = open("stonks.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("stonks.png"))

            os.remove("stonks.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def notstonks(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://vacefron.nl/api/stonks?user={member.avatar_url_as(format='png', size=4096)}&notstonks=True")
            file = open("not-stonks.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("not-stonks.png"))

            os.remove("not-stonks.png")

    @commands.command(aliases=["lemparmeja", "tbflip"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tableflip(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://vacefron.nl/api/tableflip?user={member.avatar_url_as(format='png', size=4096)}")
            file = open("table-flip.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("table-flip.png"))

            os.remove("table-flip.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wolverine(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://vacefron.nl/api/wolverine?user={member.avatar_url_as(format='png', size=4096)}")
            file = open("wolverine.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("wolverine.png"))

            os.remove("wolverine.png")

def setup(client):
    client.add_cog(Gambar5(client))