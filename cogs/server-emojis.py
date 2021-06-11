import discord
from discord.ext import commands

class ServerEmojis(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def serveremojis(self, ctx):
        embed = discord.Embed(
            title = "Semua Emoji yang ada pada Server Ini",
            description = " ".join([str(emoji) for emoji in await ctx.guild.fetch_emojis()]),
            color = ctx.guild.me.color
        )
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ServerEmojis(client))