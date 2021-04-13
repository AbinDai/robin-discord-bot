#impor
import discord, random
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print('kategori fun, siap ngebut!')
    
    #perintah 8ball
    @commands.command(aliases=['8ball', '8b'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _8ball(self, ctx):
        responses = [
            'OH YOIIII AWOKAWOKAWOK  ',
            'Yap, benar sekali. <:stalin_MANTAP:799103589078401075> ',
            'Gatau ¯\_(ツ)_/¯ ',
            'Sejak kapan jir? <:STALIN_ADUH:799103192360812594> ',
            'Gatau gw. Cari aja sndiri jawabannya. <:muka_datar:814440461166706708> ',
            'Napa lu nanyain gw yang itu? Gaada yg lain kah apa? <:thor_taapo:799097046463545374> ',
            'Gak. <:muka_datar:814440461166706708> ',
            'Kagak deh kykny. <:muka_datar:814440461166706708> ',
            'Hmm, w rasa tidak. <:muka_datar:814440461166706708> ',
            'TIDAK!!! <:thor_taapo:799097046463545374> ',
            'Tanya aja nnti <:thor_taapo:799097046463545374> ',
            'Au ah mls. <:zoro_tidur:799106689835204609> '
        ]
        await ctx.reply(f'{random.choice(responses)}')

    #command keqing
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def keqing(self, ctx):
        embed = discord.Embed(
            title = 'KAMU STRES? INI TEKS KEQING WANGY UNTUKMU!!!',
            description = 'KEQING........... KEQING KEQING KKKKKKEEEEEEEQQQQQQQQIIIIIINNNNNNGGGG AAAAAAAAAAAAAAAAAGH AAAAAAAAAAAAAAAAAAAAAAAGH <3 <3 <3 <3 WANGI WANGI WANGI WANGI HU HA HU HA HU HA, aaaah baunya keqing wangi aku mau nyiumin aroma wanginya keqing AAAAAAAAH ~~ rambutnya.... aaah rambutnya juga pengen aku elus-elus ~~~~~ AAAAAH keqing keluar pertama kali juga manis <3 <3 <3 dia pake baju itu juga manis banget AAAAAAAAH KEQING LUCCUUUUUUUUUUUUUUU............ GUA BAKAL BAKAR DUIT 12 JUTA RUPIAH BUAT KEQING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAGH\napa ? Keqing itu gak nyata ? Cuma karakter 2 dimensi katamu ? nggak, ngak ngak ngak ngak NGAAAAAAAAK GUA GAK PERCAYA ITU DIA NYATA NGAAAAAAAAAAAAAAAAAK MiHoYo BANGSAAAAAT !! GUA GAK PEDULI SAMA KENYATAAN POKOKNYA GAK PEDULI.\nKeqing ngeliat gw ... Keqing di HP ngeliatin gw Keqing... kamu percaya sama aku ? aaaaaaaaaaah syukur Keqing gak malu merelakan aku aaaaaah <3 <3 <3 YEAAAAAAAAAAAH GUA MASIH PUNYA KEQING, SENDIRI PUN NGGAK SAMA AAAAAAAAAAAAAAH FISCHL, JEAN MONA KLEE QIQI KIRIMKANLAH CINTAKU PADA KEQING KIRIMKAN KE MiHoYo AAAAAAAAH',
            color = 0x927794
        )
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
        embed.set_image(url='https://cdn.mee6.xyz/guild-images/783016541712154674/9b39d0d164bfcd1a11e4469cb74bbce3b176b7278d5202de5d6c4333e9b77798.png')
        await ctx.send(embed=embed)

    #command tes
    @commands.command(aliases=['test'])
    async def tes(self, ctx):
        await ctx.reply('Tes Anda berhasil! :thumbsup:')

    #command geh
    @commands.command(aliases=['gay', 'gei', 'gae'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def geh(self, ctx, member: discord.Member = None):
        daftar_gambar_geh = [
            'https://media1.tenor.com/images/9a5c2ee8a2a41e70215fbc8fa1ffc3f3/tenor.gif',
            'https://media1.tenor.com/images/667a5fd3839c175e7726c4757c65348a/tenor.gif',
            'https://media1.tenor.com/images/923f96db97c09439d45e98c127dda89f/tenor.gif',
            'https://media1.tenor.com/images/bdd44dfc7dd671805acd9781b0c6604a/tenor.gif',
            'https://cdn.discordapp.com/attachments/818830541998522369/819040478040424448/FB_IMG_1615344844517.jpg',
            'https://cdn.discordapp.com/attachments/783036987497513041/819134151596572712/FB_IMG_1615366788847.jpg'
        ]
        
        if not member:
            embed = discord.Embed(
                title = "Why are you geh?",
                description = "Kenapa kamu *geh*?",
                color = ctx.guild.get_member(self.client.user.id).color #hus bacot
            )
            embed.set_image(url=f'{random.choice(daftar_gambar_geh)}')
            embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title = f'{member.display_name} geh',
                description = 'Kenapa kamu *geh*?',
                color = ctx.guild.get_member(self.client.user.id).color
            )
            embed.set_image(url=f'{random.choice(daftar_gambar_geh)}')
            embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    #command kaori
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kaori(self, ctx):
        daftar_gif = [
            'https://media1.tenor.com/images/527a2e762f47bc4fe3cd31e4027f5593/tenor.gif', #1 DONE
            'https://media1.tenor.com/images/d977523a46290aeb8bfbd1d87c0248d9/tenor.gif', #2 DONE
            'https://media1.tenor.com/images/c6085750005a4202122c0fcd13ba662e/tenor.gif', #3 DONE
            'https://media1.tenor.com/images/75e0bab932595279e50c59e70a2affc4/tenor.gif', #4 DONE
            'https://media1.tenor.com/images/56768d3578bbc20f4a51cfc0e687986d/tenor.gif', #5 DONE
            'https://media1.tenor.com/images/31cb0659eeb8d64f96e45763ff46ba4b/tenor.gif', #6 DONE
            'https://media1.tenor.com/images/ba10e283f466ea58aea15dec1e5b8ae3/tenor.gif', #7 DONE
            'https://media1.tenor.com/images/45fd04d4e98273a0602b9acd797af497/tenor.gif', #8 DONE
            'https://media1.tenor.com/images/ce2718f0fa1238631cebabcaf5a93c3f/tenor.gif', #9 DONE
            'https://media1.tenor.com/images/bcec7d15272ce53457aadcf0e8776431/tenor.gif', #10 DONE
            'https://media1.tenor.com/images/b1fc1f707c41beb14dc2d2a9f7b4940b/tenor.gif', #11 DONE
            'https://media1.tenor.com/images/b1fc1f707c41beb14dc2d2a9f7b4940b/tenor.gif' #12 DONE
        ]
        embed = discord.Embed(
            title = 'Kaori Miyazono',
            colour = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=f'{random.choice(daftar_gif)}')
        await ctx.send(embed=embed)

    #command thor taapo
    @commands.command(aliases=['thortaapo', 'taapo'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tabok(self, ctx):
        daftar_gambar_taapo = [
            'https://media.discordapp.net/attachments/765093566954864650/802886551288807484/782787905344241734.png',
            'https://cdn.discordapp.com/attachments/783103285863120906/816121316272111666/799097046463545374.png'
        ]
        embed = discord.Embed(
            title = 'Ta\'apo mayi yi\'o aa',
            description = 'W tabok lu',
            color = ctx.guild.get_member(self.client.user.id).color
        )    
        embed.set_image(url=f'{random.choice(daftar_gambar_taapo)}')
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #commmand bonk
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bonk(self, ctx):
        embed = discord.Embed(
            title = 'BONK',
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/783036987497513041/816147402527342592/images_-_2021-03-02T111815.184.jpeg')
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #command saygoodbye
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def saygoodbye(self, ctx):
        embed = discord.Embed(
            title = 'SAY GOODBYE!',
            colour = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_image(url='https://media1.tenor.com/images/5948eb653169fb1884ec617a59a68a88/tenor.gif')
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))
