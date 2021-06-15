import discord, platform, datetime, time, psutil
from discord.ext import commands
from discord.ext.commands.context import Context

class About(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    @commands.command(aliases=['tentangbot', 'aboutme', 'aboutbot', 'tentang', 'info', 'infobot', 'botinfo'])
    async def about(self, ctx:Context):
        embed = discord.Embed(
            title = "Informasi Bot",
            color = ctx.guild.me.color
        )
        embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
        embed.set_thumbnail(url=self.client.user.avatar_url_as(format="png", size=4096))

        embed.add_field(name="Nama", value=f"[{self.client.user.name}](https://onepiece.fandom.com/id/wiki/Nico_Robin)")
        embed.add_field(name="Pengembang", value="Abin#4405")
        embed.add_field(name="Dibuat", value=self.client.user.created_at.strftime("%d/%m/%Y %H:%M:%S"))

        embed.add_field(name="Jumlah Server", value=len(self.client.guilds))
        embed.add_field(name="Jumlah User", value=len(self.client.users))
        #
        list_text_channel = []
        for guild in self.client.guilds:
            for channel in guild.text_channels:
                list_text_channel.append(channel)
        embed.add_field(name="Jumlah Channel", value=len(list_text_channel))
        list_text_channel.clear()

        embed.add_field(name="Library", value=f"discord.py v{discord.__version__}")
        embed.add_field(name="Bahasa Program", value=f"Python v{platform.python_version()}")
        embed.add_field(name="Ping Bot", value=f"{round(self.client.latency*1000)}ms")

        embed.add_field(name="Waktu Aktif", value=str(datetime.timedelta(seconds=int(round(time.time()-startTime)))))
        embed.add_field(name="Penggunaan Memori", value=f"CPU: {psutil.cpu_percent()}%\nRAM: {psutil.virtual_memory().percent}%")
        embed.add_field(name="ID Bot", value=self.client.user.id)

        embed.add_field(
            name="⠀",
            value="[Link Invite](https://top.gg/bot/805876219647361053/invite) | [Vote Disini!](https://top.gg/bot/805876219647361053/vote) | [Repositori GitHub](https://github.com/AbinDai/robin-discord-bot/) | [Help Server](https://discord.gg/rZqsvrMdwR)",
            inline=False
        )

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(About(client))
