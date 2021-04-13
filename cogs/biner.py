import discord, requests
from discord.ext import commands

class Biner(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("biner.py siap!")

    @commands.command(aliases=["binary"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def biner(self, ctx, *teks):
        if not teks:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan teks yang akan dikonversi menjadi angka biner!\nContoh: `r!biner ini adalah tes`")
        else:
            tulisan = "%20".join(teks)
            api = requests.get(f"https://some-random-api.ml/binary?text={tulisan}").json()
            hasil = api["binary"]

            teqs = " ".join(teks)
            embed = discord.Embed(
                title = "Pengonversi Teks ke Biner",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="Teks", value=f"```\n{teqs}\n```", inline=False)
            embed.add_field(name="Hasil", value=f"```css\n{hasil}\n```", inline=False)
            await ctx.send(embed=embed)

    @commands.command(aliases=["binarytxt"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def binertxt(self, ctx, angka):
        if not angka:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan angka biner yang akan dikonversi menjadi teks biasa!\nContoh: `r!binertxt 01101000011000010110110001101111`")
        else:
            api = requests.get(f"https://some-random-api.ml/binary?decode={angka}").json()
            hasil = api["text"]

            embed = discord.Embed(
                title = "Pengonversi Biner ke Teks",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="Angka", value=f"```css\n{angka}\n```", inline=False)
            embed.add_field(name="Hasil", value=f"```\n{hasil}\n```", inline=False)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Biner(client))
