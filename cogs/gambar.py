import discord, aiohttp
from discord.ext import commands

class Gambar(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print("kategori gambar, siap gelud!")

    #command cat
    @commands.command(aliases=['kucing', 'kuing', 'meong', 'koeching'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as ses:
            async with ses.get('http://aws.random.cat//meow') as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    file = data['file']
                    embed = discord.Embed(
                        title = ':cat: Meong',
                        colour = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_image(url=f'{file}')
                    embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    await ses.close()
                else:
                    embed = discord.Embed(title=':x: Error saat membuat request...', colour=0xff0000)
                    await ctx.reply(embed=embed)
                    await ses.close()


    #command dog
    @commands.command(aliases=['anjing', 'ajg', 'anjink', 'anjyng', 'anjng', 'ajng', 'anjg', 'doge', 'doggo'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as ses:
            async with ses.get('https://random.dog/woof.json') as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    url = data['url']
                    embed = discord.Embed(
                        title = ':dog: Guk guk',
                        colour = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_image(url=f'{url}')
                    embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    await ses.close()
                else:
                    embed = discord.Embed(title=':x: Error saat membuat request...', colour=0xff0000)
                    await ctx.send(embed=embed)
                    await ses.close()


    #command burung
    @commands.command(aliases=['birb', 'burung'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bird(self, ctx):
        async with aiohttp.ClientSession() as ses:
            async with ses.get('https://some-random-api.ml/img/birb') as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    link = data['link']
                    embed = discord.Embed(
                        title = ':bird: Burung',
                        colour = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_image(url=f'{link}')
                    embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    await ses.close()
                else:
                    embed = discord.Embed(title=':x: Error saat membuat request...', colour=0xff0000)
                    await ctx.send(embed=embed)
                    await ses.close()


    #command panda
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as ses:
            async with ses.get('https://some-random-api.ml/img/panda') as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    link = data['link']
                    embed = discord.Embed(
                        title = ':panda_face: Panda',
                        colour = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_image(url=f'{link}')
                    embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    await ses.close()
                else:
                    embed = discord.Embed(title=':x: Error saat membuat request...', colour=0xff0000)
                    await ctx.send(embed=embed)
                    await ses.close()


    #command pikachu
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pikachu(self, ctx):
        async with aiohttp.ClientSession() as ses:
            async with ses.get('https://some-random-api.ml/img/pikachu') as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    link = data['link']
                    embed = discord.Embed(
                        title = 'Pikachu',
                        colour = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_image(url=f'{link}')
                    embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    await ses.close()
                else:
                    embed = discord.Embed(title=':x: Error saat membuat request...', colour=0xff0000)
                    await ctx.send(embed=embed)
                    await ses.close()

def setup(client):
    client.add_cog(Gambar(client))
