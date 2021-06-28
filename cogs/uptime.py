import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from datetime import datetime

class Uptime(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        global waktu_mulai
        waktu_mulai = datetime.now()

    @commands.command()
    async def uptime(self, ctx:Context):
        delta_uptime = datetime.now() - waktu_mulai
        jam, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        menit, detik = divmod(remainder, 60)
        hari, jam = divmod(jam, 24)

        embed = discord.Embed(
            title = "⏲ Waktu Aktif Bot",
            description = f"{hari} hari {jam} jam {menit} menit {detik} detik.",
            color = ctx.guild.me.color
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Uptime(client))
