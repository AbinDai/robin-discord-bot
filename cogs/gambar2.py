import discord, requests, os
from discord.ext import commands

class TesGambar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("gambar2.py siap")

    #satu paket ini berisi 16 command awokawok
    @commands.command(aliases=["pistol"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gun(self, ctx, member: discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/gun?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("gun.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("gun.png"))

            os.remove("gun.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lgbt(self, ctx, member: discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/rainbow?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("lgbt.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("lgbt.png"))

            os.remove("lgbt.png")

    @commands.command(aliases=["pegang"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def grab(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/grab?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("grab.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("grab.png"))

            os.remove("grab.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def truth(self, ctx, *teks):
        if not teks:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan teks!\nContoh: `r!truth never gonna give you up`")
        else:
            async with ctx.typing():
                txt = "%20".join(teks)
                response = requests.get(f"https://api.devs-hub.xyz/truth?text={txt}")

                file = open("truth.png", "wb")
                file.write(response.content)
                file.close()

                await ctx.send(file=discord.File("truth.png"))

                os.remove("truth.png")
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def simp(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/simp?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("simp.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("simp.png"))

            os.remove("simp.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def glitch(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/glitch?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("glitch.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("glitch.png"))

            os.remove("glitch.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hearts(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/hearts?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("hearts.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("hearts.png"))

            os.remove("hearts.png")

    @commands.command(aliases=["spgbtcard"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def spongebobtimecard(self, ctx, *teks):
        if not teks:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan teks!\nContoh: `r!spgbtcard 2 abad kemudian`")
        else:
            async with ctx.typing():
                text = "%20".join(teks)
                response = requests.get(f"https://api.devs-hub.xyz/spongebob-timecard?text={text}")

                file = open("spongebob-timecard.png", "wb")
                file.write(response.content)
                file.close()

                await ctx.send(file=discord.File("spongebob-timecard.png"))

                os.remove("spongebob-timecard.png")

    @commands.command(aliases=["htlrnews"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hitlernews(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/hitler?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("hitler-news.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send('"Lebih buruk dari Hitler!"', file=discord.File("hitler-news.png"))

            os.remove("hitler-news.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def like(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/like?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("everyone-liked-that.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send('"Semua orang menyukainya."', file=discord.File("everyone-liked-that.png"))

            os.remove("everyone-liked-that.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dislike(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/dislike?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("everyone-disliked-that.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send('"Semua orang tidak menyukainya."', file=discord.File("everyone-disliked-that.png"))

            os.remove("everyone-disliked-that.png")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rip(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/rip?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("rip.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("rip.png"))

            os.remove("rip.png")

    @commands.command(aliases=["jokeovh"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def jokeoverhead(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/joke-over-head?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("joke-over-head.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("joke-over-head.png"))

            os.remove("joke-over-head.png")

    @commands.command(aliases=["penjara"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def jail(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member
        
        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/jail?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("jail.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("jail.png"))

            os.remove("jail.png")

    @commands.command(aliases=["beautiful", "cantik", "indah"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def beauty(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/beautiful?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("beautiful.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send("Oh, ini... ini sangat indah.", file=discord.File("beautiful.png"))

            os.remove("beautiful.png")

    @commands.command(aliases=["komunis"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def communist(self, ctx, member:discord.Member):
        member = ctx.author if not member else member

        async with ctx.typing():
            response = requests.get(f"https://api.devs-hub.xyz/communist?image={member.avatar_url_as(format='png', size=4096)}")

            file = open("communist.png", "wb")
            file.write(response.content)
            file.close()

            await ctx.send(file=discord.File("communist.png"))

            os.remove("communist.png")

def setup(client):
    client.add_cog(TesGambar(client))