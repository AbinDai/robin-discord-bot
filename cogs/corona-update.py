import discord, datetime, requests, re
from discord.ext import commands

class CoronaUpdate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        jam = datetime.datetime.utcnow().hour
        menit = datetime.datetime.utcnow().minute
        
        if int(jam) == 9 and int(menit) == 35: 
            api = requests.get("https://coronavirus-19-api.herokuapp.com/countries/indonesia").json()

            #tambahkan titik setelah tiga angka (contoh: 2.937.212)
            terinfeksi = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(api['cases']))
            sembuh = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(api['recovered']))
            meninggal = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(api['deaths']))
            #
            pertambahan_kasus = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(api['todayCases']))
            pertambahan_kematian = re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(api['todayDeaths']))
            
            embed = discord.Embed(
                title = f"Update Corona {str(datetime.datetime.today())[:-16]}",
                color = 0xe74d3c
            )
            embed.set_author(name="Update Harian COVID-19", icon_url="https://images-ext-2.discordapp.net/external/GFdeHKPhhW3dRT-6NUhI2iwpfooeaFIAosENDxcVxog/https/www.suse.com/c/wp-content/uploads/2020/03/corona.gif")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805880890194264137/817023521946599475/220px-SARS-CoV-2_without_background.png")

            embed.add_field(name="🟡 Terinfeksi", value=f"{terinfeksi}\n`+ {pertambahan_kasus}`")
            embed.add_field(name="🟢 Sembuh", value=sembuh)
            embed.add_field(name="🔴 Meninggal", value=f"{meninggal}\n`+ {pertambahan_kematian}`")

            await self.client.get_channel(866588260189208576).send(embed=embed)

def setup(client):
    client.add_cog(CoronaUpdate(client))
