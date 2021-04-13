import discord, requests, os
from discord.ext import commands

class Wasted(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("wasted.py siap")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wasted(self, ctx, member: discord.Member=None):
        member = ctx.author if not member else member
        
        response = requests.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png', size=4096)}")
        file = open("wasted.png", "wb")
        file.write(response.content)
        file.close()
                                    
        await ctx.send(file=discord.File("wasted.png"))
            
        os.remove("wasted.png")
                                    

def setup(client):
    client.add_cog(Wasted(client))
