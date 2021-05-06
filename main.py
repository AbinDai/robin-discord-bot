#impor segalanya#
import discord, os, json, datetime
from discord.ext import commands, tasks
from itertools import cycle

#===============================================================================================

#setel prefix + bikin variabel command
client = commands.Bot(
    command_prefix=[
        "r!",
        "R!",
        "robin ",
        "ROBIN ",
        "Robin ",
        "rObin ",
        "roBin ",
        "robIn ",
        "robiN ",
        "RObin ",
        "rOBin ",
        "roBIn ",
        "robIN ",
        "ROBin ",
        "rOBIn ",
        "roBIN "
    ], 
    case_insensitive=True
)

#===============================================================================================

#hilangkan help bawaan
client.remove_command('help')

#===============================================================================================

#daftarin cog
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#===============================================================================================
        
#isi status
status = cycle([
    'r!help',
    'r!help allcommands'
])

#===============================================================================================

#tulisan siap pada terminal dan status yg berganti2
@client.event
async def on_ready():
    change_status.start()
    print('main.py, siap ngebut!')
    
    channel = client.get_channel(839749452322963466)
    await channel.send(f"🟢 {self.client.user} telah online!")
    
#===============================================================================================

#looping status
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    
#===============================================================================================
    
#command afk
#awokawok gw buatnya dsni karena command ini gabisa dimasukin di cogs :'v
#mengsedih
async def update_data(afk, user):
    if not f"{user.id}" in afk:
        afk[f"{user.id}"] = {}
        afk[f"{user.id}"]["AFK"] = "False"

@client.event
async def on_member_join(member):
    print(f"{member} bergabung!")
    with open("afk.json", "r") as f:
        afk = json.load(f)

    await update_data(afk, member)

    with open("afk.json", "w") as f:
        json.dump(afk, f)

@client.event
async def on_message(message):
    with open("afk.json", "r") as f:
        afk = json.load(f)

    for x in message.mentions:
        if afk[f"{x.id}"]["AFK"] == "True":
            if message.author.bot:
                return
            await message.channel.send(f"{x} saat ini sedang AFK.")

    if not message.author.bot:
        await update_data(afk, message.author)

        if afk[f"{message.author.id}"]["AFK"] == "True":
            await message.channel.send(f"**Selamat datang kembali {message.author.mention}!** AFK-mu sekarang kucabut.", delete_after=5)
            afk[f"{message.author.id}"]["AFK"] = "False"
            with open("afk.json", "w") as f:
                json.dump(afk, f)
            await message.author.edit(nick=f"{message.author.display_name[6:]}")

    with open("afk.json", "w") as f:
        json.dump(afk, f)

    await client.process_commands(message)


    
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def afk(ctx, *, reason=None):
    with open("afk.json", "r") as f:
        afk = json.load(f)

    if not reason:
        reason = "jauh dari keyboard"

    afk[f"{ctx.author.id}"]["AFK"] = "True"
    await ctx.reply(f'AFK-mu sekarang kuatur ke "{reason}."')

    with open("afk.json", "w") as f:
        json.dump(afk, f)
        
    await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")
   
#===============================================================================================        

#nyalakan bot.
client.run(os.environ['DISCORD_TOKEN'])
