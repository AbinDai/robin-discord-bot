import discord
from discord.ext import commands

class Moderasi(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("moderasi.py siap")

    #skrip ini berisi 9 buah command, yaitu: kick, ban, unban, changenick, clear, newrole, giverole, removerole, deleteroles
    @commands.command(aliases=["hus", "usir", "keluarkan", "tendang", "kck"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, alasan=None):
        alasan = "Tidak ada." if not alasan else alasan

        await ctx.guild.kick(user=member, reason=alasan)
        
        embed = discord.Embed(
            description = f"**Alasan:** {alasan}",
            color = member.color
        )
        embed.set_author(name=f"{member.display_name} Berhasil di-Kick!", icon_url=member.avatar_url)
        await ctx.reply(embed=embed)

        await member.send(f'Mohon maaf, kamu di-Kick dari server **{ctx.author.guild}** dengan alasan **"{alasan}"** 🙏')
    @kick.error #ini untuk error handling-nya
    async def on_kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak memiliki izin `kick members`!**")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan orang yang mau kamu kick!\nContoh: `r!kick @Abin#4405 [alasan (opsional)]`")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, alasan=None):
        alasan = "Tidak ada." if not alasan else alasan

        await ctx.guild.ban(user=member, reason=alasan)

        embed = discord.Embed(
            description = f"**Alasan:** {alasan}",
            color = member.color
        )
        embed.set_author(name=f"{member.display_name} Berhasil di-Ban!", icon_url=member.avatar_url)
        await ctx.reply(embed=embed)

        await member.send(f'Mohon maaf, kamu di-Ban dari server **{ctx.author.guild}** dengan alasan **"{alasan}"** 🙏')
    @ban.error
    async def on_ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak memiliki izin `ban members`!**")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan orang yang mau kamu Ban!\nContoh: `r!ban @Abin#4405 [alasan (opsional)]`")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member):
        member = await self.client.fetch_user(int(member))
        await ctx.guild.unban(member)

        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name=f"{member.display_name} Berhasil di-Unban!")
        await ctx.reply(embed=embed)

        await member.send(f"Kamu telah di-Unban dari server **{ctx.author.guild}**.")
    @unban.error
    async def on_unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak memiliki izin `ban members`!**")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan ID orang yang mau kamu Unban!\nContoh: `r!unban 550953412489904129`")

    @commands.command(aliases=["nickname", "nick", "changename"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_nicknames=True)
    @commands.bot_has_guild_permissions(manage_nicknames=True)
    async def changenick(self, ctx, member:discord.Member=None, *, nick=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan nama orang yang mau kamu ubah namanya!\nContoh: `r!nick **[nama]** [nick baru]`")
        elif nick == None:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan nicknamenya!\nContoh: `r!nick [nama] **[nick baru]**`")
        else:
            await member.edit(nick=nick)

            embed = discord.Embed(
                description = f"Dari **\"{member.display_name}\"** menjadi **\"{nick}\"**",
                color = member.color
            )
            embed.set_author(name=f"Nickname {member} Berhasil Diubah!", icon_url=member.avatar_url)
            await ctx.reply(embed=embed)
    @changenick.error
    async def on_changenick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak memiliki izin `manage nicknames`!**")

    @commands.command(aliases=["purge", "clr"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    @commands.bot_has_guild_permissions(manage_messages=True)
    async def clear(self, ctx, jumlah:int):
        await ctx.channel.purge(limit=jumlah)
        await ctx.author.send(f"Behasil menghapus {jumlah} pesan.")
    @clear.error
    async def on_clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak memiliki izin `manage messages`!**")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan jumlah pesan yang mau kamu hapus!\nContoh: `r!clr 15`")

    @commands.command(aliases=["createrole", "bikinrole", "makerole", "addrole"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def newrole(self, ctx, nama, warna=None):
        warna = "fffff0" if not warna else warna

        warna_role = int(f"{warna}", 16)
        await ctx.guild.create_role(name=nama, color=discord.Color(warna_role))

        embed = discord.Embed(
            title = "Role Berhasil Dibuat!",
            description = f"Role **\"{nama}\"** dengan warna **#{warna.upper()}** berhasil dibuat!",
            color = warna_role
        )
        await ctx.reply(embed=embed)
    @newrole.error
    async def on_newrole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak memiliki izin `manage roles`!**")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan nama role!\nContoh: `r!newrole \"Pangeran\" [warna (opsional)]` (penulisan HEX warna jangan disertakan `#` ataupun `0x`).\nUntuk pemberian nama, apit namanya menggunakan tanda petik. Contoh `r!newrole \"Anjing Ganas\"`")
        elif isinstance(error, commands.CommandError):
            await ctx.reply("❌ **Terjadi kesalahan.** Kamu mungkin tidak memberikan tanda petik pada nama role yang akan diberikan. Contoh: `r!newrole \"Tes\"`")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_roles=True)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def giverole(self, ctx, member:discord.Member=None, role:discord.Role=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan user yang mau kamu beri role!\nContoh: `r!giverole **[user]** [role]`")
        elif role == None:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan role yang mau kamu berikan!\nContoh: `r!giverole [user] **[role]**`")
        else:
            await member.add_roles(role)

            embed = discord.Embed(
                description = f"Role {role.mention} berhasil diberikan kepada {member.mention}!",
                color = role.color
            )
            embed.set_author(name="Berhasil Diberikan!", icon_url=member.avatar_url)
            await ctx.reply(embed=embed)
    @giverole.error
    async def on_giverole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak memiliki izin `manage roles`!**")
        elif isinstance(error, commands.CommandError):
            await ctx.reply("❌ **Mohon maaf, saya tidak dapat memberikan role kepada orang ini.**")
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_roles=True)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def removerole(self, ctx, member:discord.Member=None, role:discord.Role=None):
        if not member:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan orang yang mau kamu hapus role-nya!\nContoh: `r!removerole **[nama]** [role]`")
        elif role == None:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan role yang mau kamu keluarkan dari orang tersebut!\nContoh: `r!removerole [nama] **[role]**`")
        else:
            await member.remove_roles(role)

            embed = discord.Embed(
                description = f"Role {role.mention} telah dicabut dari user {member.mention}.",
                color = role.color
            )
            embed.set_author(name="Berhasil Mencabut Role!", icon_url=member.avatar_url)
            await ctx.reply(embed=embed)
    @removerole.error
    async def on_removerole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak memiliki izin `manage roles`!**")
        elif isinstance(error, commands.CommandError):
            await ctx.reply("❌ **Mohon maaf, saya tidak dapat mencabut role dari orang ini.**")

    @commands.command(aliases=["hapusrole"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_roles=True)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def deleterole(self, ctx, role:discord.Role):
        embed = discord.Embed(
            title = "Role Dihapus",
            description = f"Role **\"{role.mention}\"** berhasil dihapus.",
            color = role.color
        )
        await ctx.reply(embed=embed)
        await role.delete()
    @deleterole.error
    async def on_deleterole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("❌ **Kamu tidak punya izin untuk menjalankan command ini!**")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("❌ **Saya tidak memiliki izin `manage roles`!**")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Sebutkan role yang mau kamu hapus!\nContoh: `r!deleterole @Friends`")
        elif isinstance(error, commands.CommandError):
            await ctx.reply("❌ **Mohon maaf, saya tidak dapat menghapus role ini.**")

def setup(client):
    client.add_cog(Moderasi(client))
