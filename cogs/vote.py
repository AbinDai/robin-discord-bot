import discord
from discord.ext import commands

class Vote(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def upvote(self, ctx):
    embed = discord.Embed(
      title = "Vote Robin untuk Membantu Bot Ini Berkembang!",
      description = "Apa kamu suka dengan fitur-fitur yang ada pada bot ini? Jangan lupa berikan dukunganmu dengan cara nge-Vote saya di top.gg. Vote-nya gratis, tidak dipungut biaya!\n\nVote [disini](https://top.gg/bot/805876219647361053/vote)!",
      color = ctx.guild.get_member(805876219647361053).color
    )
    embed.set_thumbnail(url=self.client.user.avatar_url_as(format="png",size=4096))
    await ctx.send(embed=embed)
    
def setup(client):
  client.add_cog(Vote(client))
