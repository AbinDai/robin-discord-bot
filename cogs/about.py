import discord, platform, datetime, time
from discord.ext import commands

class About(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    @commands.command(aliases=['tentangbot', 'aboutme', 'aboutbot', 'tentang', 'info', 'infobot', 'botinfo'])
    async def about(self, ctx):
        embed = discord.Embed(
            title = "Informasi Bot",
            color = ctx.guild.me.color
        )
        embed.set_author(name=self.client.user, icon_url=self.client.user.avatar_url)
        embed.set_thumbnail(url=self.client.user.avatar_url_as(format="png", size=4096))

        embed.add_field(name="Nama", value=f"[{self.client.user.name}](https://onepiece.fandom.com/id/wiki/Nico_Robin)")
        embed.add_field(name="Pengembang", value="Abin#4405")
        embed.add_field(name="Dibuat", value=self.client.user.created_at.strftime("%d/%m/%Y %H:%M:%S"))

        test = str(len(self.client.guilds))
        jumlah_server = ''
        while test:
            jumlah_server += test[:3]
            if len(test) > 3:
                jumlah_server += '.'
            test = test[3:]
        embed.add_field(name="Jumlah Server", value=jumlah_server)
        #
        test = str(len(self.client.users))
        jumlah_pengguna = ''
        while test:
            jumlah_pengguna += test[:3]
            if len(test) > 3:
                jumlah_pengguna += '.'
            test = test[3:]
        embed.add_field(name="Jumlah User", value=jumlah_pengguna)
        #
        list_text_channel = []
        for guild in self.client.guilds:
            for channel in guild.text_channels:
                list_text_channel.append(channel)
        test = str(len(list_text_channel))
        jumlah_text_channel = ''
        while test:
            jumlah_text_channel += test[:3]
            if len(test) > 3:
                jumlah_text_channel += '.'
            test = test[3:]
        embed.add_field(name="Jumlah Channel", value=jumlah_text_channel)
        list_text_channel.clear()

        embed.add_field(name="Library", value=f"discord.py v{discord.__version__}")
        embed.add_field(name="Bahasa Program", value=f"Python v{platform.python_version()}")
        embed.add_field(name="Ping Bot", value=f"{round(self.client.latency*1000)}ms")

        embed.add_field(name="Waktu Aktif", value=str(datetime.timedelta(seconds=int(round(time.time()-startTime)))))
        #
        test = str(len(self.client.emojis))
        jumlah_emoji = ''
        while test:
            jumlah_emoji += test[:3]
            if len(test) > 3:
                jumlah_emoji += '.'
            test = test[3:]
        embed.add_field(name="Jumlah Emoji", value=jumlah_emoji)
        embed.add_field(name="ID Bot", value=self.client.user.id)

        embed.add_field(
            name="⠀",
            value="[Link Invite](https://top.gg/bot/805876219647361053/invite) | [Vote Disini!](https://top.gg/bot/805876219647361053/vote) | [Repositori GitHub](https://github.com/AbinDai/robin-discord-bot/) | [Help Server](https://discord.gg/rZqsvrMdwR)",
            inline=False
        )

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(About(client))
