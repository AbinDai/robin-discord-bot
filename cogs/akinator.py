import discord, akinator
from discord.ext import commands

class Gaming(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=["akinator", "akn"])
    async def tebakkarakter(self, ctx):
        embed = discord.Embed(
            title = "Permainan Akinator / Tebak Karakter",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed.add_field(name="Penjelasan",value="Ini merupakan permainan tebak-tebakan dimana seorang pemain akan menebak suatu karakter atau benda atau apapun itu. Beberapa pertanyaan akan diajukan.",inline=False)
        embed.add_field(name="Cara Bermain",value="Gunakan command `r!tebakkarakter start` untuk memulai. Tunggu beberapa saat hingga pertanyaan pertama diajukan. Bayangkan sebuah karakter atau apapun itu, bisa karakter fiksi maupun nyata. Jawab semua pertanyaan dengan benar sesuai dengan ciri-ciri karakter yang kamu bayangkan. Kalau bot menemukan siapa karakter tersebut dan ternyata benar bahwa itu karakter yang kamu maksud, maka bot menang. Tapi jika bot tidak menemukan karakter yang kamu maksud... atau karakter yang ditemukan bot tidak sesuai dengan yang kamu maksud, maka kamulah yang menang.",inline=False)
        embed.add_field(name="Cara Menjawab",value="Berikut beberapa opsi jawaban yang tersedia.\n"
                                                   "`yes      / y   / 0` = ya\n"
                                                   "`no       / n   / 1` = tidak\n"
                                                   "`i        / idk / 2` = tidak tahu\n"
                                                   "`probably / p   / 3` = mungkin\n"
                                                   "Ketika pertanyaan yang diajukan tidak sesuai dengan ciri-ciri karakter yang kamu bayangkan, maka jawab `n`. Atau kalau misalnya benar, jawab `y`, begitu seterusnya.", inline=False)
        embed.set_footer(text=f"Di-Request oleh {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @tebakkarakter.command(aliases=["mulai"])
    async def start(self, ctx):
        await ctx.send("Permainan akan dimulai sesaat lagi...")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n","idk", "p","kembali"]
        try:
            aki = akinator.Akinator()
            q = aki.start_game(language="id")
            while aki.progression <= 80:
                await ctx.send(f"**{q}**\nBalas: `y`(ya), `n`(tidak), `idk`(gatau), `p`(mungkin), atau `kembali`")
                msg = await self.client.wait_for("message", check=check)
                if msg.content.lower() == "kembali":
                    try:
                        q=aki.back()
                    except akinator.CantGoBackAnyFurther:
                        await ctx.send(e)
                        continue
                else:
                    try:
                        q = aki.answer(msg.content.lower())
                    except akinator.InvalidAnswerError as e:
                        await ctx.send(e)
                        continue
            aki.win()

            embed = discord.Embed( #bikin embed
                title = aki.first_guess['name'],
                description=f"{aki.first_guess['description']}",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            embed.set_image(url=aki.first_guess['absolute_picture_path'])
            embed.set_footer(text="Balas \"Benar\" kalau benar, atau \"Salah\" jika salah.")
            await ctx.send(embed=embed)

            correct = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=15)
            if correct.content.lower() == "benar":
                await ctx.send(":v\n")
            elif correct.content.lower() == "salah":
                await ctx.send(":'v\n")
        except Exception as e:
            await ctx.send(e)

def setup(client):
    client.add_cog(Gaming(client))
