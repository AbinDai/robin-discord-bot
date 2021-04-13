import discord
from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('invite.py, siap!')

    @commands.command(aliases=['undang'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invite(self, ctx):
        embed = discord.Embed(
            title = 'Ingin menambahkanku di servermu?',
            description = 'Klik link [berikut](https://discord.com/api/oauth2/authorize?client_id=805876219647361053&permissions=1543892038&scope=bot)',
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Invite(client))