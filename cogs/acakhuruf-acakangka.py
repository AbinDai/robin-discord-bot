import asyncio, random
from discord.ext import commands

class AcakHuruf(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("acakhuruf-acakangka.py siap!")

    @commands.command(aliases=["randomletter"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def acakhuruf(self, ctx):
        list_emot_huruf = [
            ":regional_indicator_a:",
            ":regional_indicator_b:",
            ":regional_indicator_c:",
            ":regional_indicator_d:",
            ":regional_indicator_e:",
            ":regional_indicator_f:",
            ":regional_indicator_g:",
            ":regional_indicator_h:",
            ":regional_indicator_i:",
            ":regional_indicator_j:",
            ":regional_indicator_k:", 
            ":regional_indicator_l:",
            ":regional_indicator_m:",
            ":regional_indicator_n:",
            ":regional_indicator_o:",
            ":regional_indicator_p:",
            ":regional_indicator_q:",
            ":regional_indicator_r:",
            ":regional_indicator_s:",
            ":regional_indicator_t:",
            ":regional_indicator_u:",
            ":regional_indicator_v:",
            ":regional_indicator_w:",
            ":regional_indicator_x:",
            ":regional_indicator_y:",
            ":regional_indicator_z:"
        ]

        async with ctx.typing():
            await asyncio.sleep(5)
            await ctx.reply(random.choice(list_emot_huruf))

    @commands.command(aliases=["randomnumber"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def acakangka(self, ctx, angka1=None, angka2=None):
        if not angka1:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan dasar angkanya!\nContoh: `r!acakangka 1 10` (maksudnya dari 1 ke 10)")
        elif angka2 == None:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan batas angkanya!\nContoh: `r!acakangka 1 10` (maksudnya dari 1 ke 10)")
        else:
            async with ctx.typing():
                await asyncio.sleep(5)
                await ctx.reply(f"**{random.randint(int(angka1), int(angka2))}**")

def setup(client):
    client.add_cog(AcakHuruf(client))