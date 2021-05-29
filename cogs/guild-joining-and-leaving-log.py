import discord
from discord.ext import commands

class GuildLogs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, ctx):
        channel = self.client.get_channel(843437433952665641)

        embed = discord.Embed(
            title = "Diundang ke Server!",
            description = f"Bot **{self.client.user.mention}** diundang ke sebuah server!\nDengan ini, sekarang sudah berada di **{len(self.client.guilds)}** server!",
            color = 0x00ff00
        )
        embed.set_author(name=ctx.name, icon_url=ctx.icon_url)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, ctx):
        channel = self.client.get_channel(843437433952665641)

        embed = discord.Embed(
            title = "Dikeluarkan dari Server! '-'",
            description = f"Bot **{self.client.user.mention}** dikeluarkan dari sebuah server '-'\nDengan ini, sekarang tinggal berada di **{len(self.client.guilds)}** server :((",
            color = 0xff0000
        )
        embed.set_author(name=ctx.name, icon_url=ctx.icon_url)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(GuildLogs(client))
