import discord, dbl, os
from discord.ext import commands

class TopGG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.token = os.environ["TOPGG_TOKEN"]  
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True)  

    @commands.Cog.listener()
    async def on_guild_post(self):
        channel = client.get_channel(842409718835839006)
        
        embed = discord.Embed(title="🔢 Notifikasi Server Count", description="Berhasil memosting angka jumlah server ke top.gg.")
        await channel.send(embed=embed)
        print("Berhasil memosting angka jumlah server ke top.gg.")

def setup(bot):
    bot.add_cog(TopGG(bot))
