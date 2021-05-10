import discord, requests
from discord.ext import commands

class Gambar6(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("gambar6.py siap")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def neko(self, ctx):
        api = requests.get("https://shiro.gg/api/images/neko").json()
        gambar = api["url"]

        embed = discord.Embed(
            title = "🐱 Nekogirl",
            color = ctx.guild.get_member(805876219647361053).color
        )
        embed.set_image(url=gambar)
        embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatars(self, ctx):
        api = requests.get("https://shiro.gg/api/images/avatars").json()
        gambar = api["url"]

        embed = discord.Embed(
            title = "Avatar-Avatar Random", 
            color = ctx.guild.get_member(805876219647361053).color
        )
        embed.set_image(url=gambar)
        embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def trap(self, ctx):
        api = requests.get("https://shiro.gg/api/images/trap").json()
        gambar = api["url"]

        embed = discord.Embed(
            title = "Trap... (Cowok yang menyerupai Cewek)", 
            color = ctx.guild.get_member(805876219647361053).color
        )
        embed.set_image(url=gambar)
        embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["wallpaper"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wallpapers(self, ctx):
        api = requests.get("https://shiro.gg/api/images/wallpapers").json()
        gambar = api["url"]

        embed = discord.Embed(
            title = "Wallpaper-Wallpaper Anime Random", 
            color = ctx.guild.get_member(805876219647361053).color
        )
        embed.set_image(url=gambar)
        embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Gambar6(client)) 
