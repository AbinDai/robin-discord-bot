import discord
from discord.ext import commands

class Stres(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["wangy"])
    async def wangytext(self, ctx, *, konteks:str=None):
        if not konteks:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan nama!\nContoh: `r!wangytext sayu`")
        else:
            embed = discord.Embed(
                title = "Wangy Text Generator :v",
                description = f"{konteks.upper()}........... {konteks.upper()} {konteks.upper()} {konteks.upper()} AAAAAAAAAAAAAAAAAGH AAAAAAAAAAAAAAAAAAAAAAAGH <3 <3 <3 <3 WANGI WANGI WANGI WANGI HU HA HU HA HU HA, aaaah baunya {konteks.lower()} wangi aku mau nyiumin aroma wanginya {konteks.lower()} AAAAAAAAH rambutnya.... aaah rambutnya juga pengen aku elus-elus ~~~ AAAAAH {konteks.lower()} keluar pertama kali juga manis <3 <3 <3 dia pake baju itu juga manis banget AAAAAAAAH {konteks.upper()} LUCCUUUUUUUUUUUUUUU............ GUA BAKAL BAKAR DUIT 12 JUTA RUPIAH BUAT {konteks.upper()} AAAAAAAAAAAAAAAAAAAAAAAAAAAAAGH apa ? {konteks.capitalize()} itu gak nyata ? Cuma karakter 2 dimensi katamu ? nggak, ngak ngak ngak ngak NGAAAAAAAAK GUA GAK PERCAYA ITU DIA NYATA NGAAAAAAAAAAAAAAAAAK PEDULI BANGSAAAAAT !! GUA GAK PEDULI SAMA KENYATAAN POKOKNYA GAK PEDULI. {konteks.capitalize()} ngeliat gw ... {konteks.capitalize()} di HP ngeliatin gw {konteks.capitalize()}... kamu percaya sama aku ? aaaaaaaaaaah syukur {konteks.capitalize()} gak malu merelakan aku aaaaaah <3 <3 <3 YEAAAAAAAAAAAH GUA MASIH PUNYA {konteks.upper()}, SENDIRI PUN NGGAK MASALAH AAAAAAAAAAAAAAH, KIRIMKANLAH CINTAKU PADA {konteks.upper()} KIRIMKAN KE- AAAAAAAAH",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name}",icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    @wangytext.error
    async def on_wangytext_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            embed = discord.Embed(
                title = "Wangy Text Generator :v",
                description = "Maaf, terjadi error...",
                color = 0xff0000
            )
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name}",icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Stres(client))