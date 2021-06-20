import discord, time
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.ext.commands.cooldowns import BucketType

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["pong","ponggo","latensi"])
    @commands.cooldown(1, 5, type=BucketType.user)
    async def ping(self, ctx:Context):
        ping = round(self.client.latency*1000)

        def embed():
            embed = discord.Embed(
                title = "<a:loading:854013569552220200> Menghitung Ping...",
                color = discord.Color.blurple()
            )
            return embed

        def embed2(warna:str):
            embed = discord.Embed(
                title = f"📶 Ping: `{ping}`ms",
                color = warna
            )
            return embed

        if ping < 300:
            pesan_awal = await ctx.send(embed=embed())

            time.sleep(2.5)

            await pesan_awal.edit(embed=embed2(warna=0x00ff00))
        elif ping >= 300 and ping < 400:
            pesan_awal = await ctx.send(embed=embed())

            time.sleep(2.5)

            await pesan_awal.edit(embed=embed2(warna=0xffff00))
        elif ping >= 400:
            pesan_awal = await ctx.send(embed=embed())

            time.sleep(2.5)

            await pesan_awal.edit(embed=embed2(warna=0xff0000))

def setup(client):
    client.add_cog(Ping(client))
