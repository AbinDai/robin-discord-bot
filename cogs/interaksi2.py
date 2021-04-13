import discord, requests
from discord.ext import commands

class Interaksi2(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("confused.py siap")

    @commands.command(aliases=["blushed"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def blush(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        api = requests.get("https://shiro.gg/api/images/blush").json()
        gambar = api["url"]

        embed = discord.Embed(
            title = f"{member.display_name} nge-Blush...",
            color = ctx.guild.get_member(805876219647361053).color
        )
        embed.set_image(url=gambar)
        await ctx.send(embed=embed)

    @commands.command(aliases=["menangis", "nangid", "nangis", "nyedih", "menyedih", "mengsad", "mengsedih"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cry(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member

        api = requests.get("https://shiro.gg/api/images/cry").json()
        gambar = api["url"]

        embed = discord.Embed(
            title = f"{member.display_name} Nangis...",
            color = ctx.guild.get_member(805876219647361053).color
        )
        embed.set_image(url=gambar)
        await ctx.send(embed=embed)

    @commands.command(aliases=["cium"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kiss(self, ctx, member:discord.Member=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Yakin mau cium diri sendiri? Tag orang lah...\nContoh: `r!kiss @Abin#4405`")
        else:
            api = requests.get("https://shiro.gg/api/images/kiss").json()
            gambar = api["url"]

            embed = discord.Embed(
                title = f"{ctx.author.display_name} Mencium {member}",
                color = ctx.guild.get_member(805876219647361053).color
            )
            embed.set_image(url=gambar)
            await ctx.send(embed=embed)

    @commands.command(aliases=["jilat"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lick(self, ctx, member:discord.Member=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Yakin mau jilat diri sendiri? Tag orang lah...\nContoh: `r!lick @Abin#4405`")
        else:
            api = requests.get("https://shiro.gg/api/images/lick").json()
            gambar = api["url"]

            embed = discord.Embed(
                title = f"{ctx.author.display_name} Menjilat {member}",
                color = ctx.guild.get_member(805876219647361053).color
            )
            embed.set_image(url=gambar)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nom(self, ctx, member:discord.Member=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Mention seseorang untuk menggunakan command ini!\nContoh: `r!nom @Abin#4405`")
        else:
            api = requests.get("https://shiro.gg/api/images/nom").json()
            gambar = api["url"]

            embed = discord.Embed(
                title = f"{ctx.author.display_name} Memakan {member.display_name}...",
                color = ctx.guild.get_member(805876219647361053).color
            )
            embed.set_image(url=gambar)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poke(self, ctx, member:discord.Member=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Mention seseorang untuk menggunakan command ini!\nContoh: `r!poke @Abin#4405`")
        else:
            api = requests.get("https://shiro.gg/api/images/poke").json()
            gambar = api["url"]

            embed = discord.Embed(
                title = f"{ctx.author.display_name} Mencolek Pipinya {member.display_name}...",
                color = ctx.guild.get_member(805876219647361053).color
            )
            embed.set_image(url=gambar)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pout(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member
        
        api = requests.get("https://shiro.gg/api/images/pout").json()
        gambar = api["url"]

        embed = discord.Embed(
            title = f"{member.display_name} Mencibir...",
            color = ctx.guild.get_member(805876219647361053).color
        )
        embed.set_image(url=gambar)
        await ctx.send(embed=embed)

    @commands.command(aliases=["tinju"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def punch(self, ctx, member:discord.Member=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Serius mau ninju diri sndiri? Mention orang lah...\nContoh: `r!punch @Abin#4405`")
        else:
            api = requests.get("https://shiro.gg/api/images/punch").json()
            gambar = api["url"]

            embed = discord.Embed(
                title = f"{ctx.author.display_name} Meninju {member.display_name}...",
                color = ctx.guild.get_member(805876219647361053).color
            )
            embed.set_image(url=gambar)
            await ctx.send(embed=embed)

    @commands.command(aliases=["tampar"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self, ctx, member:discord.Member=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Yakin mau nampar diri sndiri? Mention orang lah...\nContoh: `r!slap @Abin#4405`")
        else:
            api = requests.get("https://shiro.gg/api/images/slap").json()
            gambar = api["url"]

            embed = discord.Embed(
                title = f"{ctx.author.display_name} Menampar {member.display_name}...",
                color = ctx.guild.get_member(805876219647361053).color
            )
            embed.set_image(url=gambar)
            await ctx.send(embed=embed)

    @commands.command(aliases=["tidur"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sleep(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member
        
        api = requests.get("https://shiro.gg/api/images/sleep").json()
        gambar = api["url"]

        embed = discord.Embed(
            title = f"{member.display_name} Tidur...",
            color = ctx.guild.get_member(805876219647361053).color
        )
        embed.set_image(url=gambar)
        await ctx.send(embed=embed)

    @commands.command(aliases=["sombong"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def smug(self, ctx, member:discord.Member=None):
        member = ctx.author if not member else member
        
        api = requests.get("https://shiro.gg/api/images/smug").json()
        gambar = api["url"]

        embed = discord.Embed(
            title = f"{member.display_name} Menyombongkan Diri...",
            color = ctx.guild.get_member(805876219647361053).color
        )
        embed.set_image(url=gambar)
        await ctx.send(embed=embed)

    @commands.command(aliases=["gelitik"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tickle(self, ctx, member:discord.Member=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Yakin mau menggelitik diri sndiri? Mention orang lah...\nContoh: `r!tickle @Abin#4405`")
        else:
            api = requests.get("https://shiro.gg/api/images/tickle").json()
            gambar = api["url"]

            embed = discord.Embed(
                title = f"{ctx.author.display_name} Menggelitik {member.display_name}...",
                color = ctx.guild.get_member(805876219647361053).color
            )
            embed.set_image(url=gambar)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Interaksi2(client))