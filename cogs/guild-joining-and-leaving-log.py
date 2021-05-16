import discord
from discord.ext import commands

class GuildLogs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, ctx):
        channel = self.client.get_channel(843437433952665641)

        embed = discord.Embed(
            description = f"Bot **{self.client.user}** diundang ke server **{ctx.name}**!",
            color = 0x22ff00
        )
        embed.set_author(name="Diundang ke Server!", icon_url=ctx.icon_url)
        embed.set_footer(text=f"Dengan ini, sekarang Robin sudah berada di {len(self.client.guilds)} server.")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, ctx):
        channel = self.client.get_channel(843437433952665641)

        embed = discord.Embed(
            description = f"Bot **{self.client.user}** dikeluarkan dari server **{ctx.name}** :'v",
            color = 0xff0000
        )
        embed.set_author(name="Dikeluarkan dari Server!", icon_url=ctx.icon_url)
        embed.set_footer(text=f"Dengan ini, sekarang Robin tinggal berada di {len(self.client.guilds)} server.")
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(GuildLogs(client))