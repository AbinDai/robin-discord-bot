import discord
import requests
from discord.ext import commands

class Gempa(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("gempa.py siap")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gempa(self, ctx):
        api = requests.get("https://gempa-api-zhirrr.vercel.app/api/gempa").json()
        waktu = api["Waktu"]
        lintang = api["Lintang"]
        bujur = api["Bujur"]
        magnitudo = api["Magnitudo"]
        kedalaman = api["Kedalaman"]
        wilayah = api["Wilayah"]
        map = api["Map"]

        tanagoyang = discord.Embed(
            title = "Gempa Bumi Terkini di Indonesia",
            color = 0xff0000
        )
        tanagoyang.set_thumbnail(url="http://iconsetc.com/icons-watermarks/simple-red/ocha/ocha_disaster-earthquake/ocha_disaster-earthquake_simple-red_512x512.png")
        tanagoyang.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        tanagoyang.add_field(name="Wilayah", value=wilayah, inline=False)
        tanagoyang.add_field(name="Waktu", value=waktu, inline=False)
        tanagoyang.add_field(name="Kedalaman", value=kedalaman, inline=False)
        tanagoyang.add_field(name="Lintang", value=lintang, inline=False)
        tanagoyang.add_field(name="Bujur", value=bujur, inline=False)
        tanagoyang.add_field(name="Magnitudo", value=f"{magnitudo}\n\nJangan panik, tetap pantau keadaan terkini, dan waspada terhadap gempa susulan yang mungkin bisa saja terjadi.", inline=False)
        await ctx.send(embed=tanagoyang)    

def setup(client):
    client.add_cog(Gempa(client))