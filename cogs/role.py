import discord
from discord.ext import commands

class Role(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("role.py siap!")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def roleinfo(self, ctx, role: discord.Role=None):
        if not role:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Tuliskan nama role yang ingin kamu lihat infonya!\nContoh: `r!roleinfo @Owner`")
        else:
            embed = discord.Embed(
                title = "Informasi Role",
                color = role.color
            )
            embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
            embed.add_field(name="Nama", value=role.mention)
            embed.add_field(name="ID", value=f"{role.id}")
            embed.add_field(name='Warna', value=f"{role.color}")
            embed.add_field(name="Posisi", value=role.position)
            embed.add_field(name="Terpisah dari yang Online", value=role.hoist)
            embed.add_field(name="Bisa Di-Mention", value=role.mentionable)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Role(client))
