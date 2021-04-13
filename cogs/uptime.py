import datetime, time
from discord.ext import commands

class Uptime(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("uptime.py, siap!")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time))
        text = str(datetime.timedelta(seconds=difference))
    
        await ctx.send(f":timer: **Waktu *uptime* bot:** `{text}`.")

def setup(client):
    client.add_cog(Uptime(client))
