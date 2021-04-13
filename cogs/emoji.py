import discord
from discord.ext import commands

class Emoji(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.Cog.listener()
  async def on_ready(self):
    print("emoji.py, siap!")
    
  @commands.command(aliases=["moji", "emj"])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def emoji(self, ctx, emoji: discord.Emoji=None):
    if not emoji:
      return await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Tuliskan emoji yang mau kamu lihat infonya, *ngab*.\nContoh: `r!moji :k_ketawa:`")
    try:
      emoji = await emoji.guild.fetch_emoji(emoji.id)
    except:
      return await ctx.send("<:robin_palato:818892964457349220> Emoji tidak ditemukan!")
    is_managed = "Ya" if emoji.managed else "Tidak"
    is_animated = "Ya" if emoji.animated else "Tidak"
    require_colons = "Ya" if emoji.require_colons else "Tidak"
    creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
    can_use_emoji = "Semuanya" if not emoji.roles else " ".join(role.name for role in emoji.roles)
    embed = discord.Embed(
      title = "Informasi Emoji",
      color = ctx.guild.get_member(self.client.user.id).color
    )
    embed.set_image(url=f'{emoji.url}')
    embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
    embed.add_field(name='Nama', value=f':{emoji.name}:')
    embed.add_field(name='ID', value=f'{emoji.id}')
    embed.add_field(name='Pengidentifikasi', value=f'`{emoji.name}:{emoji.id}`')
    embed.add_field(name='Ditambahkan oleh', value=f'{emoji.user.mention}')
    embed.add_field(name='Dibuat pada', value=f'{creation_time}')
    embed.add_field(name='Bisa digunakan oleh', value=f'{can_use_emoji}')
    embed.add_field(name='Beranimasi?', value=f'{is_animated}')
    embed.add_field(name='Dikelola?', value=f'{is_managed}')
    embed.add_field(name='Membutuhkan titik dua?', value=f'{require_colons}')
    embed.add_field(name='Server asal', value=f'{emoji.guild.name}')
    embed.add_field(name='ID server asal', value=f'{emoji.guild.id}')
    embed.add_field(name='Link', value=f'[Klik disini]({emoji.url})')
    await ctx.send(embed=embed)
    
def setup(client):
  client.add_cog(Emoji(client))
