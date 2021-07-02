import discord, requests
from discord.ext import commands
from discord.ext.commands.context import Context

class Quote(commands.Cog): 
    def __init__(self, client): self.client = client

    @commands.group(invoke_without_command=True, aliases=["quotes"])
    async def quote(self, ctx:Context):
        embed = discord.Embed(
            title = "Quote",
            description  =  "`r!quote bucin`\n"
                            "`r!quote galau`\n"
                            "`r!quote kehidupan`\n"
                            "`r!quote random`",
            color = ctx.guild.me.color
        )
        await ctx.send(embed=embed)

    @quote.command()
    async def bucin(self, ctx:Context):
        async with ctx.typing():
            try:
                api = requests.get("https://natsu.yuu02.repl.co/api/quote/bucin").json()

                embed = discord.Embed(
                    title = "Quote Bucin",
                    description = api["data"],
                    color = ctx.guild.me.color
                )
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="Mohon maaf, terjadi error",description="Coba lagi lain kali.",color=0xff0000)
                await ctx.reply(embed=embed)

    @quote.command()
    async def galau(self, ctx:Context):
        async with ctx.typing():
            try:
                api = requests.get("https://natsu.yuu02.repl.co/api/quote/galau").json()

                embed = discord.Embed(
                    title = "Quote Galau",
                    description = api["data"],
                    color = ctx.guild.me.color
                )
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="Mohon maaf, terjadi error",description="Coba lagi lain kali.",color=0xff0000)
                await ctx.reply(embed=embed)

    @quote.command()
    async def kehidupan(self, ctx:Context):
        async with ctx.typing():
            try:
                api = requests.get("https://natsu.yuu02.repl.co/api/quote/kehidupan").json()

                embed = discord.Embed(
                    title = "Quote Kehidupan",
                    description = api["data"],
                    color = ctx.guild.me.color
                )
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="Mohon maaf, terjadi error",description="Coba lagi lain kali.",color=0xff0000)
                await ctx.reply(embed=embed)

    @quote.command()
    async def random(self, ctx:Context):
        async with ctx.typing():
            try:
                api = requests.get("https://natsu.yuu02.repl.co/api/quote/random").json()

                embed = discord.Embed(
                    title = "Quote Acak",
                    description = api["data"],
                    color = ctx.guild.me.color
                )
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="Mohon maaf, terjadi error",description="Coba lagi lain kali.",color=0xff0000)
                await ctx.reply(embed=embed)

def setup(client): client.add_cog(Quote(client))