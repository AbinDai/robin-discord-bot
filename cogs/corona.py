import discord, re, requests
from discord.ext import commands

class Corona(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=["covid-19", "covid19", "coronavirus", "korona", "corona"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def covid(self, ctx, *negara):
        #negara = "indonesia" if not negara else negara
        if not negara:
            link_api = "https://coronavirus-19-api.herokuapp.com/countries/indonesia"
        else:
            link_api = f"https://coronavirus-19-api.herokuapp.com/countries/{'%20'.join(negara)}"
        
        api = requests.get(link_api).json()
        
        kasus = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', f"{api['cases']}")
        penambahan_kasus = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', f"{api['todayCases']}")
        
        sembuh = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', f"{api['recovered']}")
        
        meninggal = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', f"{api['deaths']}")
        penambahan_kematian = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', f"{api['todayDeaths']}")
        
        embed = discord.Embed(
            color = 0xb64242
        )
        embed.set_author(name="Info COVID-19", icon_url="https://images-ext-2.discordapp.net/external/GFdeHKPhhW3dRT-6NUhI2iwpfooeaFIAosENDxcVxog/https/www.suse.com/c/wp-content/uploads/2020/03/corona.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805880890194264137/817023521946599475/220px-SARS-CoV-2_without_background.png")
        
        if negara == "world":
            embed.title = "Kasus COVID-19 di Seluruh Dunia"
        else:
            embed.title = f"Kasus COVID-19 di {api['country']}"
        
        embed.add_field(name="🟡 Terinfeksi", value=f"{kasus}\n`+ {penambahan_kasus}`")
        embed.add_field(name="🟢 Sembuh", value=sembuh)
        embed.add_field(name="🔴 Meninggal", value=f"{meninggal}\n`+ {penambahan_kematian}`")
        
        embed.add_field(name="⠀", value="Tetap patuhi protokol kesehatan. Gunakan masker ketika berada di luar rumah, jaga jarak untuk meminimalisir kemungkinan tertular, selalu cuci tangan pakai sabun, dan jangan sampai tertular.")
        
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(Corona(client))
