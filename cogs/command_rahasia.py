import discord
from discord.ext import commands

class CommandRahasia(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('kategori "command rahasia", siap gelud!')
    
    #command rickroll
    @commands.command(aliases=['???'])
    async def rickrolled(self, ctx):
        embed = discord.Embed(
            title = 'SELAMAT!!! ANDA TELAH DI-RICKROLL!!!',
            colour = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_image(url='https://media1.tenor.com/images/8c409e6f39acc1bd796e8031747f19ad/tenor.gif')
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(CommandRahasia(client))
