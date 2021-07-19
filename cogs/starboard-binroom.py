import discord
from discord.ext import commands

class Starboard(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction:discord.Reaction, user):
        if reaction.emoji == "⭐":
            embed = discord.Embed(
                description = reaction.message.content,
                color = 0xffac33
            )
            embed.set_author(name=user, icon_url=user.avatar_url)

            try:
                embed.set_image(url=reaction.message.attachments[0].url)
            except:
                pass

            if str(reaction.message.content).startswith("https://") or str(reaction.message.content).startswith("http://"):
                try:
                    embed.set_image(url=reaction.message.content)
                except:
                    pass

            if user.guild.id == 783016541712154674:
                await self.client.get_channel(866550228773503009).send(content=f"⭐ {reaction.message.channel.mention}\n{reaction.message.jump_url}", embed=embed)

def setup(client):
    client.add_cog(Starboard(client))
