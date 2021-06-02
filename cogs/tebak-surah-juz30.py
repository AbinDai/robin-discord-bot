import discord as wahyu, random, asyncio
from discord.ext import commands
from discord import FFmpegPCMAudio

class TebakSurahJuz30(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def tebaksurahjuz30(self, ctx):
        if (ctx.author.voice):
            #masuk vc
            voice = await ctx.author.voice.channel.connect()

            #kirim pesan penanda
            embed = wahyu.Embed(
                title = "Tebak Surah (Edisi Juz 30)",
                description = f"Terhubung ke {ctx.author.voice.channel.mention}\nAkan dimulai dalam 5 detik, siap-siap!",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            await ctx.send(embed=embed)

            #jeda 5 detik
            await asyncio.sleep(5)

            #daftar audio
            audio = [
                "./audio/078-an-naba.mp3",
                "./audio/079-an-naziat.mp3",
                "./audio/080-abasa.mp3",
                "./audio/081-at-takwir.mp3",
                "./audio/082-al-infitar.mp3",
                "./audio/083-al-mutaffifin.mp3",
                "./audio/084-al-inshiqaq.mp3",
                "./audio/085-al-buruj.mp3",
                "./audio/086-at-tariq.mp3",
                "./audio/087-al-ala.mp3",
                "./audio/088-al-ghashiyah.mp3",
                "./audio/089-al-fajr.mp3",
                "./audio/090-al-balad.mp3",
                "./audio/091-ash-shams.mp3",
                "./audio/092-al-lail.mp3",
                "./audio/093-ad-duha.mp3",
                "./audio/094-ash-sharh.mp3",
                "./audio/095-at-tin.mp3",
                "./audio/096-al-alaq.mp3",
                "./audio/097-al-qadr.mp3",
                "./audio/098-al-baiyyinah.mp3",
                "./audio/099-az-zalzalah.mp3",
                "./audio/100-al-adiyat.mp3",
                "./audio/101-al-qariah.mp3",
                "./audio/102-at-takathur.mp3",
                "./audio/103-al-asr.mp3",
                "./audio/104-al-humazah.mp3",
                "./audio/105-al-fil.mp3",
                "./audio/106-quraish.mp3",
                "./audio/107-al-maun.mp3",
                "./audio/108-al-kauthar.mp3",
                "./audio/109-al-kafirun.mp3",
                "./audio/110-an-nasr.mp3",
                "./audio/111-al-masad.mp3",
                "./audio/112-al-ikhlas.mp3",
                "./audio/113-al-falaq.mp3",
                "./audio/114-an-nas.mp3"
            ]

            #acak file audio
            acak = random.choice(audio)

            #putar hasil acakan
            voice.play(FFmpegPCMAudio(acak))

            #kirim pesan menebak
            embed = wahyu.Embed(
                title = "Tebak Surah (Edisi Juz 30) Dimulai",
                description = "Silahkan dengarkan dengan seksama surah yang sedang diputar.\nJika sudah mengetahui jawabannya, langsung jawab dengan menyebutkan nama surah-nya.\n\nJawab `gatau` jika tidak tahu.",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            embed.set_footer(text="Timeout dalam 1 menit 30 detik")
            pesan_kedua = await ctx.send(embed=embed)

            try:
                if acak == "./audio/078-an-naba.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "an-naba", "an-naba'"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah An-Naba'.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah An-Naba'.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/079-an-naziat.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "an-naziat", "an-nazi'at"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah An-Nazi'at.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah An-Nazi'at.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/080-abasa.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "abasa"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Abasa.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Abasa.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/081-at-takwir.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "at-takwir"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah At-Takwir.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Takwir.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/082-al-infitar.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-infitar"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Infitar.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Infitar.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                
                elif acak == "./audio/083-al-mutaffifin.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-mutaffifin"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Mutaffifin.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Mutaffifin.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/084-al-inshiqaq.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-insyiqaq"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Insyiqaq.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Insyiqaq.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/085-al-buruj.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-buruj"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Buruj.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Buruj.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/086-at-tariq.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "at-tariq", "at-thoriq"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah At-Tariq.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah At-Tariq.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/087-al-ala.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-a'la", "al-ala"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-A'la.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-A'la.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/088-al-ghashiyah.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-ghasyiyah"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Ghasyiyah.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Ghasyiyah.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/089-al-fajr.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-fajr"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Fajr.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Fajr.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/090-al-balad.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-balad"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Balad.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Balad.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/091-ash-shams.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "asy-syams"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Asy-Syams.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Asy-Syams.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/092-al-lail.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-lail"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Lail.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Lail.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/093-ad-duha.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "ad-duha"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Ad-Duha.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Ad-Duha.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/094-ash-sharh.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "asy-syarh", "al-insyirah", "al-insiroh"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Insyirah.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Insyirah.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/095-at-tin.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "at-tin"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah At-Tin.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah At-Tin.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/096-al-alaq.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-alaq"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Alaq.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Alaq.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/097-al-qadr.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-qadr"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Qadr.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Qadr.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/098-al-baiyyinah.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-bayyinah"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Bayyinah.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Bayyinah.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/099-az-zalzalah.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "az-zalzalah"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Az-Zalzalah.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Az-Zalzalah.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/100-al-adiyat.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-adiyat"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Adiyat.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Adiyat.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/101-al-qariah.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-qariah", "al-qoriah", "al-qari'ah", "al-qori'ah"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Qari'ah.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Qari'ah.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/102-at-takathur.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "at-takasur"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah At-Takasur.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah At-Takasur.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/103-al-asr.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-asr", "al-'asr"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-'Asr.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-'Asr.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/104-al-humazah.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-humazah"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Humazah.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Humazah.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/105-al-fil.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-fil"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Fil.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Fil.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/106-quraish.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "quraisy"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Quraisy.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Quraisy.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/107-al-maun.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-maun", "al-ma'un"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Ma'un.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Ma'un.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/108-al-kauthar.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-kausar"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Kausar.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Kausar.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                
                elif acak == "./audio/109-al-kafirun.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-kafirun"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Kafirun.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Kafirun.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/110-an-nasr.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "an-nasr"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah An-Nasr.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah An-Nasr.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/111-al-masad.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-massad", "al-lahab"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Lahab.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Lahab.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/112-al-ikhlas.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-ikhlas"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Ikhlas.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Ikhlas.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/113-al-falaq.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "al-falaq"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah Al-Falaq.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah Al-Falaq.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

                elif acak == "./audio/114-an-nas.mp3": #<----
                    def check(msg):                         
                        return msg.content.lower() in ["gatau", "an-nas"] and msg.channel == ctx.channel
                    #                                          ^^^^^^^^^^^
                    msg = await self.client.wait_for("message", check=check, timeout=90)
                    if msg.content.lower() == "gatau":
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Surah yang diputar barusan yaitu Surah An-Nas.\n\nPermainan dihentikan.",
                            color = 0xff0000                                     #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()
                    else:
                        embed = wahyu.Embed(
                            title = "Tebak Surah",
                            description = "Benar!\nSurah tersebut adalah surah An-Nas.\n\nMain lagi? Eksekusi kembali command-nya.",
                            color = 0x00ff00                                  #^^^^^^^^
                        )
                        await ctx.send(embed=embed)
                        await ctx.guild.voice_client.disconnect()

            except asyncio.TimeoutError:
                await pesan_kedua.delete()
                await ctx.guild.voice_client.disconnect()
                embed = wahyu.Embed(
                    title = "Tebak Surah (Edisi Juz 30)",
                    description = "Sudah 1 menit 30 detik tidak ada jawaban.\n\nPermainan dihentikan.",
                    color = 0xff0000
                )
                await ctx.send(embed=embed) 

        else:
            await ctx.reply("Silahkan masuk voice channel terlebih dahulu utk memainkan permainan ini!")
 
def setup(client):
    client.add_cog(TebakSurahJuz30(client))