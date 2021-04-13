import discord, os, requests
from discord.ext import commands

class Gambar4(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("gambar4.py siap")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def respect(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://useless-api.vierofernando.repl.co/respects?image={member.avatar_url}")
            file = open("respect.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send('"Tekan :regional_indicator_f: untuk memberi hormat."', file=discord.File("respect.png"))

            os.remove("respect.png")

    @commands.command(aliases=["jijik"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def disgusting(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://useless-api.vierofernando.repl.co/disgusting?image={member.avatar_url}")
            file = open("disgusting.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send('"Ini menjijikkan!"', file=discord.File("disgusting.png"))

            os.remove("disgusting.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ferbtv(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://useless-api.vierofernando.repl.co/ferbtv?image={member.avatar_url}")
            file = open("ferbtv.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("ferbtv.png"))

            os.remove("ferbtv.png")
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def graph(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://useless-api.vierofernando.repl.co/graph?image={member.avatar_url}")
            file = open("graph.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("graph.png"))

            os.remove("graph.png")

    @commands.command(aliases=["primitif", "primitive"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def jadul(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://useless-api.vierofernando.repl.co/primitive?image={member.avatar_url}")
            file = open("primitive.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("primitive.png"))

            os.remove("primitive.png")

    @commands.command(aliases=["minecraftdisconnected", "mcdisconnect", "mcdc"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def disconnected(self, ctx, *teks):
        if not teks:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan teks!\nContoh: `r!mcdc karena kamu belum pro awkawokawok`")
        else:
            async with ctx.typing():
                text = "%20".join(teks)

                response = requests.get(f"https://useless-api.vierofernando.repl.co/disconnected?text={text}")
                file = open("minecraft-disconnected.png", "wb")
                file.write(response.content)
                file.close()

                await ctx.send(file=discord.File("minecraft-disconnected.png"))

                os.remove("minecraft-disconnected.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def chapta(self, ctx, *teks):
        if not teks:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan teks!\nContoh: `r!mcdc semawdw`")
        else:
            async with ctx.typing():
                text = "%20".join(teks)

                response = requests.get(f"https://useless-api.vierofernando.repl.co/captcha?text={text}")
                file = open("chapta.png", "wb")
                file.write(response.content)
                file.close()

                await ctx.send(file=discord.File("chapta.png"))

                os.remove("chapta.png")

    @commands.command(aliases=["bakar"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def burn(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://useless-api.vierofernando.repl.co/burn?image={member.avatar_url}")
            file = open("burn.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("burn.png"))

            os.remove("burn.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def swirl(self, ctx, member:discord.Member=None, degree=None):
        member = ctx.author if not member else member
        degree = 360 if not degree else degree

        async with ctx.typing():
            response = requests.get(f"https://useless-api.vierofernando.repl.co/swirl?image={member.avatar_url_as(format='png', size=4096)}&degree={degree}")
            file = open("swirl.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("swirl.png"))

            os.remove("swirl.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def implode(self, ctx, member:discord.Member=None, intensitas=None):
        member = ctx.author if not member else member
        intensitas = 0.5 if not intensitas else intensitas

        async with ctx.typing():
            response = requests.get(f"https://useless-api.vierofernando.repl.co/implode?image={member.avatar_url_as(format='png', size=4096)}&amount={intensitas}")
            file = open("implode.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("implode.png"))

            os.remove("implode.png")

    @commands.command(aliases=["distort"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wave(self, ctx, member:discord.Member=None, intensitas=None):
        member = ctx.author if not member else member
        intensitas = 5 if not intensitas else intensitas

        async with ctx.typing():
            response = requests.get(f"https://useless-api.vierofernando.repl.co/wave?image={member.avatar_url_as(format='png', size=4096)}&amount={intensitas}")
            file = open("wave.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("wave.png"))

            os.remove("wave.png")

    @commands.command(aliases=["burik"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pixelate(self, ctx, member:discord.Member=None, intensitas=None):
        member = ctx.author if not member else member
        intensitas = 1.5 if not intensitas else intensitas

        async with ctx.typing():
            response = requests.get(f"https://useless-api.vierofernando.repl.co/pixelate?image={member.avatar_url_as(format='png', size=4096)}&amount={intensitas}")
            file = open("pixelate.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("pixelate.png"))

            os.remove("pixelate.png")

def setup(client):
    client.add_cog(Gambar4(client))