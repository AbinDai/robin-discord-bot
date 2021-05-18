import discord, requests, os
from discord.ext import commands
from dominant_color_detection import detect_colors

class Profil(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('kategori profil, siap ngegas!')
    
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
            title = f'Berikut ini avatarnya si {member.display_name}:',
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
        title = 'Informasi Server',
        colour = ctx.guild.get_member(self.client.user.id).color
        )
        nama_server = ctx.guild.name
        id_server = ctx.guild.id
        negara_server = ctx.guild.region
        jumlah_member = ctx.guild.member_count
        level_verifikasi = ctx.guild.verification_level
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Server:', value=f'{nama_server}', inline=False)
        embed.add_field(name='ID Server:', value=f'{id_server}', inline=False)
        embed.add_field(name='Dibuat Pada:', value=f'{ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}', inline=False)
        embed.add_field(name='Negara:', value=f'{negara_server}', inline=False)
        embed.add_field(name='Jumlah Member:', value=f'{jumlah_member}', inline=False)
        embed.add_field(name='Level Verifikasi:', value=f'{level_verifikasi}', inline=False)
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
        roles = [role for role in member.roles]
        embed = discord.Embed(
            title = 'Informasi Pengguna',
            color = member.color
        )
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama:', value=f'{member}', inline=False)
        embed.add_field(name='Nickname di Server Ini:', value=f'{member.display_name}', inline=False)
        embed.add_field(name='ID:', value=f'{member.id}', inline=False)
        embed.add_field(name='Tanggal Dibuatnya Akun:', value=f'{member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}', inline=False)
        embed.add_field(name='Tanggal Bergabung Dengan Server Ini:', value=f'{member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}', inline=False)
        embed.add_field(name=f'Role: ({len(roles)})', value=' '.join([role.mention for role in roles]), inline=False)
        embed.add_field(name='Role Tertinggi:', value=f'{member.top_role.mention}', inline=False)
        embed.add_field(name='Adalah Bot?', value=f'{member.bot}')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Profil(client))
