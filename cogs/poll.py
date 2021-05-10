import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("poll.py siap")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poll(self, ctx, *, konten):
        if not konten:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan isi konten yang ingin kamu mintai pendapat!\nContoh: `r!poll tar mlm mabar yok`")
        else:
            await ctx.message.delete()

            embed = discord.Embed(
                description = konten,
                color = ctx.guild.get_member(self.client.user.id).color
            )
            embed.set_author(name=f"{ctx.author.display_name} meminta pendapat!", icon_url=ctx.author.avatar_url)
            kirim = await ctx.send(embed=embed)

            emot = ["✅", "❌"]
            for emoji in emot:
                await kirim.add_reaction(emoji)

def setup(client):
    client.add_cog(Poll(client))
