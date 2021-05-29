import discord
from discord.ext import commands

class Saran(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("saran.py siap!")

    @commands.command(aliases=["feedback"])
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def saran(self, ctx, *, saran:str):
        await ctx.reply(":white_check_mark: **Masukan Anda sudah terkirim!** Terima kasih banyak atas kontribusinya :))")

        channel = self.client.get_channel(824308102367019068)
        embed = discord.Embed(
            title = "Ada Saran!"
            description = saran,
            color = 0x058cfc
        )
        embed.set_footer(text=f"Dari Server: {ctx.author.guild}", icon_url=ctx.author.guild.icon_url)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(Saran(client))
