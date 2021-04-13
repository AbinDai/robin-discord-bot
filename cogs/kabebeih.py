import discord
import requests
from discord.ext import commands

class KBBI(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("kabebeih.py siap!")

    @commands.command()
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def kbbi(self, ctx, *kata):
        try:
            if not kata:
                await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan kata yang ingin kamu lihat di KBBI!\nContoh: `r!kbbi bantal`")
            else:
                async with ctx.typing():
                    khata = "%20".join(kata)
                    api_panas = requests.get(f"https://kbbi-api-zhirrr.vercel.app/api/kbbi?text={khata}").json()
                    katah = api_panas["lema"]
                    arti = api_panas["arti"][0]

                    tabera = discord.Embed(
                        title = katah.upper(),
                        description = arti,
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    tabera.set_footer(text='Diberayakan oleh Badan Pengembangan dan Pembinaan Bahasa, Kemendikbud RI', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=tabera)
        except:
            kahta = " ".join(kata)
            embed = discord.Embed(
                title = f"{kahta.upper()}",
                description = "Kata tidak ditemukan...",
                color = 0xff0000
            )
            embed.set_footer(text='Diberayakan oleh Badan Pengembangan dan Pembinaan Bahasa, Kemendikbud RI', icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(KBBI(client))
