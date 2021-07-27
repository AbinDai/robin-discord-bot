import discord
from discord.ext import commands

class PrefixonMention(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content in [f"<@!{self.client.user.id}>", f"<@{self.client.user.id}>"]:
            embed = discord.Embed(description="Prefix: `r!`", color=message.guild.me.color)
            await message.channel.send(embed=embed)
            
def setup(client):
    client.add_cog(PrefixonMention(client))
