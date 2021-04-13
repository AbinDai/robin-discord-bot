import discord
import random
from discord.ext import commands

class Rate(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.Cog.listener()
  async def on_ready(self):
    print("rate.py siap!")
    
  @commands.command(aliases=["nilai"])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def rate(self, ctx, *, obj=None):
    if not obj:
      await ctx.reply(f"<:robin_palato:818892964457349220> **Sintaks tidak valid!** Tuliskan objek yang akan saya nilai!\nContoh: `r!rate @Abin#4405`")
    else:
      tabera = random.randint(0, 10)
      await ctx.reply(f"Hmm, saya menilai {obj} **{tabera}/10.**")
      
def setup(client):
  client.add_cog(Rate(client))
