import discord, asyncio
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ping.py siap")
    
    @commands.command(aliases=["pong", "ponggo", "latensi"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        ping = round(self.client.latency*1000)

        if ping <= 299:
            embed = discord.Embed(
                color = discord.Color.default()
            )
            embed.set_author(name="Menghitung Ping...", icon_url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Youtube_loading_symbol_1_(wobbly).gif")
            pesan_awal = await ctx.send(embed=embed)

            embed = discord.Embed(
                title = f":signal_strength: Ping Bot: `{ping}`ms",
                color = 0x22ff00
            )
            await asyncio.sleep(1.5)
            await pesan_awal.edit(embed=embed)
        elif ping >= 300 and ping < 399:
            embed = discord.Embed(
                color = discord.Color.default()
            )
            embed.set_author(name="Menghitung Ping...", icon_url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Youtube_loading_symbol_1_(wobbly).gif")
            pesan_avval = await ctx.send(embed=embed)

            embed = discord.Embed(
                title = f":signal_strength: Ping Bot: `{ping}`ms",
                color = 0xffff00
            )
            await asyncio.sleep(1.5)
            await pesan_avval.edit(embed=embed)
        elif ping >= 400:
            embed = discord.Embed(
                color = discord.Color.default()
            )
            embed.set_author(name="Menghitung Ping...", icon_url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Youtube_loading_symbol_1_(wobbly).gif")
            pesan_aual = await ctx.send(embed=embed)

            embed = discord.Embed(
                title = f":signal_strength: Ping Bot: `{ping}`ms",
                color = 0xff0000
            )
            await asyncio.sleep(1.5)
            await pesan_aual.edit(embed=embed)

def setup(client):
    client.add_cog(Ping(client))