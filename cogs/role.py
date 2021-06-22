import discord
from discord.ext import commands

class RoleInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def roleinfo(self, ctx:commands.Context, *, role:discord.Role=None):
        if role is None:
            return await ctx.send("<:robin_palato:818892964457349220> **Sintaks tidak valid**! Tuliskan role yang ingin kamu lihat infonya!\nContoh: `r!roleinfo [role]`")

        embed = discord.Embed(
            title = f"Informasi Role",
            color = role.color
        )
        embed.add_field(name="Nama", value=f"{role.mention} (`{role.name}`)")
        embed.add_field(name="ID", value=role.id)
        embed.add_field(name="Warna", value=str(role.color).upper())

        if role.hoist is True:
            embed.add_field(name="Terpisah", value="✅")
        else:
            embed.add_field(name="Terpisah", value="❌")
        #
        if role.mentionable is True:
            embed.add_field(name="Bisa di-Mention", value="✅")
        else:
            embed.add_field(name="Bisa di-Mention", value="❌")
        #
        if role.managed is True:
            embed.add_field(name="Di-Manage", value="✅")
        else:
            embed.add_field(name="Di-Manage", value="❌")

        if role.is_default():
            embed.add_field(name="Role Default", value="✅")
        else:
            embed.add_field(name="Role Default", value="❌")
        #
        if role.is_premium_subscriber():
            embed.add_field(name="Role Booster", value="✅")
        else:
            embed.add_field(name="Role Booster", value="❌")
        #
        if role.is_bot_managed():
            embed.add_field(name="Diatur oleh Bot", value="✅")
        else:
            embed.add_field(name="Diatur oleh Bot", value="❌")

        embed.add_field(name="Posisi", value=role.position)
        embed.add_field(name="Dibuat pada", value=role.created_at.strftime("%d/%m/%Y %H:%M:%S UTC"))
        embed.add_field(name="Jumlah Member", value=len(role.members))

        if sum(len(izin) for izin in [perm[0] for perm in role.permissions if perm[1]]) < 1024:
            embed.add_field(name=f"Izin-Izin ({len([perm[0] for perm in role.permissions if perm[1]])})", value=f'`{", ".join([perm[0] for perm in role.permissions if perm[1]]).replace("_", " ")}`', inline=False)
        else:
            embed.add_field(name=f"Izin-Izin ({len([perm[0] for perm in role.permissions if perm[1]])})", value='Tidak muat', inline=False)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(RoleInfo(client))
