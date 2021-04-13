import discord, requests
from discord.ext import commands


class covid(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("corona.py siap")

    @commands.command(aliases=["covid-19", "covid19", "coronavirus", "korona", "corona"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def covid(self, ctx, *countryName):
        try:
            if not countryName:
                api = requests.get(f"https://coronavirus-19-api.herokuapp.com/countries/indonesia").json()
                positif = api["cases"]
                sembuh = api["recovered"]
                meninggoy = api["deaths"]
                dirawat = api["active"]

                embed = discord.Embed(
                    color = discord.Colour.red()
                )
                embed.set_author(name="Status COVID-19 di Indonesia", icon_url="https://www.suse.com/c/wp-content/uploads/2020/03/corona.gif")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805880890194264137/817023521946599475/220px-SARS-CoV-2_without_background.png")
                embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                embed.add_field(name="Kasus Positif", value=positif, inline=False)
                embed.add_field(name="Kasus Sembuh", value=sembuh, inline=False)
                embed.add_field(name="Kasus Meninggal", value=f"{meninggoy}\n", inline=False)
                embed.add_field(name="Masih Dirawat", value=f"{dirawat}\n\nTetap patuhi protokol kesehatan. Gunakan masker ketika berada di luar rumah, jaga jarak untuk meminimalisir kemungkinan tertular, selalu cuci tangan pakai sabun, dan jangan sampai tertular.", inline=False)
                await ctx.send(embed=embed)
            else:
                negara = "%20".join(countryName)
                api = requests.get(f"https://coronavirus-19-api.herokuapp.com/countries/{negara}").json()
                neggara = api["country"]
                confirmed = api["cases"]
                recovered = api["recovered"]
                deaths = api["deaths"]
                active = api["active"]

                embed = discord.Embed(
                    color = discord.Colour.red()
                )
                embed.set_author(name=f"Status COVID-19 di {neggara}", icon_url="https://www.suse.com/c/wp-content/uploads/2020/03/corona.gif")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805880890194264137/817023521946599475/220px-SARS-CoV-2_without_background.png")
                embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                embed.add_field(name="Kasus Positif", value=confirmed, inline=False)
                embed.add_field(name="Kasus Sembuh", value=recovered, inline=False)
                embed.add_field(name="Kasus Meninggal", value=f"{deaths}\n", inline=False)
                embed.add_field(name="Masih Dirawat", value=f"{active}\n\nTetap patuhi protokol kesehatan. Gunakan masker ketika berada di luar rumah, jaga jarak untuk meminimalisir kemungkinan tertular, selalu cuci tangan pakai sabun, dan jangan sampai tertular.", inline=False)
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title = "Nama negara tidak valid!",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)



def setup(client):
    client.add_cog(covid(client))