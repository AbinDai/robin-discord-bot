import discord, json, asyncio
from discord.ext import commands
from discord.message import Message

class Autoreplier(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=["autoreply", "autorespond", "balasotomatis"])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_guild=True)
    async def autoreplier(self, ctx:commands.Context):
        embed = discord.Embed(
            title = "Autoreplier | Pembalas Pesan Otomatis",
            description   = "Sintaks:\n"
                            '- Mengatur Autoreplier: `r!autoreplier set "[pesan]" "[respon]"` (Jangan lupa tanda petik)\n'
                            "- Menampilkan daftar kata-kata: `r!autoreplier showall`\n"
                            '- Menghapus item Autoreplier: `r!autoreplier delete "[pesan]"`\n'
                            "- Menghapus semua Autoreplier: `r!autoreplier deleteall`",
            color = ctx.guild.me.color
        )
        await ctx.reply(embed=embed, mention_author=False)

    @autoreplier.command()
    async def set(self, ctx:commands.Context, pesan:str=None, respon:str=None):
        if not pesan and respon == None:
            await ctx.send('Masukkan kata atau kalimat yang ingin dijadikan Autoreplier.\nContoh: `r!autoreplier set "assalaamualaikum" "waalaikumussalaam"` (Pastikan menggunakan tanda petik ya!)')
        elif respon == None:
            await ctx.send(f'Masukkan kata/kalimat untuk balasannya.\nContoh: `r!autoreplier set "{pesan}" "[balasan]"`')
        else:
            with open(file="autorepliers.json", mode="r") as read:
                file_json = json.load(read)

            if f"{ctx.guild.id}" not in file_json:
                file_json[f"{ctx.guild.id}"] = {f"{pesan.lower()}":f"{respon.lower()}"}
            elif pesan.lower() in file_json[f"{ctx.guild.id}"]:
                return await ctx.send("Kamu tidak dapat menambahkan dua Autoreplier yang sama!")
            else:
                file_json[f"{ctx.guild.id}"].update({f"{pesan.lower()}":f"{respon.lower()}"})

            with open(file="autorepliers.json", mode="w") as write:
                json.dump(file_json, write, indent=4)

            embed = discord.Embed(
                title = "Berhasil Diatur",
                description = f'Pesan **"{pesan}"** dengan balasan **"{respon}"** berhasil diatur.',
                color = ctx.guild.me.color
            )
            await ctx.send(embed=embed)

    @autoreplier.command()
    async def showall(self, ctx:commands.Context):
        with open(file="autorepliers.json", mode="r") as r:
            json_obj = json.load(r)

        embed = discord.Embed(
            title = "Daftar Kata Autoreplier pada Server Ini",
            color = ctx.guild.me.color
        )

        embed.add_field(name="Pesan",value="\n".join([pesan for pesan in json_obj[f"{ctx.guild.id}"].keys()]), inline=False)
        embed.add_field(name="Balasan",value="\n".join([balasan for balasan in json_obj[f"{ctx.guild.id}"].values()]))

        await ctx.send(embed=embed)

    @autoreplier.command()
    async def delete(self, ctx:commands.Context, *, pesan:str=None):
        if not pesan:
            return await ctx.reply("Masukkan pesan Autoreplier yang ingin kamu hapus.")

        with open(file="autorepliers.json", mode="r") as baca:
            json_object = json.load(baca)

        try:
            json_object[f"{ctx.guild.id}"].pop(pesan.lower())

            with open(file="autorepliers.json", mode="w") as tulis:
                json.dump(json_object, tulis, indent=4)

            embed = discord.Embed(title="Berhasil Dihapus",description=f'Berhasil menghapus kata **"{pesan.lower()}"** dari Autoreplier.',color=ctx.guild.me.color)
            await ctx.send(embed=embed)
        except KeyError:
            await ctx.reply(f"Tidak ditemukan Autoreplier `{pesan.lower()}`!\nSilahkan lihat daftar Autoreplier yang tersedia dengan command `r!autoreplier showall`")

    @autoreplier.command()
    async def deleteall(self, ctx:commands.Context):
        with open(file="autorepliers.json", mode="r") as r:
            json_obj = json.load(r)

        embed = discord.Embed(
            title = "Konfirmasi Penghapusan",
            description = "Apakah kamu yakin untuk menhapus semua Autoreplier? Aksi ini tidak dapat dipulihkan!",
            color = 0xffff00
        )
        embed.set_footer(text="Balas 'ya' atau 'tidak' | Timeout dalam 10 detik")
        pesan_awal = await ctx.reply(embed=embed)

        def check(m:discord.Message):
            return m.content.lower() in ["ya", "tidak"] and m.channel == ctx.channel

        try:
            msg = await self.client.wait_for("message", check=check, timeout=10)
            if msg.content.lower() == "ya":
                await pesan_awal.delete()
                json_obj.pop(f"{ctx.guild.id}")

                with open(file="autorepliers.json", mode="w") as nulis:
                    json.dump(json_obj, nulis, indent=4)

                embed = discord.Embed(title="Berhasil Dihapus",description="Semua Autoreplier untuk server ini dihapus.",color=ctx.guild.me.color)
                await ctx.send(embed=embed)
            elif msg.content.lower() == "tidak":
                await pesan_awal.delete()

                embed = discord.Embed(title="Batal Dihapus",description="Semua Autoreplier pada server ini batal dihapus.",color=ctx.guild.me.color)
                await ctx.send(embed=embed)
        except asyncio.TimeoutError:
            await pesan_awal.delete()

            await ctx.send("Batal dihapus karena tidak ada jawaban setelah 10 detik ditanya.")

    @autoreplier.error
    async def on_autoreplier_error(self, ctx:commands.Context, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")

    @commands.Cog.listener()
    async def on_message(self, message:Message):
        with open(file="autorepliers.json", mode="r") as baca:
            json_obj = json.load(baca)

        try:
            if message.content.lower() in json_obj[f"{message.guild.id}"].keys():
                return await message.channel.send(json_obj[f"{message.guild.id}"][f"{message.content.lower()}"])
        except KeyError:
            pass

def setup(client):
    client.add_cog(Autoreplier(client))