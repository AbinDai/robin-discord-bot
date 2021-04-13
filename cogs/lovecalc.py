import discord, random
from discord.ext import commands

class LoveCalc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("lovecalc.py siap")

    @commands.command(aliases=["lc", "kalkcinta"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lovecalc(self, ctx, nama1, nama2=None):
        if not nama1:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan nama orang pertama yang mau kamu jodohkan!\nContoh: `r!lovecalc **[nama1]** [nama2]`")
        elif nama2 == None:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan nama orang yang ingin kamu jodohkan!\nContoh: `r!lovecalc [nama1] **[nama2]**`")

        persen = random.randint(0, 100)
        embed = discord.Embed(
            title = "Kalkulator Cinta",
            description = f"{nama1} :heart: {nama2}\nCinta kalian berdua: **{persen}%!** :v",
            color = discord.Color.red()
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(LoveCalc(client)) 