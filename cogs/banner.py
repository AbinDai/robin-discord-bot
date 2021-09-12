import discord
from discord.ext import commands

class Banner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def banner(self, ctx, *, member:discord.Member):
        member = ctx.author if not member else member

        try:
            user = await self.client.fetch_user(id)
            req = await self.client.http.request(discord.http.Route("GET", f"/users/{user.id}"))
            banner_id = req["banner"]
            if banner_id:
                banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=4096"

            await ctx.send(banner_url)
        except:
            print("command `banner` gagal dieksekusi")

def setup(client):
    client.add_cog(Banner(client))
