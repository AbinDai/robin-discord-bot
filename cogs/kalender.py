import discord, calendar, datetime, DiscordUtils
from discord.ext import commands

class Kalender(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["calendar","calender"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kalender(self, ctx, tahun:int=None, bulan:str=None):
        tanggal = datetime.datetime.now().strftime("%d")
        buulan = datetime.datetime.now().strftime("%m")
        taahun = datetime.datetime.now().strftime("%Y")

        if not tahun and bulan == None:
            embed = discord.Embed(
                title = "Penggunaan Command `kalender` yang benar",
                description = "`r!kalender [tahun (angka)]` kalau cuma mau melihat 1 tahun kalender.\n"
                              "`r!kalender [tahun (angka)] [bulan (angka/huruf)]` kalau mau melihat 1 bulan kalender.\n"
                              "\n"
                              "**Contoh:**\n"
                              "`r!kalender 2021` untuk melihat kalender tahun 2021.\n"
                              "`r!kalender 2021 april` untuk melihat kalender bulan April di tahun 2021\n"
                              "`r!kalender 2021 4` sama aja, tapi kali ini pake angka.",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            embed.set_footer(text=f"Di-Request oleh {ctx.author.name}",icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
        elif not bulan:
            try:
                embed1 = discord.Embed(
                    title = f"Kalender Januari {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,1)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed1.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed2 = discord.Embed(
                    title = f"Kalender Februari {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,2)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed2.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed3 = discord.Embed(
                    title = f"Kalender Maret {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,3)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed3.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed4 = discord.Embed(
                    title = f"Kalender April {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,4)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed4.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed5 = discord.Embed(
                    title = f"Kalender Mei {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,5)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed5.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed6 = discord.Embed(
                    title = f"Kalender Juni {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,6)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed6.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed7 = discord.Embed(
                    title = f"Kalender Juli {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,7)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed7.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed8 = discord.Embed(
                    title = f"Kalender Agustus {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,8)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed8.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed9 = discord.Embed(
                    title = f"Kalender September {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,9)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed9.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed10 = discord.Embed(
                    title = f"Kalender Oktober {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,10)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed10.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed11 = discord.Embed(
                    title = f"Kalender November {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,11)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed11.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                embed12 = discord.Embed(
                    title = f"Kalender Desember {tahun}",
                    description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,12)}\n```",
                    color = ctx.guild.get_member(self.client.user.id).color
                )
                embed12.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")

                paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
                paginator.add_reaction("◀", "back")
                paginator.add_reaction("▶", "next")
                embed_embed = [
                    embed1,
                    embed2,
                    embed3,
                    embed4,
                    embed5,
                    embed6,
                    embed7,
                    embed8,
                    embed9,
                    embed10,
                    embed11,
                    embed12
                ]
                await paginator.run(embed_embed)
            except:
                await ctx.reply("❌ **Tahun yang kamu masukkan tidak valid!**")
        else:
            try:
                if bulan.lower() == "januari" or bulan.lower() == "january" or bulan == "1":
                    embed = discord.Embed(
                        title = f"Kalender Januari {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,1)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "februari" or bulan.lower() == "february" or bulan == "2":
                    embed = discord.Embed(
                        title = f"Kalender Februari {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,2)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "maret" or bulan.lower() == "march" or bulan == "3":
                    embed = discord.Embed(
                        title = f"Kalender Maret {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,3)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "april" or bulan == "4":
                    embed = discord.Embed(
                        title = f"Kalender April {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,4)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "mei" or bulan.lower() == "may" or bulan == "5":
                    embed = discord.Embed(
                        title = f"Kalender Mei {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,5)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "juni" or bulan.lower() == "june" or bulan == "6":
                    embed = discord.Embed(
                        title = f"Kalender Juni {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,6)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "juli" or bulan.lower() == "july" or bulan == "7":
                    embed = discord.Embed(
                        title = f"Kalender Juli {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,7)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "agustus" or bulan.lower() == "august" or bulan == "8":
                    embed = discord.Embed(
                        title = f"Kalender Agustus {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,8)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "september" or bulan == "9":
                    embed = discord.Embed(
                        title = f"Kalender September {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,9)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "oktober" or bulan.lower() == "october" or bulan == "10":
                    embed = discord.Embed(
                        title = f"Kalender Oktober {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,10)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "november" or bulan == "11":
                    embed = discord.Embed(
                        title = f"Kalender November {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,11)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
                elif bulan.lower() == "desember" or bulan.lower() == "december" or bulan == "12":
                    embed = discord.Embed(
                        title = f"Kalender Desember {tahun}",
                        description = f"```py\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(tahun,12)}\n```",
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    embed.set_footer(text=f"Hari Ini: {tanggal}/{buulan}/{taahun}")
                    await ctx.send(embed=embed)
            except:
                await ctx.reply("❌ **Input yang kamu masukkan tidak valid!**")
        

def setup(client):
    client.add_cog(Kalender(client))
