import discord, random, asyncio
from discord.ext import commands

class TebakAngka(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tebakangka(self, ctx, angkaAwal:int=None, angkaAkhir:int=None):
        angkaAwal = 1 if not angkaAwal else angkaAwal
        angkaAkhir = 10 if not angkaAkhir else angkaAkhir

        pesan_awal = await ctx.send(f"Oke, ambil angka dari {angkaAwal} sampai {angkaAkhir}, nanti akan kutebak.\nJawab `sudah` kalau sudah. (Timeout dalam 10 detik).", delete_after=10)
        
        try:
            msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=10)
            if msg.content.lower() == "sudah":
                await pesan_awal.delete()

                pesan_menebak = await ctx.send("Oke, akan kutebak...")
                await asyncio.sleep(3)

                acak_angkanya = random.randint(angkaAwal, angkaAkhir)

                await pesan_menebak.delete()
                pesan_konfirmasi = await ctx.send(f"Saya menebak **{acak_angkanya}**. `Benar` atau `salah`?", delete_after=15)

                try:
                    mesej = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=15)
                    if mesej.content.lower() == "benar":
                        await pesan_konfirmasi.delete()
                        await ctx.send("Naisu :v main lagi lain kali :v")
                    elif mesej.content.lower() == "salah":
                        await pesan_konfirmasi.delete()
                        await ctx.send("Ah sori :v oke main lagi nanti :v")
                except asyncio.TimeoutError:
                    await ctx.send("Hadeh lama bgt jawab `benar` ato `salah`nya. Main lagi nanti.")
        except asyncio.TimeoutError:
            await ctx.send("Lama bgt balasnya, gajadi ah.")

def setup(client):
    client.add_cog(TebakAngka(client))