from discord.ext import commands
from discord.ext.commands.context import Context
from main import togetherControl

class DiscordTogether(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(invoke_without_command=True, aliases=["yttogether", "ytt"])
    async def youtubetogether(self, ctx:Context):
        if ctx.author.is_on_mobile():
            return await ctx.send("Fitur ini belum tersedia untuk platform mobile!")

        if (ctx.author.voice):
            link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')

            await ctx.send(f"Berikut link YouTube Together untuk Voice Channel {ctx.author.voice.channel.mention}.\n**Klik link-nya** untuk memulai!\n\n{link}")
        else:
            await ctx.send("❌ **Masuk ke Voice Channel terlebih dahulu.**")

    @commands.command()
    async def chess(self, ctx:Context):
        if ctx.author.is_on_mobile():
            return await ctx.send("Fitur ini belum tersedia untuk platform mobile!")

        if (ctx.author.voice):
            link = await togetherControl.create_link(ctx.author.voice.channel.id, 'chess')

            await ctx.send(f"**Klik link** dibawah ini untuk memulai!\n\n{link}")
        else:
            await ctx.send("❌ **Masuk ke Voice Channel terlebih dahulu.**")

    @commands.command()
    async def betrayal(self, ctx:Context):
        if ctx.author.is_on_mobile():
            return await ctx.send("Fitur ini belum tersedia untuk platform mobile!")

        if (ctx.author.voice):
            link = await togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')

            await ctx.send(f"**Klik link** dibawah ini untuk memulai!\n\n{link}")
        else:
            await ctx.send("❌ **Masuk ke Voice Channel terlebih dahulu.**")

    @commands.command()
    async def fishing(self, ctx:Context):
        if ctx.author.is_on_mobile():
            return await ctx.send("Fitur ini belum tersedia untuk platform mobile!")

        if (ctx.author.voice):
            link = await togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')

            await ctx.send(f"**Klik link** dibawah ini untuk memulai!\n\n{link}")
        else:
            await ctx.send("❌ **Masuk ke Voice Channel terlebih dahulu.**")

def setup(client):
    client.add_cog(DiscordTogether(client))