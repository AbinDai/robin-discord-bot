import discord, os, requests
from discord.ext import commands

class KomenYT(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("komenyt.py siap")

    @commands.command(aliases=['ytcmt', 'cmtyt'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtubecomment(self, ctx, *msg):
        if not msg:
            await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Kamu tidak menuliskan isi komentar!\nContoh: `r!ytcmt ini adalah komentar`")
        else:
            async with ctx.typing():
                komen = "%20".join(msg)

                #conversi list jadi string
                def Convert(string): 
                    li = list(string.split(" "))
                    return li 
                
                str1 = f"{ctx.author.display_name}"
                pengirim = Convert(str1)

                pengyrim = "%20".join(pengirim)

                response = requests.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={ctx.author.avatar_url_as(format='png', size=4096)}&username={pengyrim}&comment={komen}")

                file = open("youtube-comment.png", "wb")
                file.write(response.content)
                file.close()

                await ctx.send(file=discord.File("youtube-comment.png"))

                os.remove("youtube-comment.png")

def setup(client):
    client.add_cog(KomenYT(client))
