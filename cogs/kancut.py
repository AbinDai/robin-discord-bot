import discord
from discord.ext import commands

class Kancut(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["kancut"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kancuttext(self, ctx, *, nama:str=None):
        if not nama:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan nama! :v\nContoh: `r!kancuttext alpi`")
        else:
            embed = discord.Embed(
                title = "Kancut Text Generator :v",
                description = f"Review kancut {nama.capitalize()}:\n"
                               ".\n"
                               "- bahan\n"
                              f"sejatinya ane ga pernah perhatiin bahkan nyentuh CD {nama.capitalize()}, jadi nggak tau kualitas bahannya sebagus apa...\n"
                               "tapi sepertinya nyaman di kulit... \n"
                               "skor: 8/10\n"
                               ".\n"
                               "- kondisi:\n"
                               "agak lembab dan ada sedikit bekas noda kekuningan, itu artinya seller jujur dan mengirimkan item sesuai kondisi yg telah disepakati 😃\n"
                               "skor: 10/10\n"
                               ".\n"
                               "- aroma\n"
                               "kalian ingat sewaktu masih duduk di jenjang pendidikan SMP/SMA? ketika berpapasan dengan murid yang suka galer di jam pelajaran olahraga?\n"
                               "benar sekali! 👍👍👍\n"
                               "skor 90/10\n",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name}",icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    @kancuttext.error
    async def on_kancuttext_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            embed = discord.Embed(
                title = "Kancut Text Generator :v",
                description = "Maaf, terjadi error...",
                color = 0xff0000
            )
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name}",icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Kancut(client))
