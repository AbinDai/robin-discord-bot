import discord, requests, datetime, os
from discord.ext import commands

class Spotipai(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def spotify(self, ctx, orang:discord.Member=None):
        orang = ctx.author if not orang else orang

        crotify = next((activity for activity in orang.activities if isinstance(activity, discord.Spotify)), None)

        if crotify is None:
            if orang == ctx.author:
                embed = discord.Embed(
                    description = f"Kamu sedang tidak mendengarkan Spotify.",
                    color = 0xff0000
                )
                return await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(
                    description = f"{orang.mention} sedang tidak mendengarkan Spotify.",
                    color = 0xff0000
                )
                return await ctx.reply(embed=embed)

        embed = discord.Embed(
            title= f"Yang Sedang Didengar oleh {orang.name}",
            color= crotify.color
        )
        embed.set_author(name="Spotify", icon_url="https://user-images.githubusercontent.com/75367930/120773067-293cc680-c54b-11eb-950e-a4518c464124.png")
        embed.add_field(name="Judul", value=f"[{crotify.title}](https://open.spotify.com/track/{crotify.track_id})")
        embed.add_field(name="Artis", value=crotify.artist)
        embed.add_field(name="Album", value=crotify.album)

        waktusekarang = datetime.datetime.utcnow() - crotify.start
        durasilagu = crotify.duration
		
        bar = requests.get(f"https://api.jastinch.xyz/progressbar?key={os.environ['JASTINCH_API']}&now={waktusekarang.total_seconds()}&max={durasilagu.total_seconds()}").json()
        embed.add_field(name="⠀", value=f"{str(waktusekarang)[:-7]}   `{bar['bar']}`   {str(durasilagu)[:-7]}")

        embed.set_footer(text=f"Pendengar: {orang}", icon_url=orang.avatar_url)
        #
        try:
            embed.set_thumbnail(url=crotify.album_cover_url)
        except:
            pass
        #
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Spotipai(client))
