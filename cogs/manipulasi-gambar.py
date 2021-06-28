import discord, os, requests
from discord.ext import commands
from PIL import Image, ImageEnhance

class ImageManipulations(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def resize(self, ctx, lebardantinggi:str=None):
        try:
            attachment = ctx.message.attachments[0]
            link_foto = attachment.url
        except:
            return await ctx.send("❌ **Tidak terdeteksi adanya gambar yang diunggah!** Coba lagi mengeksekusi command ini dengan membawa foto atau gambar!")

        if not lebardantinggi:
            return await ctx.send("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan lebar dan tinggi gambar!\nContoh: `r!resize 3280x3280`")

        async with ctx.typing():
            try:
                download = requests.get(link_foto)

                if link_foto.endswith(".gif"):
                    format = "gambar.gif"
                else:
                    format = "gambar.png"

                file = open(format, "wb")
                file.write(download.content)
                file.close()

                gambar = Image.open(format)
                #bikin argumen jadi tuple
                mengtapel = lebardantinggi.replace("x", ", ")
                mengtapel2 = tuple(map(int, mengtapel.split(', ')))
                gambar_baru = gambar.resize(mengtapel2)
                if format.endswith(".gif"):
                    nama_baru = "gabar-baru.gif"
                elif format.endswith(".png"):
                    nama_baru = "gabar-baru.png"
                gambar_baru.save(nama_baru)

                await ctx.send(file=discord.File(nama_baru))
                os.remove(nama_baru)
                os.remove(format)
            except:
                await ctx.send("❌ Maaf, terjadi error saat sedang memproses...")

    @commands.command()
    async def rotate(self, ctx, derajat:int=None):
        try:
            attachment = ctx.message.attachments[0]
            link_foto = attachment.url
        except:
            return await ctx.send("❌ **Tidak terdeteksi adanya gambar yang diunggah!** Coba lagi mengeksekusi command ini dengan membawa foto atau gambar!")

        if not derajat:
            return await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan derajat putaran!\nContoh: `r!rotate 90`")

        async with ctx.typing():
            try:
                download = requests.get(link_foto)
                file = open("rotate.png", "wb")
                file.write(download.content)
                file.close()

                gambar = Image.open("rotate.png")
                putar = gambar.rotate(derajat)
                putar.save(f"rotate-{derajat}.png")

                await ctx.send(file=discord.File(f"rotate-{derajat}.png"))

                os.remove("rotate.png")
                os.remove(f"rotate-{derajat}.png")
            except:
                await ctx.send("❌ Maaf, terjadi error...")

    @commands.command()
    async def flip(self, ctx, mode:str=None):
        try:
            attachment = ctx.message.attachments[0]
            link_foto = attachment.url
        except:
            if not mode:
                return await ctx.send("Mode gambar yang valid:\n1. `FLIP_LEFT_RIGHT` flip kiri-kanan\n2. `FLIP_TOP_BOTTOM` flip atas-bawah\n3. `ROTATE_90` memutar gambar 90°\n4. `ROTATE_180` memutar gambar 180°\n5. `ROTATE_270` memutar gambar 270°\n6. `TRANSPOSE` mengubah urutan gambar\n7. `TRANSVERSE` melintangkan gambar\n\nKetik dengan cara `r!flip mdoe1` atau `mode2` dan seterusnya.")
            else:
                return await ctx.send("❌ **Tidak terdeteksi adanya gambar yang diunggah!** Coba lagi mengeksekusi command ini dengan membawa foto atau gambar!")

        if not mode:
            return await ctx.send("Mode gambar yang valid:\n1. `FLIP_LEFT_RIGHT` flip kiri-kanan\n2. `FLIP_TOP_BOTTOM` flip atas-bawah\n3. `ROTATE_90` memutar gambar 90°\n4. `ROTATE_180` memutar gambar 180°\n5. `ROTATE_270` memutar gambar 270°\n6. `TRANSPOSE` mengubah urutan gambar\n7. `TRANSVERSE` melintangkan gambar\n\nKetik dengan cara `r!flip mdoe1` atau `mode2` dan seterusnya.")
        
        async with ctx.typing():
            try:
                def donlot_gambar():
                    download = requests.get(link_foto)
                    file = open("flip.png", "wb")
                    file.write(download.content)
                    file.close()

                if mode.lower() == "mode1":
                    donlot_gambar()

                    gambar = Image.open("flip.png")
                    flip = gambar.transpose(Image.FLIP_LEFT_RIGHT)
                    flip.save("flipped.png")

                    await ctx.send(file=discord.File("flipped.png"))
                elif mode.lower() == "mode2":
                    donlot_gambar()

                    gambar = Image.open("flip.png")
                    flip = gambar.transpose(Image.FLIP_TOP_BOTTOM)
                    flip.save("flipped.png")

                    await ctx.send(file=discord.File("flipped.png"))
                elif mode.lower() == "mode3":
                    donlot_gambar()

                    gambar = Image.open("flip.png")
                    flip = gambar.transpose(Image.ROTATE_90)
                    flip.save("flipped.png")

                    await ctx.send(file=discord.File("flipped.png"))
                elif mode.lower() == "mode4":
                    donlot_gambar()

                    gambar = Image.open("flip.png")
                    flip = gambar.transpose(Image.ROTATE_180)
                    flip.save("flipped.png")

                    await ctx.send(file=discord.File("flipped.png"))
                elif mode.lower() == "mode5":
                    donlot_gambar()

                    gambar = Image.open("flip.png")
                    flip = gambar.transpose(Image.ROTATE_270)
                    flip.save("flipped.png")

                    await ctx.send(file=discord.File("flipped.png"))
                elif mode.lower() == "mode6":
                    donlot_gambar()

                    gambar = Image.open("flip.png")
                    flip = gambar.transpose(Image.TRANSPOSE)
                    flip.save("flipped.png")

                    await ctx.send(file=discord.File("flipped.png"))
                elif mode.lower() == "mode7":
                    donlot_gambar()

                    gambar = Image.open("flip.png")
                    flip = gambar.transpose(Image.TRANSVERSE)
                    flip.save("flipped.png")

                    await ctx.send(file=discord.File("flipped.png"))
                os.remove("flip.png")
                os.remove("flipped.png")
            except:
                ctx.send("❌ Terjadi kesalahan...")

    @commands.command(aliases=["kontras"])
    async def contrast(self, ctx, intensitas:float=None):
        try:
            attachment = ctx.message.attachments[0]
            link_foto = attachment.url
        except:
            if not intensitas:
                return await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Upload foto dan tuliskan intensitas kontrasnya!\nContoh: `r!kontras 1.5`")
            else:
                return await ctx.send("❌ **Tidak terdeteksi adanya gambar yang diunggah!** Coba lagi mengeksekusi command ini dengan membawa foto atau gambar!")

        if not intensitas:
            return await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Tuliskan intensitas kontrasnya!\nContoh: `r!kontras 1.5`")

        try:
            async with ctx.typing():
                download = requests.get(link_foto)
                file = open("contrast.png", "wb")
                file.write(download.content)
                file.close()

                gambar = Image.open("contrast.png")
                edit = ImageEnhance.Contrast(gambar)
                edit.enhance(float(intensitas)).save("contrast-edited.png")

                await ctx.send(file=discord.File("contrast-edited.png"))

                os.remove("contrast.png")
                os.remove("contrast-edited.png")
        except:
            await ctx.send("❌ Terjadi error...")

    @commands.command(aliases=["editwarna"])
    async def coloredit(self, ctx, intensitas:float=None):
        try:
            attachment = ctx.message.attachments[0]
            link_foto = attachment.url
        except:
            if not intensitas:
                return await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Upload foto dan tuliskan intensitas warnanya!\nContoh: `r!editwarna 1.5`")
            else:
                return await ctx.send("❌ **Tidak terdeteksi adanya gambar yang diunggah!** Coba lagi mengeksekusi command ini dengan membawa foto atau gambar!")

        if not intensitas:
            return await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Tuliskan intensitas warnanya!\nContoh: `r!editwarna 1.5`")

        try:
            async with ctx.typing():
                download = requests.get(link_foto)
                file = open("color-edit.png", "wb")
                file.write(download.content)
                file.close()

                gambar = Image.open("color-edit.png")
                edit = ImageEnhance.Color(gambar)
                edit.enhance(float(intensitas)).save("color-edited.png")

                await ctx.send(file=discord.File("color-edited.png"))

                os.remove("color-edit.png")
                os.remove("color-edited.png")
        except:
            await ctx.send("❌ Terjadi error...")

def setup(client):
    client.add_cog(ImageManipulations(client))