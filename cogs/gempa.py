import discord, requests
from discord.ext import commands

class Gempa(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gempa(self, ctx):
        api = requests.get("https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json").json()
        
        embed = discord.Embed(
            title = "Info Gempa Terkini di Indonesia",
            color = 0xff0000
        )
        #embed.set_thumbnail(url="http://iconsetc.com/icons-watermarks/simple-red/ocha/ocha_disaster-earthquake/ocha_disaster-earthquake_simple-red_512x512.png")
        #embed.set_image(url=api["Infogempa"]["gempa"]["Shakemap"])
        #embed.set_footer(text="Badan Meteorologi, Klimatologi, dan Geofisika", icon_url="https://cdn.bmkg.go.id/Web/Logo-BMKG-new-242x300.png")
        
        embed.add_field(name="Tanggal", value=api["Infogempa"]["gempa"]["Tanggal"])
        embed.add_field(name="Jam", value=api["Infogempa"]["gempa"]["Jam"])
        embed.add_field(name="Datetime", value=api["Infogempa"]["gempa"]["DateTime"])
        
        embed.add_field(name="Koordinat", value=api["Infogempa"]["gempa"]["Coordinates"])
        embed.add_field(name="Lintang", value=api["Infogempa"]["gempa"]["Lintang"])
        embed.add_field(name="Bujur", value=api["Infogempa"]["gempa"]["Bujur"])
        
        embed.add_field(name="Magnitudo", value=api["Infogempa"]["gempa"]["Magnitude"])
        embed.add_field(name="Kedalaman", value=api["Infogempa"]["gempa"]["Kedalaman"])
        embed.add_field(name="Wilayah", value=api["Infogempa"]["gempa"]["Wilayah"])
        
        embed.add_field(name="Potensi", value=api["Infogempa"]["gempa"]["Potensi"], inline=False)
        embed.add_field(name="Dirasakan", value=api["Infogempa"]["gempa"]["Dirasakan"], inline=False)
        
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(Gempa(client))
