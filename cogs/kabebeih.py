import discord
from discord.ext.commands.context import Context
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
    async def kbbi(self, ctx:Context, *kata):
        if not kata:
            return await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan kata yang ingin kamu lihat di KBBI!\nContoh: `r!kbbi bantal`")

        def bikin_embed(title:str, desc:str, color):
            embed = discord.Embed(
                title = title,
                description = desc
            )
            embed.set_footer(text="Diberayakan oleh Badan Pengembangan dan Pembinaan Bahasa, Kemendikbud RI", icon_url="https://www.kemdikbud.go.id/main/files/large/83790f2b43f00be")

            if color:
                embed.color = color

            return embed

        pesan_awal = await ctx.send(embed=bikin_embed(
            title = str(" ".join(kata)).upper(),
            desc = "<a:loading:854013569552220200> Mencari kata...",
            color = discord.Color.blurple()
        ))

        try:
            api = requests.get(f"https://kbbi-api-zhirrr.vercel.app/api/kbbi?text={'%20'.join(kata)}").json()

            await pesan_awal.edit(embed=bikin_embed(
                title = str(api["lema"]).upper(),
                desc = api["arti"][0],
                color = ctx.guild.me.color
            ))
        except:
            await pesan_awal.edit(embed=bikin_embed(
                title = str(" ".join(kata)).upper(),
                desc = "Kata tidak ditemukan!",
                color = 0xff0000
            ))

def setup(client):
    client.add_cog(KBBI(client))
