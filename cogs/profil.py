import discord, requests, os
from discord.flags import PublicUserFlags
from discord.ext import commands
from discord.ext.commands import Context
from dominant_color_detection import detect_colors

class Profil(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #command avatar
    @commands.command(aliases=['avt', 'pfp', 'pp'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self, ctx, *, member: discord.Member=None):
        member = ctx.author if not member else member

        #gunakan "mengetik"
        async with ctx.typing():
            #kita coba donlot pp nya
            response = requests.get(member.avatar_url_as(format="png",size=4096))
            file = open("pp.png", "wb")
            file.write(response.content)
            file.close()
            
            #setelah itu kita coba detect warna yg pling dominan di foto profilnya
            #kemudian kita pake buat warna embed
            colors, ratios = detect_colors("pp.png", 3)
            warna = colors[0][1:]
            warna_akhir = int(warna, 16)
            os.remove("pp.png")

            #bikin embed
            embed = discord.Embed(
                title = f'Berikut ini foto profilnya si {member.name}:',
                description = f'Link untuk format lain:\n[jpeg]({member.avatar_url_as(format="jpeg", size=4096)}) | [jpg]({member.avatar_url_as(format="jpg", size=4096)}) | [webp]({member.avatar_url_as(format="webp", size=4096)})',
                colour = warna_akhir #warna dominan pada foto profil seseorang
            )
            embed.set_image(url=member.avatar_url_as(format=None, static_format="png", size=4096))
            embed.set_footer(text=f'Di-Request oleh {ctx.author.name}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    #command serverinfo
    @commands.command(aliases=['infoserver'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverinfo(self, ctx:Context):
        embed = discord.Embed(
            title = "Informasi Server",
            color = ctx.guild.me.color
        )
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.guild.icon_url_as(format=None, static_format="png", size=4096))

        if ctx.guild.banner_url:
            embed.set_image(url=ctx.guild.banner_url)

        embed.add_field(name="Nama", value=ctx.guild.name)
        embed.add_field(name="ID", value=ctx.guild.id)
        try:
            embed.add_field(name="Dibuat pada", value=ctx.guild.created_at.strftime(f'%d/%m/%Y {int(ctx.guild.created_at.hour)+8}:%M:%S WITA'))
        except:
            embed.add_field(name="Dibuat pada", value="Gagal memuat info")

        if ctx.guild.description is not None:
            embed.add_field(name="Deskripsi", value=ctx.guild.description, inline=False)
        else:
            embed.add_field(name="Deskripsi", value="Tidak ada deskripsi.", inline=False)

        try:
            embed.add_field(name="Jumlah Text Channel", value=len(ctx.guild.text_channels))
            embed.add_field(name="Jumlah Voice Channel", value=len(ctx.guild.voice_channels))
            embed.add_field(name="Jumlah Kategori", value=len(ctx.guild.categories))
        except:
            embed.add_field(name="Jumlah Text Channel", value="Gagal memuat info")
            embed.add_field(name="Jumlah Voice Channel", value="Gagal memuat info")
            embed.add_field(name="Jumlah Kategori", value="Gagal memuat info")

        try:
            if ctx.guild.region is not None:
                embed.add_field(name="Negara", value=str(ctx.guild.region).capitalize())
            else:
                embed.add_field(name="Negara", value="Tidak ada")
        except:
            embed.add_field(name="Negara", value="Gagal memuat info")

        if ctx.guild.shard_id is not None:
            embed.add_field(name="ID Shard", value=ctx.guild.shard_id)
        else:
            embed.add_field(name="ID Shard", value="Tidak ada")
        if ctx.guild.afk_channel is not None:
            embed.add_field(name="Channel AFK", value=len(ctx.guild.afk_channel.mention))
        else:
            embed.add_field(name="Channel AFK", value="Tidak ada")

        if ctx.guild.owner is not None:
            embed.add_field(name="Pemilik", value=f"{ctx.guild.owner.mention} (`{ctx.guild.owner}`)")
        else:
            embed.add_field(name="Pemilik", value="Tidak dapat menemukan pemilik server.")
        embed.add_field(name="Level Boost", value=f"Level {ctx.guild.premium_tier} ({ctx.guild.premium_subscription_count} Boost)")
        if ctx.guild.premium_subscriber_role is not None:
            embed.add_field(name="Role Eksklusif Booster", value=ctx.guild.premium_subscriber_role.mention)
        else:
            embed.add_field(name="Role Eksklusif Booster", value="Tidak ada")

        try:
            if ctx.guild.system_channel is not None:
                embed.add_field(name="Channel Sistem", value=ctx.guild.system_channel.mention)
            else:
                embed.add_field(name="Channel Sistem", value="Tidak ada")
        except:
            embed.add_field(name="Channel Sistem", value="Gagal memuat info")

        try:
            if ctx.guild.rules_channel is not None:
                embed.add_field(name="Channel Aturan", value=ctx.guild.rules_channel.mention)
            else:
                embed.add_field(name="Channel Aturan", value="Tidak ada")
        except:
            embed.add_field(name="Channel Aturan", value="Gagal memuat info")

        try:
            if ctx.guild.public_updates_channel is not None:
                embed.add_field(name="Channel Update", value=ctx.guild.public_updates_channel.mention)
            else:
                embed.add_field(name="Channel Update", value="Tidak ada")
        except:
            embed.add_field(name="Channel Update", value="Gagal memuat info")

        try:
            if sum(len(emoji) for emoji in ", ".join([str(emoji) for emoji in await ctx.guild.fetch_emojis()])) < 1024:
                embed.add_field(name=f"Emoji ({len(ctx.guild.emojis)})", value=' '.join([str(emoji) for emoji in await ctx.guild.fetch_emojis()]), inline=False)
            else:
                embed.add_field(name=f"Emoji ({len(ctx.guild.emojis)})", value="Emoji terlalu banyak sehingga tidak muat disini.", inline=False)
        except:
            embed.add_field(name=f"Emoji (???)", value="Gagal memuat info.", inline=False)

        if sum(len(role) for role in ", ".join([str(role) for role in await ctx.guild.fetch_roles()])) < 1024:
            embed.add_field(name=f"Role ({len(ctx.guild.roles)})", value=' '.join([str(role.mention) for role in await ctx.guild.fetch_roles()]), inline=False)
        else:
            embed.add_field(name=f"Role ({len(ctx.guild.roles)})", value="Role terlalu banyak sehingga tidak muat disini.", inline=False)

        embed.set_footer(text=f"Di-Request oleh {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    #command servericon
    @commands.command(aliases=['fotoserver, serverpicture, serveravatar'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servericon(self, ctx):
        response = requests.get(ctx.guild.icon_url_as(format="png",size=4096))
        file = open("servericon.png", "wb")
        file.write(response.content)
        file.close()
        
        #kita coba detect warna yg pling dominan di foto server-nya
        #kemudian kita pake buat warna embed
        colors, ratios = detect_colors("servericon.png", 3)
        warna = colors[0][1:]
        warna_akhir = int(warna, 16)

        os.remove("servericon.png")

        embed = discord.Embed(
            title = f'Berikut foto server {ctx.guild.name}:',
            description = f'Butuh link dalam format lain?\n[jpeg]({ctx.guild.icon_url_as(format="jpeg", size=4096)}) | [jpg]({ctx.guild.icon_url_as(format="jpg", size=4096)}) | [webp]({ctx.guild.icon_url_as(format="webp", size=4096)})',
            colour = warna_akhir
        )
        embed.set_image(url=f'{ctx.guild.icon_url_as(format=None, static_format="png", size=4096)}')
        embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)

    #command userinfo
    @commands.command(aliases=['infopengguna, infoorang'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self, ctx:Context, *, member: discord.Member = None):
        member = ctx.author if not member else member

        embed = discord.Embed(
            title = "Informasi User",
            color = member.color
        )
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url_as(format=None, static_format="png", size=4096))

        embed.add_field(name="Username", value=member.name)
        embed.add_field(name="Tag", value=f"#{member.discriminator}")
        embed.add_field(name="Nama di Server Ini", value=member.display_name)

        embed.add_field(name="ID", value=member.id)
        if member.bot is True:
            embed.add_field(name="Adalah Bot?", value="Ya")
        else:
            embed.add_field(name="Adalah Bot?", value="Bukan")
        if member.top_role is not None:
            embed.add_field(name="Role Teratas", value=member.top_role.mention)
        else:
            embed.add_field(name="Role Teratas", value="Tidak ada")

        embed.add_field(name="HEX Warna Nama", value=member.color)
        if member.voice is not None:
            try:
                embed.add_field(name="Sedang Berada di Voice Channel", value=member.voice.channel.name.mention)
            except:
                embed.add_field(name="Sedang Berada di Voice Channel", value=member.voice.channel.name)
        else:
            embed.add_field(name="Sedang Berada di Voice Channel", value="Tidak ada")

        list_badge = []
        badge = str(member.public_flags.all())
        if "bug_hunter" in badge:
            list_badge.append("<:BugHunterLevel_1:853628065376763904> Bug Hunter (Pemburu Bug)")

        if "bug_hunter_level_2" in badge:
            list_badge.append("<:BugHunterLevel_2:853628340875296800> Bug Hunter Level 2 (Pemburu Bug Level 2)")

        if "early_supporter" in badge:
            list_badge.append("<:EarlySupporter:853628130816032810> Early Supporter (Pendukung Terdahulu Discord)")

        if "early_verified_bot_developer" in badge:
            list_badge.append("<:EarlyVerifiedBotDev:853624406399647774> Early Verified Bot Developer (Pengembang Bot Terdahulu yang Terverifikasi)")

        if "hypesquad_balance" in badge:
            list_badge.append("<:HypesquadBalance:853619058699796491> HypeSquad Balance")

        if "hypesquad_bravery" in badge:
            list_badge.append("<:HypesquadBravery:853619039615320064> HypeSquad Bravery")

        if "hypesquad_brilliance" in badge:
            list_badge.append("<:HypesquadBrilliance:853619079051345952> HypeSquad Brilliance")

        if "partner" in badge:
            list_badge.append("<:ServerPartner:853620957037592656> Server Partner (Pemilik Server yang ber-Partner dengan Discord)")

        if "staff" in badge:
            list_badge.append("<:DiscordEmployee:853619019192991744> Discord Staff (Karyawan Discord)")

        if "verified_bot" in badge:
            list_badge.append("<:VerifiedBot:853619094883270676> Verified Bot (Bot yang Sudah Terverifikasi)")

        if len(list_badge) == 0:
            embed.add_field(name=f"Badge ({len(list_badge)})", value="Tidak ada")
        else:
            embed.add_field(name=f"Badge ({len(list_badge)})", value="\n".join([badge for badge in list_badge]))
            list_badge.clear()

        embed.add_field(name="Dibuat pada", value=member.created_at.strftime(f"%d/%m/%Y {int(member.created_at.hour)+8}:%M:%S WITA"))
        embed.add_field(name="Bergabung pada", value=member.joined_at.strftime(f"%d/%m/%Y {int(member.joined_at.hour)+8}:%M:%S WITA"))

        roles = [role for role in member.roles]
        if sum(len(ROLE) for ROLE in ', '.join([role.mention for role in roles])) < 1024:
            embed.add_field(name=f'Jumlah Role ({len(roles)})', value=' '.join([role.mention for role in roles]), inline=False)
        else:
            embed.add_field(name=f'Jumlah Role ({len(roles)})', value="Role kebanyakan, sehingga tidak muat ditulis disini.", inline=False)

        if sum(len(izin) for izin in [perm[0] for perm in member.guild_permissions if perm[1]]) < 1024:
            embed.add_field(name=f"Izin-Izin ({len([perm[0] for perm in member.guild_permissions if perm[1]])})", value=f'`{", ".join([perm[0] for perm in member.guild_permissions if perm[1]]).replace("_", " ").capitalize()}`', inline=False)
        else:
            embed.add_field(name=f"Izin-Izin ({len([perm[0] for perm in member.guild_permissions if perm[1]])})", value=f'Izin kebanyakan, jadi tidak muat disini.', inline=False)

        if member.status == discord.Status.online:
            if member.is_on_mobile() == True:
                embed.add_field(name="Status", value="<:mobilestatus:853831784114028584> Online (Daring)")
            else:
                embed.add_field(name="Status", value="<:online:854258699908022302> Online (Daring)")
        elif member.status == discord.Status.idle:
            embed.add_field(name="Status", value="<:idle:854258886282313749> Idle (Diam)")
        elif member.status == discord.Status.dnd:
            embed.add_field(name="Status", value="<:dnd:854258993785733130> Do Not Disturb (Jangan Ganggu)")
        elif member.status == discord.Status.offline:
            embed.add_field(name="Status", value="<:offline:854259075608084480> Offline (Luring)")
        elif member.status == discord.Status.invisible:
            embed.add_field(name="Status", value="<:offline:854259075608084480> Invisible (Tak Terlihat)")
        else:
            embed.add_field(name="Status", value="Gagal mendapatkan info")

        for activity in member.activities:
            if isinstance(activity, discord.Game):
                embed.add_field(name="Aktifitas", value=f"Bermain **{activity.name}**")
            elif isinstance(activity, discord.Spotify):
                embed.add_field(name="Aktifitas", value=f"Mendengarkan **Spotify**")
            elif isinstance(activity, discord.Streaming):
                embed.add_field(name="Aktifitas", value=f"Streaming di **{activity.platform}**")

        for activity in member.activities:
            if isinstance(activity, discord.CustomActivity):
                if activity.name and activity.emoji:
                    embed.add_field(name="Status Kustom", value=f"{activity.emoji} {activity.name}")
                elif activity.emoji is None:
                    embed.add_field(name="Status Kustom", value=activity.name)
                elif activity.name is None:
                    embed.add_field(name="Status Kustom", value=activity.emoji)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Profil(client))
