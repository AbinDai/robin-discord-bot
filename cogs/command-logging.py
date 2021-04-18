import discord
from discord.ext import commands

class CommandsLog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command(self, ctx):
        channel = self.client.get_channel(833456801915338763)
        nama_server = ctx.guild.name
        foto_server = ctx.guild.icon_url
        TeKaPe = ctx.channel
        pelaku = ctx.author
        nama_command = ctx.command

        embed = discord.Embed(
            description = f"__{pelaku}__ mengeksekusi command `{nama_command}` di channel __#{TeKaPe}__."
        )
        embed.set_author(name="Command Dieksekusi", icon_url=pelaku.avatar_url_as(format=None, static_format='png', size=4096))
        embed.set_footer(text=f"Server: {nama_server}", icon_url=foto_server)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(CommandsLog(client))