import discord, random
from discord.ext import commands
from discord.ext.commands.context import Context

class GakNyangka(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="gak-nyangka", aliases=["gn"])
    async def gaknyangka(self, ctx:Context, *, nama):
        if not nama:
            return await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan nama karakter/orang yang ingin kamu gunakan dalam teksnya!\nContoh: `r!gak-nyangka sayu`")

        embed = discord.Embed(
            title = "'Gak Nyangka' Text Generator :v",
            description = f"Beneran gak nyangka, out of nowhere gitu, bener-bener di luar ekspetasi banget ini. Lagi rebahan merenungkan hidup, tiba-tiba ada yang dateng, ngelamar aku. Malu plus kaget banget. Karena jelas, aku ga ada niatan buat nikah. Sama sekali, apalagi kalo kalian tau kondisiku. Please lah, aku tuh belum punya pekerjaan, lulus kuliah aja beloman. Mana ga ada modal buat nikah apalagi berkeluarga. Dia tipeku banget sih anjir... banget malah. Kalo aku mutusin buat nikah, pasti aku mau sama dia. Udah baik, senyumnya manis, suka bantuin aku pas ada masalah, perhatian, tegas kalo dibutuhkan, selalu ada buat aku, mana kelakuannya nggak nahan pula, keknya pas diciptakan Tuhan nggak nanggung-nanggung deh nambahin speknya. Sayang banget belum bisa aku terima langsung...\n\nMaaf {nama}, kita coba pendekatan dulu ya?",
            color = ctx.guild.me.color
        )

        if len(ctx.message.attachments) != 0:
            embed.set_image(url=ctx.message.attachments[0].url)

        if random.randint(0, 1000+1) == 500:
            if len(ctx.message.attachments) == 0:
                embed.set_footer(text="Tip: Kamu bisa mengupload foto karakter kesukaanmu sambil mengeksekusi perintah ini untuk disandingkan bersama dengan teks.")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(GakNyangka(client))