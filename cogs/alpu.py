import discord, random
from discord.ext import commands

class Alpu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['alfu', 'alpu', 'alpish', 'alfish', 'alpis', 'alfi', 'alpush', 'alpipalinggantengdiduniaini'])
    async def alpi(self, ctx): #<---- awokawokoa mampus nama command nya 'alpi' wkwkwwk
        embed = discord.Embed(
            title = 'Si Alpu',
            description = 'Alfiza Lizuardy Santoso',
            colour = ctx.guild.get_member(self.client.user.id).color
        )
        list_foto_alpi = [
            'https://cdn.discordapp.com/attachments/783036987497513041/817566902095839232/IMG_20210306_081833_328.jpg',
            'https://cdn.discordapp.com/attachments/783036987497513041/817565653560066049/awkoakw.jpeg',
            'https://cdn.discordapp.com/attachments/783106350522695721/817572998226640957/IMG_20210306_084240_649.jpg',
            'https://cdn.discordapp.com/attachments/783036987497513041/817575374414151691/116324331_628639204431491_6761345164964904967_o.png',
            'https://cdn.discordapp.com/attachments/783036987497513041/817580168452898816/magik.png',
            'https://cdn.discordapp.com/attachments/783036987497513041/818454632116387880/IMG-20210224-WA0033.png',
            'https://cdn.discordapp.com/attachments/794253113891749899/820144168306999296/IMG_20210313_105938_202.jpg',
            'https://cdn.discordapp.com/attachments/794253113891749899/820226325486239754/IMG-20210313-WA0040.jpg',
            'https://media.discordapp.net/attachments/765093717328658452/822153958091915324/magik.png'
        ]
        embed.set_image(url=f'{random.choice(list_foto_alpi)}')
        embed.set_footer(text=f'Di-Request oleh {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Alpu(client))
