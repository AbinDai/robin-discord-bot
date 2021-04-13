from discord.ext import commands

class ErrorHandle(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("error handling siap")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply('Command yang kamu coba eksekusi tidak tersedia saat ini. <:singa_nangis:799096679776387103>')
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"❌ **Santai bro!** Tunggu **{error.retry_after:.2f}** detik lagi sebelum menggunakan command ini!")
        elif isinstance(error, commands.EmojiNotFound):
            await ctx.reply("❌ **Emoji tidak ditemukan...**")
        elif isinstance(error, commands.RoleNotFound):
            await ctx.reply("❌ **Role tidak ditemukan...**")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.reply("❌ **Member tidak ditemukan...**")

def setup(client):
    client.add_cog(ErrorHandle(client))