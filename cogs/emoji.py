import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Emojih(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["moji", "emj"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def emoji(self, ctx:Context, emoji:discord.PartialEmoji):
        embed = discord.Embed(
            title = "Emoji",
            color = ctx.guild.me.color
        )
        embed.add_field(name="Nama", value=f"[:{emoji.name}:]({emoji.url})")
        if emoji.animated is True:
            embed.add_field(name="Beranimasi?", value="Ya")
        else:
            embed.add_field(name="Beranimasi?", value="Tidak")
        embed.add_field(name="ID", value=emoji.id)

        embed.add_field(name="Ditambahkan pada", value=emoji.created_at.strftime("%d-%m-%Y | %H:%M:%S"))
        embed.add_field(name="Kode", value=f"`{emoji.name}:{emoji.id}`")
        if emoji.is_custom_emoji() is True:
            embed.add_field(name="Emoji Kustom?", value="Ya")
        else:
            embed.add_field(name="Emoji Kustom?", value="Bukan")

        embed.set_image(url=emoji.url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Emojih(client))
