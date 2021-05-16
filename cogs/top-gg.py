import discord, dbl, os
from discord.ext import commands, tasks

class TopGG(commands.Cog):
    """
    This example uses dblpy's autopost feature to post guild count to top.gg every 30 minutes.
    """

    def __init__(self, bot):
        self.bot = bot
        self.token = f'{os.environ["TOPGG_TOKEN"]}' 
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True)  # Autopost will post your guild count every 30 minutes

    @commands.Cog.listener()
    async def on_guild_post(self):
        channel = self.bot.get_channel(842409718835839006)
        embed = discord.Embed(title="Notifikasi Servercount top.gg", description="Berhasil memosting servercount.")
        await channel.send(embed=embed)

        print("Server count posted successfully")

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        """An event that is called whenever someone votes for the bot on top.gg."""
        channel = self.bot.get_channel(843453862319882252)
        embed = discord.Embed(title="Bot di-Upvote", description=f"Seseorang meng-upvote bot ini!\n`{data}`.", color=discord.Color.green())
        await channel.send(embed=embed)

        print("Received an upvote:", "\n", data, sep="")

def setup(bot):
    bot.add_cog(TopGG(bot))
