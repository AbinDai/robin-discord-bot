import discord
import aiohttp
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print('kategori interaksi, siap ngebut!')

    #command hug
    @commands.command(aliases=['peluk', 'ba polo'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hug(self, ctx, *, member:discord.Member=None):
        member = ctx.author if not member else member
        async with aiohttp.ClientSession() as ses:
            async with ses.get('https://some-random-api.ml/animu/hug') as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    link = data['link']
                    embed = discord.Embed(
                        title = f'{ctx.message.author.name} memeluk {member.display_name}...',
                        colour = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_image(url=f'{link}')
                    await ctx.send(embed=embed)
                    await ses.close()
                else:
                    embed = discord.Embed(title=':x: Error saat membuat request...', colour=0xff0000)
                    await ctx.reply(embed=embed)
                    await ses.close()

    #commang pat
    @commands.command(aliases=['tepuk', 'nepuk'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pat(self, ctx, *, member:discord.Member=None):
        member = ctx.author if not member else member
        async with aiohttp.ClientSession() as ses:
            async with ses.get('https://some-random-api.ml/animu/pat') as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    link = data['link']
                    embed = discord.Embed(
                        title = f'{ctx.message.author.name} menepuk {member.display_name}...',
                        colour = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_image(url=f'{link}')
                    await ctx.send(embed=embed)
                    await ses.close()
                else:
                    embed = discord.Embed(title=':x: Error saat membuat request...', colour=0xff0000)
                    await ctx.reply(embed=embed)
                    await ses.close()

    #command wink
    @commands.command(aliases=['kedip'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wink(self, ctx):
        async with aiohttp.ClientSession() as ses:
            async with ses.get('https://some-random-api.ml/animu/wink') as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    link = data['link']
                    embed = discord.Embed(
                        title = f'{ctx.message.author.name} berkedip...',
                        colour = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_image(url=f'{link}')
                    await ctx.send(embed=embed)
                    await ses.close()
                else:
                    embed = discord.Embed(title=':x: Error saat membuat request...', colour=0xff0000)
                    await ctx.reply(embed=embed)
                    await ses.close()

def setup(client):
    client.add_cog(Fun(client))
