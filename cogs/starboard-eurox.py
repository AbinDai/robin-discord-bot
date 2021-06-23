import discord
from discord.ext import commands

class Starboard(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction:discord.Reaction, user):
        channel = self.client.get_channel(855752544004079636)
        eurox = [470473044972929034]

        if reaction.emoji == "⭐":
            embed = discord.Embed(
                description = reaction.message.content,
                color = 0xffac33
            )
            embed.set_author(name=reaction.message.author, icon_url=reaction.message.author.avatar_url)
            #
            try:
                if str(reaction.message.content).startswith("http"):
                    try:
                        embed.set_image(url=reaction.message.content)
                    except:
                        pass
                else:
                    attachment = reaction.message.attachments[0]
                    embed.set_image(url=attachment.url)
            except:
                pass

            if reaction.message.guild.id in eurox:
                await channel.send(
                    f"⭐ {reaction.message.channel.mention}\n{reaction.message.jump_url}",
                    embed = embed
                )

def setup(client):
    client.add_cog(Starboard(client))
