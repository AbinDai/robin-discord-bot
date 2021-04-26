import discord, time, datetime, platform
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
        embed = discord.Embed(
            title = 'Tentang Bot',
            colour = ctx.guild.get_member(self.client.user.id).color
        )
        current_time = time.time()
        difference = int(round(current_time))
        text = str(datetime.timedelta(seconds=difference))
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Nama Bot:', value=self.client.user)
        embed.add_field(name='Dibuat:', value='27 Februari 2021')
        embed.add_field(name='Pengembang:', value='Abin#4405')
        embed.add_field(name='Library:', value='discord.py')
        embed.add_field(name='Bahasa Pemrograman:', value='Python')
        embed.add_field(name='Ping Bot:', value=f'{round(self.client.latency * 1000)}ms')
        embed.add_field(name='Versi discord.py:', value=f'{discord.__version__}')
        embed.add_field(name='Versi Python:', value=f'{platform.python_version()}')
        embed.add_field(name='Uptime:', value=f'{text}')
        embed.add_field(name='Jumlah Pengguna:', value=f'{len(set(self.client.get_all_members()))}')
        embed.add_field(name='Jumlah Server:', value=f'{len(self.client.guilds)}')
        embed.add_field(name='Asal Anime:', value='One Piece')
        embed.add_field(name="⠀", value="[Link Invite](https://top.gg/bot/805876219647361053/invite)\n"
                                        "[Vote Disini!](https://top.gg/bot/805876219647361053/vote)\n"
                                        "[Repositori GitHub](https://github.com/AbinDai/robin-discord-bot/)\n"
                                        "[Help Server](https://discord.gg/rZqsvrMdwR)", inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(About(client))
