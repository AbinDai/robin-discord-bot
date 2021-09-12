import discord
from discord.ext import commands

class Banner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def banner(self, ctx, *, member:discord.Member):
        member = ctx.author if not member else member

        try:
            user = await self.client.fetch_user(member.id)
            await ctx.send(user.banner.url)
        except:
            print("command `banner` gagal dieksekusi")

def setup(client):
    client.add_cog(Banner(client))