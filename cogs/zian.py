import discord, random
from discord.ext import commands

class Zian(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.Cog.listener()
  async def on_ready(self):
    print("zian.py, siap!")
    
  @commands.command(aliases=['zian'])
  async def ziansuffer(self, ctx):
    list_daftar_foto_zian = [
      'https://cdn.discordapp.com/attachments/783036987497513041/818656797732241459/IMG-20210309-WA0001.jpg',
      'https://cdn.discordapp.com/attachments/783036987497513041/818657866239705088/magik.png'
    ]
    embed = discord.Embed(
      title = 'Zian\'s Suffering...',
      color = ctx.guild.get_member(self.client.user.id).color
    )
    embed.set_image(url=f'{random.choice(list_daftar_foto_zian)}')
    embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(Zian(client))