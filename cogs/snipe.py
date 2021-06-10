import discord, requests, os
from discord.ext import commands
from discord.ext.commands.context import Context
from asyncio.tasks import sleep

snipe_message_author = {}
snipe_message_content = {}
snipe_attachment_content = {}

class Snipe(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        attachment = message.attachments[0]
        snipe_attachment_content[message.channel.id] = attachment.url

        response = requests.get(attachment.url)
        file = open("deleted.png", "wb")
        file.write(response.content)
        file.close()

        await sleep(300)
        del snipe_message_author[message.channel.id]
        del snipe_message_content[message.channel.id]
        del snipe_attachment_content[message.channel.id]
        os.remove("deleted.png")

    @commands.command()
    async def snipe(self, kongteks:Context):
        channel = kongteks.channel
        try:
            embed = discord.Embed(
                title = f"Pesan yang Baru Saja Dihapus di Channel Ini",
                description = snipe_message_content[channel.id],
                color = kongteks.guild.me.color
            )
            embed.set_author(name=f"Dikirim oleh {snipe_message_author[channel.id]}", \
            icon_url=snipe_message_author[channel.id].avatar_url)
            try:
                file = discord.File("./deleted.png", filename="deleted.png")
                embed.set_image(url="attachment://deleted.png")
                await kongteks.send(file=file, embed=embed)
                os.remove("deleted.png")
            except:
                embed.set_image(url=snipe_message_content[channel.id])
                await kongteks.send(embed=embed)
        except: 
            embed = discord.Embed(
                title = f"Pesan yang Baru Saja Dihapus di Channel Ini",
                description = snipe_message_content[channel.id],
                color = kongteks.guild.me.color
            )
            embed.set_author(name=f"Dikirim oleh {snipe_message_author[channel.id]}", \
            icon_url=snipe_message_author[channel.id].avatar_url)
            await kongteks.send(embed=embed)
    @snipe.error
    async def on_snipe_error(self, ctx:Context, error):
        if isinstance(error, commands.CommandError):
            await ctx.send("Tidak ada pesan yang barusan dihapus di channel ini.")

def setup(client):
    client.add_cog(Snipe(client))