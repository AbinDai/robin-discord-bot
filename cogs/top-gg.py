import discord, dbl, os
from discord.ext import commands, tasks

class TopGG(commands.Cog):
    """
    This example uses tasks provided by discord.ext to create a task that posts guild count to top.gg every 30 minutes.
    """

    def __init__(self, bot):
        self.bot = bot
        self.token = os.environ["TOPGG_TOKEN"]  # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.bot, self.token)
        self.update_stats.start()

    def cog_unload(self):
        self.update_stats.cancel()

    @tasks.loop(minutes=30)
    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count."""
        await self.bot.wait_until_ready()
        try:
            server_count = len(self.bot.guilds)
            await self.dblpy.post_guild_count(server_count)

            channel = self.bot.get_channel(842409718835839006)
            embed = discord.Embed(title="Notifikasi Top.gg", description = f"Berhasil memosting servercount `{server_count}`", color=discord.Color.green())
            await channel.send(embed=embed)
            print('Posted server count ({})'.format(server_count))
        except Exception as e:
            channel = self.bot.get_channel(842409718835839006)
            embed = discord.Embed(title="Notifikasi Top.gg", description = f"Gagal memosting servercount.\n`{type(e).__name__}`: `{e}`", color=discord.Color.red())
            await channel.send(embed=embed)
            print('Failed to post server count\n{}: {}'.format(type(e).__name__, e))

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        """An event that is called whenever someone votes for the bot on top.gg."""
        print("Received an upvote:", "\n", data, sep="")

def setup(bot):
    bot.add_cog(TopGG(bot))
