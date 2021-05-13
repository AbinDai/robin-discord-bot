from discord.ext import commands

import dbl


class TopGG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjgwNTg3NjIxOTY0NzM2MTA1MyIsImJvdCI6dHJ1ZSwiaWF0IjoxNjIwOTE0ODE2fQ.duPaGHNn2W9X6E2Or-u2kN_MIWyaIxU9dp1jFqUfEw0'  
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True)  

    @commands.Cog.listener()
    async def on_guild_post(self):
        print("Berhasil memosting angka jumlah server ke top.gg.")

    


def setup(bot):
    bot.add_cog(TopGG(bot))