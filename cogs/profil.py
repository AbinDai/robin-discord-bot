import discord, requests, os
from discord.ext import commands
from dominant_color_detection import detect_colors

class Profil(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #command avatar
    @commands.command(aliases=['avt', 'pfp', 'pp'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self, ctx, *, member: discord.Member=None):
        member = ctx.author if not member else member

        response = requests.get(member.avatar_url_as(format="png",size=4096))
        file = open("pp.png", "wb")
        file.write(response.content)
        file.close()
        
        #kita coba detect warna yg pling dominan di foto profilnya
        #kemudian kita pake buat warna embed
        colors, ratios = detect_colors("pp.png", 3)
        warna = colors[0][1:]
        warna_akhir = int(warna, 16)

        os.remove("pp.png")

        embed = discord.Embed(
            title = f'Berikut ini avatarnya si {member.name}:',
            description = f'Butuh link dalam format lain?\n[jpeg]({member.avatar_url_as(format="jpeg", size=4096)}) | [jpg]({member.avatar_url_as(format="jpg", size=4096)}) | [webp]({member.avatar_url_as(format="webp", size=4096)})',
            colour = warna_akhir
        )
        embed.set_image(url=f'{member.avatar_url_as(format=None, static_format="png", size=4096)}')
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #command serverinfo
    @commands.command(aliases=['infoserver'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            title = "Informasi Server",
            color = ctx.guild.me.color
        )
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Nama", value=ctx.guild.name)
        embed.add_field(name="ID", value=ctx.guild.id)

        dibuat_pada = ctx.guild.created_at
        tanggal, bulan, tahun = dibuat_pada.strftime("%d"), dibuat_pada.strftime("%m"), dibuat_pada.strftime("%Y")
        jam, menit, detik = dibuat_pada.strftime("%H"), dibuat_pada.strftime("%M"), dibuat_pada.strftime("%S")
        embed.add_field(name="Dibuat pada", value=f"{tanggal}/{bulan}/{tahun} {jam}:{menit}:{detik}")

        if ctx.guild.description is not None:
            embed.add_field(name="Deskripsi", value=ctx.guild.description, inline=False)
        else:
            embed.add_field(name="Deskripsi", value="Tidak ada", inline=False)

        embed.add_field(name="Jumlah Text Channel", value=len(ctx.guild.text_channels))
        embed.add_field(name="Jumlah Voice Channel", value=len(ctx.guild.voice_channels))
        if ctx.guild.owner is not None:
            embed.add_field(name="Pemilik", value=ctx.guild.owner)
        else:
            embed.add_field(name="Pemilik", value=f"Tidak ada")

        embed.add_field(name="Jumlah Emoji", value=len(ctx.guild.emojis))
        if ctx.guild.region is not None:
            embed.add_field(name="Negara", value=ctx.guild.region)
        else:
            embed.add_field(name="Negara", value="Tidak ada")

        if ctx.guild.afk_channel is not None:
            embed.add_field(name="Channel AFK", value=ctx.guild.afk_channel.mention)
        else:
            embed.add_field(name="Channel AFK", value="Tidak ada")

        try:
            if ctx.guild.system_channel is not None:
                embed.add_field(name="Channel Sistem", value=ctx.guild.system_channel.mention)
            else:
                embed.add_field(name="Channel Sistem", value="Tidak ada")
        except:
            embed.add_field(name="Channel Sistem", value="Tidak dapat memuat info")

        if ctx.guild.rules_channel is not None:
            embed.add_field(name="Channel Aturan", value=ctx.guild.rules_channel.mention)
        else:
            embed.add_field(name="Channel Aturan", value="Tidak ada")
        try:
            if ctx.guild.public_updates_channel is not None:
                embed.add_field(name="Channel Update", value=ctx.guild.public_updates_channel.mention)
            else:
                embed.add_field(name="Channel Update", value="Tidak ada")
        except:
            embed.add_field(name="Channel Update", value="Tidak dapat memuat info")

        embed.add_field(name=f"Jumlah Emoji ({len(await ctx.guild.fetch_emojis())})", value=' '.join([str(emoji) for emoji in await ctx.guild.fetch_emojis()]), inline=False)

        embed.add_field(name=f"Jumlah Role ({len(await ctx.guild.fetch_roles())})", value=' '.join([role.mention for role in await ctx.guild.fetch_roles()]), inline=False)

        embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    #command servericon
    @commands.command(aliases=['fotoserver, serverpicture, serveravatar'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servericon(self, ctx):
        response = requests.get(ctx.guild.icon_url_as(format="png",size=4096))
        file = open("servericon.png", "wb")
        file.write(response.content)
        file.close()
        
        #kita coba detect warna yg pling dominan di foto server-nya
        #kemudian kita pake buat warna embed
        colors, ratios = detect_colors("servericon.png", 3)
        warna = colors[0][1:]
        warna_akhir = int(warna, 16)

        os.remove("servericon.png")

        embed = discord.Embed(
            title = f'Berikut foto server {ctx.guild.name}:',
            description = f'Butuh link dalam format lain?\n[jpeg]({ctx.guild.icon_url_as(format="jpeg", size=4096)}) | [jpg]({ctx.guild.icon_url_as(format="jpg", size=4096)}) | [webp]({ctx.guild.icon_url_as(format="webp", size=4096)})',
            colour = warna_akhir
        )
        embed.set_image(url=f'{ctx.guild.icon_url_as(format=None, static_format="png", size=4096)}')
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)

    #command userinfo
    @commands.command(aliases=['infopengguna, infoorang'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        embed = discord.Embed(
            title = "Informasi User",
            color = member.color
        )
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url_as(format=None, static_format="png", size=4096))

        embed.add_field(name="Username", value=member.name)
        embed.add_field(name="Tag", value=f"#{member.discriminator}")
        embed.add_field(name="Nama di Server Ini", value=member.display_name)

        embed.add_field(name="ID", value=member.id)
        if member.bot is True:
            embed.add_field(name="Adalah Bot?", value=member.bot)
        else:
            embed.add_field(name="Adalah Bot?", value="Bukan")

        if member.system is True:
            embed.add_field(name="Akun Sistem?", value=member.system)
        else:
            embed.add_field(name="Akun Sistem?", value="Bukan")

        dibuat_pada = member.created_at
        tanggal, bulan, tahun = dibuat_pada.strftime("%d"), dibuat_pada.strftime("%m"), dibuat_pada.strftime("%Y")
        jam, menit, detik = dibuat_pada.strftime("%H"), dibuat_pada.strftime("%M"), dibuat_pada.strftime("%S")
        zonawaktu, ZONAWAKTU = dibuat_pada.strftime("%z"), dibuat_pada.strftime("%Z")
        embed.add_field(name="Dibuat pada", value=f"{tanggal}/{bulan}/{tahun} {jam}:{menit}:{detik} {ZONAWAKTU} {zonawaktu}")

        dibuat_pada = member.joined_at
        tanggal, bulan, tahun = dibuat_pada.strftime("%d"), dibuat_pada.strftime("%m"), dibuat_pada.strftime("%Y")
        jam, menit, detik = dibuat_pada.strftime("%H"), dibuat_pada.strftime("%M"), dibuat_pada.strftime("%S")
        zonawaktu, ZONAWAKTU = dibuat_pada.strftime("%z"), dibuat_pada.strftime("%Z")
        embed.add_field(name="Bergabung pada", value=f"{tanggal}/{bulan}/{tahun} {jam}:{menit}:{detik} {ZONAWAKTU} {zonawaktu}")

        roles = [role for role in member.roles]
        embed.add_field(name=f'Jumlah Role ({len(roles)})', value=' '.join([role.mention for role in roles]), inline=False)

        embed.add_field(name="Role Teratas", value=member.top_role.mention)
        embed.add_field(name="Warna Nama", value=member.color)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Profil(client))
