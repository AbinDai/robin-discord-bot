import discord, requests, os
from discord.ext import commands
from PIL import Image

class EnlargeEmoji(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["e"])
    async def enlarge(self, ctx, emoji:discord.PartialEmoji=None):
        if not emoji:
            return await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan emoji yang ingin diperbesar!\nContoh: `r!e :k_tatawa:`")

        link_emoji = emoji.url

        #donlot emojinya
        donlot = requests.get(link_emoji)
        file = open("resize.png", "wb")
        file.write(donlot.content)
        file.close()

        #kode utk me-resize emoji (untuk png saja)
        def pembesar_gambar(namafile:str):
            gambar = Image.open(namafile)
            atur_ukuran = gambar.resize((1000, 1000))
            atur_ukuran.save("resized.png")

        #resize emoji-nya
        async with ctx.typing():
            if str(link_emoji).endswith(".gif"):
                emubeddo = discord.Embed(
                    title = "Pembesar Emoji",
                    description = "Sayangnya untuk emoji .gif tidak dapat dibesarkan sebesar pada .png :'v",
                    color = ctx.guild.me.color
                )
                emubeddo.set_image(url=link_emoji)
                emubeddo.set_footer(text=f":{emoji.name}:")
                await ctx.send(embed=emubeddo)
            elif str(link_emoji).endswith(".png"):
                pembesar_gambar("resize.png")

                fairu = discord.File("./resized.png", filename="resized.png")
                emubeddo = discord.Embed(
                    title = "Pembesar Emoji",
                    color = ctx.guild.me.color
                )
                emubeddo.set_image(url=f"attachment://resized.png")
                emubeddo.set_footer(text=f":{emoji.name}:")
                await ctx.send(file=fairu, embed=emubeddo)
                os.remove("resized.png")
                os.remove("resize.png")

    @enlarge.error
    async def on_enlarge_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.reply("Sayang sekali, bot tidak dapat memperbesar emoji bawaan :'v")

def setup(client):
    client.add_cog(EnlargeEmoji(client))