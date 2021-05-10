import discord, time, datetime, platform, random
from discord.ext import commands

class About(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("about.py siap")

    @commands.command(aliases=['tentangbot', 'aboutme', 'aboutbot', 'tentang', 'info', 'infobot'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def about(self, ctx):
        deftar_foto_random = [
            f"{self.client.user.avatar_url_as(format='png',size=4096)}",
            f"{self.client.user.avatar_url_as(format='png',size=4096)}",
            f"{self.client.user.avatar_url_as(format='png',size=4096)}",
            f"{self.client.user.avatar_url_as(format='png',size=4096)}",
            f"{self.client.user.avatar_url_as(format='png',size=4096)}",
            "https://media1.tenor.com/images/8c409e6f39acc1bd796e8031747f19ad/tenor.gif?itemid=17029825"
        ]
        
        embed = discord.Embed(
            title = 'Tentang Bot',
            colour = ctx.guild.get_member(self.client.user.id).color
        )
        current_time = time.time()
        difference = int(round(current_time))
        text = str(datetime.timedelta(seconds=difference))
        embed.set_thumbnail(url=random.choice(deftar_foto_random))
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Bot:', value=self.client.user)
        embed.add_field(name='Dibuat:', value='27 Februari 2021')
        embed.add_field(name='Pengembang:', value='Abin#4405')
        embed.add_field(name='Library:', value='discord.py')
        embed.add_field(name='Bahasa Pemrograman:', value='Python')
        embed.add_field(name='Ping Bot:', value=f'{round(self.client.latency * 1000)}ms')
        embed.add_field(name='Versi Library:', value=f'v{discord.__version__}')
        embed.add_field(name='Versi Python:', value=f'v{platform.python_version()}')
        embed.add_field(name='Jumlah Server:', value=len(self.client.guilds))
        embed.add_field(name="⠀", value="[Link Invite](https://top.gg/bot/805876219647361053/invite)\n"
                                        "[Vote Disini!](https://top.gg/bot/805876219647361053/vote)\n"
                                        "[Repositori GitHub](https://github.com/AbinDai/robin-discord-bot/)\n"
                                        "[Help Server](https://discord.gg/rZqsvrMdwR)", inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(About(client))
