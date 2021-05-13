import os
from discord.ext import commands

import dbl


class TopGG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.token = os.environ["TOPGG_TOKEN"]  
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True)  

    @commands.Cog.listener()
    async def on_guild_post(self):
        print("Berhasil memosting angka jumlah server ke top.gg.")

    


def setup(bot):
    bot.add_cog(TopGG(bot))
