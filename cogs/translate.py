import discord, requests
from discord.ext import commands

class Translate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("translate.py siap babang!!!")

    @commands.command(aliases=["tl", "tr"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def translate(self, ctx, lang_to=None, *kalimat):
        try:
            if lang_to == None:
                await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan kode bahasa tujuan!\nContoh: `r!tr id(<--kode bahasa indonesia) (isi kalimat-->)never gonna give you up` <:keanu_nunjuk:799114521347751996>")
            elif not kalimat:
                await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak menuliskan isi teks yang akan diterjemahkan!\nContoh: `r!tr id (isi kalimat-->)never gonna give you up` <:keanu_nunjuk:799114521347751996>")
            else:
                async with ctx.typing():
                    isi_kalimat = "%20".join(kalimat)
                    api = requests.get(f"https://amm-api-translate.herokuapp.com/translate?engine=google&text={isi_kalimat}&to={lang_to}").json()
                    bahasa_asal = api["data"]["origin"]
                    hasil_terjemahan = api["data"]["result"]

                    isy_kalymat = " ".join(kalimat)
                    embed = discord.Embed(
                        title = "Terjemahan",
                        description = f"**Teks ({bahasa_asal.upper()})**\n```\n{isy_kalymat}\n```\n**Hasil ({lang_to.upper()})**\n```\n{hasil_terjemahan}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text="Diberdayakan oleh Google Translate", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title = "Terjadi error...",
                description = "Kamu mungkin memasukkan kode bahasa yang salah, atau bisa jadi API mengalami error. Untuk melihat daftar kode bahasa yang valid, eksekusi command `r!translatecode` atau kunjungi laman [berikut](https://cloud.google.com/translate/docs/languages).\n\nPenulisan command: `r!tl [kode bahasa tujuan] [teks]`\nContoh: `r!tr en ini adalah tes`.",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)

    @commands.command(aliases=["tlcode", "trcode"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def translatecode(self, ctx):
        embed = discord.Embed(
            title = "Informasi Kode Bahasa dalam Format ISO-639-1",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_footer(text="Diberdayakan oleh Google Translate", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Urutan A", value="""Afrikaans: `af`
        Albania: `sq`
        Amharik: `am`
        Arab: `ar`
        Armenia: `hy`
        Azerbaijani: `az`
        """)
        embed.add_field(name="Urutan B", value="""Basque: `eu`
        Belarusia: `be`
        Bengali: `bn`
        Belanda: `nl`
        Bosnia: `bs`
        Bulgaria: `bg`
        """)
        embed.add_field(name="Urutan C", value="""Cebuano: `ceb` ([ISO-639-2](https://en.wikipedia.org/wiki/ISO_639-2))
        Ceko: `cs`
        China (Sederhana): `zh-CN` atau `zh` ([BCP-47](https://tools.ietf.org/html/bcp47))
        China (Tradisional): `zh-TW` ([BCP-47](https://tools.ietf.org/html/bcp47))
        """)
        embed.add_field(name="Urutan D", value="Denmark: `da`")
        embed.add_field(name="Urutan E", value="""Esperanto: `eo`
        Estonia: `et`
        """)
        embed.add_field(name="Urutan F", value="""Finlandia: `fi`
        Frisian: `fy`
        """)
        embed.add_field(name="Urutan G", value="""Gaelik Skotlandia: `gd`
        Galicia: `gl`
        Georgia: `ka`
        Gujarati: `gu`
        """)
        embed.add_field(name="Urutan H", value="""Hausa: `ha`
        Hawaii: `haw` ([ISO-639-2](https://en.wikipedia.org/wiki/ISO_639-2))
        Hmong: `hmn` ([ISO-639-2](https://en.wikipedia.org/wiki/ISO_639-2))
        Hongaria: `hu`
        """)
        embed.add_field(name="Urutan I", value="""Ibrani: `he` atau `iw`
        Igbo: `ig`
        India: `hi`
        **Indonesia: `id`**
        **Inggris: `en`**
        Irlandia: `ga`
        Islandia: `is`
        Italia: `it`
        """)
        embed.add_field(name="Urutan J", value="""Jepang: `ja`
        Jerman: `de`
        **Jawa: `jv`**
        """)
        embed.add_field(name="Urutan K", value="""Kannada: `kn`
        Katalan: `ca`
        Kazak: `kk`
        Khmer: `km`
        Kinyarwanda: `rw`
        Korea: `ko`
        Korsika: `co`
        Kroasia: `hr`
        Kreol Haiti: `ht`
        Kurdi: `ku`
        Kirgis: `ky`
        """)
        embed.add_field(name="Urutan L", value="""Lao: `lo`
        Latin: `la`
        Latvia: `lv`
        Lithuania: `lt`
        Luksemburg: `lb`
        """)
        embed.add_field(name="Urutan M", value="""Makedonia: `mk`
        Malagasi: `mg`
        Melayu: `ms`
        Malayalam: `ml`
        Malta: `mt`
        Maori: `mi`
        Marathi: `mr`
        Mongolia: `mn`
        Myanmar (Burma): `my`
        """)
        embed.add_field(name="Urutan N", value="""Nepal: `ne`
        Norsk: `no`
        Nyanja (Chichewa): `ny`
        """)
        embed.add_field(name="Urutan O", value="Odia (Oriya): `or`")
        embed.add_field(name="Urutan P", value="""Pashto: `ps`
        Perancis: `fr`
        Persia: `fa`
        Polandia: `pl`
        Portugis (Portugal, Brasil): `pt`
        Punjabi: `pa`
        """)
        embed.add_field(name="Urutan R", value="""Rumania: `ro`
        Rusia: `ru`
        """)
        embed.add_field(name="Urutan S", value="""Samoa: `sm`
        Serbia: `sr`
        Shona: `sn`
        Sindhi: `sd`
        Sinhala (Sinhala): `si`
        Slovakia: `sk`
        Slovenia: `sl`
        Somalia: `so`
        Spanyol: `es`
        **Sunda: `su`**
        Swahili: `sw`
        Swedia: `sv`
        """)
        embed.add_field(name="Urutan T", value="""Tagalog (Filipina): `tl`
        Tajik: `tg`
        Tamil: `ta`
        Tatar: `tt`
        Telugu: `te`
        Thailand: `th`
        Turki: `tr`
        Turkmenistan: `tk`
        """)
        embed.add_field(name="Urutan U", value="""Ukraina: `uk`
        Urdu: `ur`
        Uyghur: `ug`
        Uzbek: `uz`
        """)
        embed.add_field(name="Urutan V", value="Vietnam: `vi`")
        embed.add_field(name="Urutan W", value="Welsh: `cy`")
        embed.add_field(name="Urutan X", value="Xhosa: `xh`")
        embed.add_field(name="Urutan Y", value="""Yiddi: `yi`
        Yoruba: `yo`
        """)
        embed.add_field(name="Urutan Z", value="Zulu: `zu`\n\nSumber: https://cloud.google.com/translate/docs/languages")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Translate(client))

