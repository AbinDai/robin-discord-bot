import discord, asyncio
from discord.ext import commands

class ModerasiDua(commands.Cog):
    def __init__(self, client):
        self.client = client

    #isi command: slowmode, createchannel, deletetextchannel, deletevoicechannel, renametextchannel, renamevoicechannel, editchanneltopic
    @commands.group(invoke_without_command=True)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slowmode(self, ctx, detik=None, channel:discord.TextChannel=None):
        if not detik:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak memasukkan detik!\nContoh: `r!slowmode [waktu (detik)] [#channel (opsional)]`\n*kamu bisa gunakan `r!slowmode disable/off [#channel (opsioanl)]` utk mematikannya")
        else:
            channel = ctx.channel if not channel else channel

            await channel.edit(slowmode_delay=detik)

            embed = discord.Embed(
                title = "Slowmode Diaktifkan!",
                description = f"Channel {channel.mention} telah dipakaikan slowmode dengan durasi **{detik}** detik.",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            await ctx.send(embed=embed)
    @slowmode.command(aliases=["off"])
    async def disable(self, ctx, channel:discord.TextChannel=None):
        channel = ctx.channel if not channel else channel

        await channel.edit(slowmode_delay=0)

        embed = discord.Embed(
            title = "Slowmode Dimatikan",
            description = f"Slowmode untuk channel {channel.mention} telah dimatikan.",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        await ctx.send(embed=embed)
    @slowmode.error
    async def on_slowmode_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak punya izin `manage channels`!**")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")

    @commands.group(invoke_without_command=True, aliases=["newchannel"])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def createchannel(self, ctx):
        embed = discord.Embed(
            title = "Penggunaan Command `createchannel`",
            description = "`r!newchannel voice [nama channel]` untuk membuat voice channel.\n"
                          "`r!newchannel text [nama channel]` untuk membuat text channel.",
            color = ctx.guild.get_member(self.client.user.id).color
        )
        embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @createchannel.command()
    async def text(self, ctx, *, nama=None):
        if not nama:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan nama channel!\nContoh: `r!newchannel text [nama channel]`")
        else:
            guild = ctx.message.guild
            await guild.create_text_channel(nama)

            embed = discord.Embed(
                title = "Channel Dibuat!",
                description = f'Text channel **"#{nama}"** berhasil dibuat.',
                color = ctx.guild.get_member(self.client.user.id).color
            )
            await ctx.send(embed=embed)
    @createchannel.command()
    async def voice(self, ctx, *, nama=None):
        if not nama:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan nama channel!\nContoh: `r!newchannel voice [nama channel]`")
        else:
            guild = ctx.message.guild
            await guild.create_voice_channel(nama)

            embed = discord.Embed(
                title = "Channel Dibuat!",
                description = f'Voice channel **"🔉{nama}"** berhasil dibuat.',
                color = ctx.guild.get_member(self.client.user.id).color
            )
            await ctx.send(embed=embed)
    @createchannel.error
    async def on_createchannel_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak punya izin `manage channels`!**")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk mejalankan command ini!**")

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def deletetextchannel(self, ctx, cenel:discord.TextChannel):
        embed = discord.Embed(
            title = "⚠ Konfirmasi",
            description = f"Yakinkah kamu ingin menghapus channel {cenel.mention}? Tindakan ini tidak dapat dipulihkan!",
            color = 0xffcc4d
        )
        embed.set_footer(
            text='Balas "ya" untuk mengonfirmasi, "tidak" untuk membatalkan. Timeout dalam 10 detik.',
            icon_url="https://natsab.files.wordpress.com/2015/11/countdown-o.gif"
        )
        konfirmasi = await ctx.send(embed=embed, delete_after=10)
        
        msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=10)

        if msg.content.lower() == "ya":
            await konfirmasi.delete()
            await cenel.delete()
            embed = discord.Embed(
                title=f"Berhasil Dihapus",
                description=f"Channel **#{cenel.name}** berhasil dihapus.",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            await ctx.send(embed=embed)
        elif msg.content.lower() == "tidak":
            await konfirmasi.delete()
            embed = discord.Embed(
                title=f"Operasi Dibatalkan",
                description=f"Tidak jadi menghapus channel, operasi dibatalkan.",
                color = 0xff0000
            )
            await ctx.send(embed=embed)
    @deletetextchannel.error
    async def on_deletetextchannel_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak punya izin `manage channels`!**")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk mejalankan command ini!**")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan channelnya!\nContoh: `r!deletetextchannel #general`")

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def deletevoicechannel(self, ctx, channel:discord.VoiceChannel):
        embed = discord.Embed(
            title = "⚠ Konfirmasi",
            description = f"Yakinkah kamu ingin menghapus channel {channel.mention}? Tindakan ini tidak dapat dipulihkan!",
            color = 0xffcc4d
        )
        embed.set_footer(
            text='Balas "ya" untuk mengonfirmasi, "tidak" untuk membatalkan. Timeout dalam 10 detik.',
            icon_url="https://natsab.files.wordpress.com/2015/11/countdown-o.gif"
        )
        konfirmasi = await ctx.send(embed=embed, delete_after=10)
        
        msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=10)

        if msg.content.lower() == "ya":
            await konfirmasi.delete()
            await channel.delete()
            embed = discord.Embed(
                title=f"Berhasil Dihapus",
                description=f"Channel **🔊{channel.name}** berhasil dihapus.",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            await ctx.send(embed=embed)
        elif msg.content.lower() == "tidak":
            await konfirmasi.delete()
            embed = discord.Embed(
                title=f"Operasi Dibatalkan",
                description=f"Tidak jadi menghapus channel, operasi dibatalkan.",
                color = 0xff0000
            )
            await ctx.send(embed=embed)
    @deletevoicechannel.error
    async def on_deletevoicechannel_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak punya izin `manage channels`!**")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk mejalankan command ini!**")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan channelnya!\nContoh: `r!deletetextchannel dengar lagu 1`")

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def renametextchannel(self, ctx, channel:discord.TextChannel=None, *, nama=None):
        if not channel:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan nama text channel dan nama barunya!\nContoh: `r!edittextchannelname #general chat biasa`")
        elif nama == None:
            await ctx.reply(f"<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan nama barunya!\nContoh: `r!edittextchannelname #{channel.name} [nama baru]`")
        else:
            embed = discord.Embed(
                title = "Berhasil Mengubah Nama",
                description = f"Channel **#{channel.name}** berhasil diubah nama menjadi **{nama}**",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            await ctx.send(embed=embed)

            await channel.edit(name=nama)
    @renametextchannel.error
    async def on_renametextchannel_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak punya izin `manage channels`!**")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk mejalankan command ini!**")

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def renamevoicechannel(self, ctx, channel:discord.VoiceChannel=None, *, nama=None):
        if not channel:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebut channel-nya sekaligus nama barunya!\nContoh: `r!renamevoicechannel [voice channel (bisa mention, bisa juga sebut, bisa juga kasih ID-nya)] [nama baru]`")
        elif nama == None:
            await ctx.reply(f"<:robin_palato:818892964457349220> **Sintaks tidak valid!** Tuliskan nama barunya!\nContoh: `r!renamevoicechannel \"{channel.name}\" [nama baru]`")
        else:
            embed = discord.Embed(
                title = "Berhasil Diubah",
                description = f"Channel **🔉{channel.name}** diubah nama menjadi **{nama}**.",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            await ctx.send(embed=embed)

            await channel.edit(name=nama)
    @renamevoicechannel.error
    async def on_renamevoicechannel_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak punya izin `manage channels`!**")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk mejalankan command ini!**")

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def editchanneltopic(self, ctx, channel:discord.TextChannel=None, *, topik=None):
        if not channel:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebut channel-nya dengan topik barunya!\nContoh: `r!editchanneltopic [text channel] [topik baru]`")
        elif topik == None:
            await ctx.reply(f"<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan topiknya!\nContoh: `r!editchanneltopic #{channel.name} [topik baru]`")
        else:
            await channel.edit(topic=topik)

            embed = discord.Embed(
                title = "Topik Diterapkan",
                description = f"Topik untuk channel {channel.mention} telah ditetapkan menjadi `{topik}`.",
                color = ctx.guild.get_member(self.client.user.id).color
            )
            await ctx.send(embed=embed)
    @editchanneltopic.error
    async def on_editchanneltopic_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak punya izin `manage channels`!**")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk mejalankan command ini!**")

def setup(client):
    client.add_cog(ModerasiDua(client))