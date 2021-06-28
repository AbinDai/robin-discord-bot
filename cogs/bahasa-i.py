import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Bahasa_I(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="bahasa-i")
    async def bhsaI(self, ctx:Context, *, teks:str=None):
        if not teks:
            return await ctx.send("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan teks!\nContoh: `r!bahasa-i ini adalah tes`")
        
        await ctx.reply(content=teks.replace("a", "i").replace("u", "i").replace("e", "i").replace("o", "i"), mention_author=False)

def setup(client):
    client.add_cog(Bahasa_I(client))
