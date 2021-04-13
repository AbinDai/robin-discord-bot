import discord, requests, DiscordUtils
from discord.ext import commands

class KodePos(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("kodepos.py")

    @commands.command()
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def kodepos(self, ctx, *kota):
        try:
            if not kota:
                await ctx.reply("**Sintaks tidak valid!** Anda tidak memasukkan nama kota/tempat!\nContoh: `r!kodepos gorontalo`")
            else:
                async with ctx.typing():
                    nama_tempat = "%20".join(kota)
                    api = requests.get(f"https://kodepos.herokuapp.com/search?q={nama_tempat}").json()
                    provinsi1 = api["data"][0]["province"]
                    kota1 = api["data"][0]["city"]
                    kecamatan1 = api["data"][0]["subdistrict"]
                    perkotaan1 = api["data"][0]["urban"]
                    kodepos1 = api["data"][0]["postalcode"]

                    provinsi2 = api["data"][1]["province"]
                    kota2 = api["data"][1]["city"]
                    kecamatan2 = api["data"][1]["subdistrict"]
                    perkotaan2 = api["data"][1]["urban"]
                    kodepos2 = api["data"][1]["postalcode"]

                    provinsi3 = api["data"][2]["province"]
                    kota3 = api["data"][2]["city"]
                    kecamatan3 = api["data"][2]["subdistrict"]
                    perkotaan3 = api["data"][2]["urban"]
                    kodepos3 = api["data"][2]["postalcode"]

                    provinsi4 = api["data"][3]["province"]
                    kota4 = api["data"][3]["city"]
                    kecamatan4 = api["data"][3]["subdistrict"]
                    perkotaan4 = api["data"][3]["urban"]
                    kodepos4 = api["data"][3]["postalcode"]

                    provinsi5 = api["data"][4]["province"]
                    kota5 = api["data"][4]["city"]
                    kecamatan5 = api["data"][4]["subdistrict"]
                    perkotaan5 = api["data"][4]["urban"]
                    kodepos5 = api["data"][4]["postalcode"]

                    provinsi6 = api["data"][5]["province"]
                    kota6 = api["data"][5]["city"]
                    kecamatan6 = api["data"][5]["subdistrict"]
                    perkotaan6 = api["data"][5]["urban"]
                    kodepos6 = api["data"][5]["postalcode"]

                    provinsi7 = api["data"][6]["province"]
                    kota7 = api["data"][6]["city"]
                    kecamatan7 = api["data"][6]["subdistrict"]
                    perkotaan7 = api["data"][6]["urban"]
                    kodepos7 = api["data"][6]["postalcode"]

                    provinsi8 = api["data"][7]["province"]
                    kota8 = api["data"][7]["city"]
                    kecamatan8 = api["data"][7]["subdistrict"]
                    perkotaan8 = api["data"][7]["urban"]
                    kodepos8 = api["data"][7]["postalcode"]

                    provinsi9 = api["data"][8]["province"]
                    kota9 = api["data"][8]["city"]
                    kecamatan9 = api["data"][8]["subdistrict"]
                    perkotaan9 = api["data"][8]["urban"]
                    kodepos9 = api["data"][8]["postalcode"]

                    provinsi10 = api["data"][9]["province"]
                    kota10 = api["data"][9]["city"]
                    kecamatan10 = api["data"][9]["subdistrict"]
                    perkotaan10 = api["data"][9]["urban"]
                    kodepos10 = api["data"][9]["postalcode"]

                    provinsi11 = api["data"][10]["province"]
                    kota11 = api["data"][10]["city"]
                    kecamatan11 = api["data"][10]["subdistrict"]
                    perkotaan11 = api["data"][10]["urban"]
                    kodepos11 = api["data"][10]["postalcode"]

                    provinsi12 = api["data"][10]["province"]
                    kota12 = api["data"][10]["city"]
                    kecamatan12 = api["data"][10]["subdistrict"]
                    perkotaan12 = api["data"][10]["urban"]
                    kodepos12 = api["data"][10]["postalcode"]

                    provinsi13 = api["data"][12]["province"]
                    kota13 = api["data"][12]["city"]
                    kecamatan13 = api["data"][12]["subdistrict"]
                    perkotaan13 = api["data"][12]["urban"]
                    kodepos13 = api["data"][12]["postalcode"]

                    provinsi13 = api["data"][12]["province"]
                    kota13 = api["data"][12]["city"]
                    kecamatan13 = api["data"][12]["subdistrict"]
                    perkotaan13 = api["data"][12]["urban"]
                    kodepos13 = api["data"][12]["postalcode"]

                    provinsi14 = api["data"][13]["province"]
                    kota14 = api["data"][13]["city"]
                    kecamatan14 = api["data"][13]["subdistrict"]
                    perkotaan14 = api["data"][13]["urban"]
                    kodepos14 = api["data"][13]["postalcode"]

                    provinsi15 = api["data"][14]["province"]
                    kota15 = api["data"][14]["city"]
                    kecamatan15 = api["data"][14]["subdistrict"]
                    perkotaan15 = api["data"][14]["urban"]
                    kodepos15 = api["data"][14]["postalcode"]

                    provinsi16 = api["data"][15]["province"]
                    kota16 = api["data"][15]["city"]
                    kecamatan16 = api["data"][15]["subdistrict"]
                    perkotaan16 = api["data"][15]["urban"]
                    kodepos16 = api["data"][15]["postalcode"]

                    provinsi17 = api["data"][16]["province"]
                    kota17 = api["data"][16]["city"]
                    kecamatan17 = api["data"][16]["subdistrict"]
                    perkotaan17 = api["data"][16]["urban"]
                    kodepos17 = api["data"][16]["postalcode"]

                    provinsi18 = api["data"][17]["province"]
                    kota18 = api["data"][17]["city"]
                    kecamatan18 = api["data"][17]["subdistrict"]
                    perkotaan18 = api["data"][17]["urban"]
                    kodepos18 = api["data"][17]["postalcode"]

                    provinsi19 = api["data"][18]["province"]
                    kota19 = api["data"][18]["city"]
                    kecamatan19 = api["data"][18]["subdistrict"]
                    perkotaan19 = api["data"][18]["urban"]
                    kodepos19 = api["data"][18]["postalcode"]
                    
                    provinsi20 = api["data"][19]["province"]
                    kota20 = api["data"][19]["city"]
                    kecamatan20 = api["data"][19]["subdistrict"]
                    perkotaan20 = api["data"][19]["urban"]
                    kodepos20 = api["data"][19]["postalcode"]

                    embed1 = discord.Embed(
                        title = "Rincian Tempat Beserta Kode Pos",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/805880890194264137/822303916224938044/kisspng-sw-postcode-area-nw-postcode-area-postcodes-in-the-london-map-5b350599bfefd3.489928751530201.png")
                    embed1.set_footer(text=f"Halaman 1/4 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                    embed1.add_field(name="Hasil 1", value=f"Provinsi: {provinsi1}\nKota: {kota1}\nKecamatan: {kecamatan1}\nPerkotaan: {perkotaan1}\nKode Pos: {kodepos1}")
                    embed1.add_field(name="Hasil 2", value=f"Provinsi: {provinsi2}\nKota: {kota2}\nKecamatan: {kecamatan2}\nPerkotaan: {perkotaan2}\nKode Pos: {kodepos2}")
                    embed1.add_field(name="Hasil 3", value=f"Provinsi: {provinsi3}\nKota: {kota3}\nKecamatan: {kecamatan3}\nPerkotaan: {perkotaan3}\nKode Pos: {kodepos3}")
                    embed1.add_field(name="Hasil 4", value=f"Provinsi: {provinsi4}\nKota: {kota4}\nKecamatan: {kecamatan4}\nPerkotaan: {perkotaan4}\nKode Pos: {kodepos4}")
                    embed1.add_field(name="Hasil 5", value=f"Provinsi: {provinsi5}\nKota: {kota5}\nKecamatan: {kecamatan5}\nPerkotaan: {perkotaan5}\nKode Pos: {kodepos5}")
                    embed1.add_field(name="Hasil 6", value=f"Provinsi: {provinsi6}\nKota: {kota6}\nKecamatan: {kecamatan6}\nPerkotaan: {perkotaan6}\nKode Pos: {kodepos6}")

                    embed2 = discord.Embed(
                        title = "Rincian Tempat Beserta Kode Pos",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/805880890194264137/822303916224938044/kisspng-sw-postcode-area-nw-postcode-area-postcodes-in-the-london-map-5b350599bfefd3.489928751530201.png")
                    embed2.set_footer(text=f"Halaman 2/4 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                    embed2.add_field(name="Hasil 7", value=f"Provinsi: {provinsi7}\nKota: {kota7}\nKecamatan: {kecamatan7}\nPerkotaan: {perkotaan7}\nKode Pos: {kodepos7}")
                    embed2.add_field(name="Hasil 8", value=f"Provinsi: {provinsi8}\nKota: {kota8}\nKecamatan: {kecamatan8}\nPerkotaan: {perkotaan8}\nKode Pos: {kodepos8}")
                    embed2.add_field(name="Hasil 9", value=f"Provinsi: {provinsi9}\nKota: {kota9}\nKecamatan: {kecamatan9}\nPerkotaan: {perkotaan9}\nKode Pos: {kodepos9}")
                    embed2.add_field(name="Hasil 10", value=f"Provinsi: {provinsi10}\nKota: {kota10}\nKecamatan: {kecamatan10}\nPerkotaan: {perkotaan10}\nKode Pos: {kodepos10}")
                    embed2.add_field(name="Hasil 11", value=f"Provinsi: {provinsi11}\nKota: {kota11}\nKecamatan: {kecamatan11}\nPerkotaan: {perkotaan11}\nKode Pos: {kodepos11}")
                    embed2.add_field(name="Hasil 12", value=f"Provinsi: {provinsi12}\nKota: {kota12}\nKecamatan: {kecamatan12}\nPerkotaan: {perkotaan12}\nKode Pos: {kodepos12}")

                    embed3 = discord.Embed(
                        title = "Rincian Tempat Beserta Kode Pos",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/805880890194264137/822303916224938044/kisspng-sw-postcode-area-nw-postcode-area-postcodes-in-the-london-map-5b350599bfefd3.489928751530201.png")
                    embed3.set_footer(text=f"Halaman 3/4 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                    embed3.add_field(name="Hasil 13", value=f"Provinsi: {provinsi13}\nKota: {kota13}\nKecamatan: {kecamatan13}\nPerkotaan: {perkotaan13}\nKode Pos: {kodepos13}")
                    embed3.add_field(name="Hasil 14", value=f"Provinsi: {provinsi14}\nKota: {kota14}\nKecamatan: {kecamatan14}\nPerkotaan: {perkotaan14}\nKode Pos: {kodepos14}")
                    embed3.add_field(name="Hasil 15", value=f"Provinsi: {provinsi15}\nKota: {kota15}\nKecamatan: {kecamatan15}\nPerkotaan: {perkotaan15}\nKode Pos: {kodepos15}")
                    embed3.add_field(name="Hasil 16", value=f"Provinsi: {provinsi16}\nKota: {kota16}\nKecamatan: {kecamatan16}\nPerkotaan: {perkotaan16}\nKode Pos: {kodepos16}")
                    embed3.add_field(name="Hasil 17", value=f"Provinsi: {provinsi17}\nKota: {kota17}\nKecamatan: {kecamatan17}\nPerkotaan: {perkotaan17}\nKode Pos: {kodepos17}")
                    embed3.add_field(name="Hasil 18", value=f"Provinsi: {provinsi18}\nKota: {kota18}\nKecamatan: {kecamatan18}\nPerkotaan: {perkotaan18}\nKode Pos: {kodepos18}")

                    embed4 = discord.Embed(
                        title = "Rincian Tempat Beserta Kode Pos",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed4.set_thumbnail(url="https://cdn.discordapp.com/attachments/805880890194264137/822303916224938044/kisspng-sw-postcode-area-nw-postcode-area-postcodes-in-the-london-map-5b350599bfefd3.489928751530201.png")
                    embed4.set_footer(text=f"Halaman 4/4 • Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                    embed4.add_field(name="Hasil 19", value=f"Provinsi: {provinsi19}\nKota: {kota19}\nKecamatan: {kecamatan19}\nPerkotaan: {perkotaan19}\nKode Pos: {kodepos19}")
                    embed4.add_field(name="Hasil 20", value=f"Provinsi: {provinsi20}\nKota: {kota20}\nKecamatan: {kecamatan20}\nPerkotaan: {perkotaan20}\nKode Pos: {kodepos20}")

                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
                    paginator.add_reaction("◀", "back")
                    paginator.add_reaction("▶", "next")
                    embed_embed = [embed1, embed2, embed3, embed4]
                    await paginator.run(embed_embed)
        except:
            embed = discord.Embed(
                title = "Nama kota/tempat yang Anda masukkan tidak valid!",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(KodePos(client))
