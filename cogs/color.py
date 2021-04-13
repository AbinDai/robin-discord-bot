import discord, requests
from discord.ext import commands

class Color(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("color.py, siap!")

    @commands.command(aliases=["hex", "colour", "warna"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def color(self, ctx, color=None):
        try:
            if not color:
                await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan HEX warna yang ingin kamu ketahui detailnya **tanpa tanda `#`**.\nContoh: `r!color ffff00`")
            else:
                hasil = requests.get(f"https://www.thecolorapi.com/id?hex={color}").json()
                nama_warna = hasil["name"]["value"]
                kode_hex = hasil["hex"]["value"]
                rgb_R = hasil["rgb"]["r"]
                rgb_G = hasil["rgb"]["g"]
                rgb_B = hasil["rgb"]["b"]
                hsl_H = hasil["hsl"]["h"]
                hsl_S = hasil["hsl"]["s"]
                hsl_L = hasil["hsl"]["l"]
                hsv_H = hasil["hsv"]["h"]
                hsv_S = hasil["hsv"]["s"]
                hsv_V = hasil["hsv"]["v"]
                cmyk_C = hasil["cmyk"]["c"]
                cmyk_M = hasil["cmyk"]["m"]
                cmyk_Y = hasil["cmyk"]["y"]
                cmyk_K = hasil["cmyk"]["k"]
                xyz_X = hasil["XYZ"]["X"]
                xyz_Y = hasil["XYZ"]["Y"]
                xyz_Z = hasil["XYZ"]["Z"]

                warnaEmbed = int(f"{color}", 16)
                embed = discord.Embed(
                    title = f"Warna: {nama_warna}",
                    color = warnaEmbed
                )
                embed.set_thumbnail(url=f'https://some-random-api.ml/canvas/colorviewer?hex={color}')
                embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
                embed.add_field(name="HEX", value=f"`{kode_hex}`")
                embed.add_field(name="RGB", value=f"`{rgb_R}, {rgb_G}, {rgb_B}`")
                embed.add_field(name="HSL", value=f"`{hsl_H}, {hsl_S}, {hsl_L}`")
                embed.add_field(name="HSV", value=f"`{hsv_H}, {hsv_S}, {hsv_V}`")
                embed.add_field(name="CMYK", value=f"`{cmyk_C}, {cmyk_M}, {cmyk_Y}, {cmyk_K}`")
                embed.add_field(name="XYZ", value=f"`{xyz_X}, {xyz_Y}, {xyz_Z}`")
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title = ":x: Warna tidak valid!",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Color(client))
