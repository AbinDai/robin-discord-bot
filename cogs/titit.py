import discord, random
from discord.ext import commands

class Titit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("titit.py :v siap")

    @commands.command(aliases=["kntl", "dicksize"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def titit(self, ctx, member: discord.Member):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak menyebutkan seseorang!\nContoh: `r!titit @Nathz#6498`")
        else:
            ukuran_titit = [
                "8=D",
                "8==D",
                "8===D",
                "8====D",
                "8=====D",
                "8======D",
                "8=======D",
                "8========D",
                "8=========D",
                "8==========D",
                "8===========D",
                "8============D",
                "8=============D",
                "8==============D",
                "8===============D",
                "8================D"
            ]
            embed = discord.Embed(
                title = f"Ukuran T*tit {member.display_name} :v",
                description = random.choice(ukuran_titit),
                color = member.color
            )
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Titit(client))