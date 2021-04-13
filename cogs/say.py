import discord
from discord.ext import commands

class Say(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.Cog.listener()
  async def on_ready(self):
    print("say.py dengan 3 command, siap!")
  
  @commands.command(pass_context=True)
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def sayy(self, ctx, *, msg):
    if not msg:
      await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan kalimat!\nContoh: `r!sayy ini adalah teks`")
    else:
      await ctx.message.delete()
      await ctx.send(msg)
    
  @commands.command(pass_context=True)
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def sayem(self, ctx, *, msg):
    if not msg:
      await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan kalimat!\nContoh: `r!sayy ini adalah embed`")
    else:
      await ctx.message.delete()
      embed = discord.Embed(
        description = f'{msg}',
        color = ctx.guild.get_member(self.client.user.id).color
      )
      await ctx.send(embed=embed)
    
  @commands.command(pass_context=True)
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def say(self, ctx, *, msg):
    if not msg:
      await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan kalimat!\nContoh: `r!sayy ini adalah teks`")
    else:
      await ctx.message.delete()
      await ctx.send(f"{msg}\n\n**--{ctx.author}--**")
    
def setup(client):
  client.add_cog(Say(client))