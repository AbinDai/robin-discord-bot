#impor segalanya#
import discord, os, datetime
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from itertools import cycle

#===============================================================================================

#setel prefix + bikin variabel client
intents = discord.Intents.all()
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
    case_insensitive=True,
    intents=intents
)
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)

#===============================================================================================

#hilangkan help bawaan
client.remove_command('help')

#===============================================================================================

#daftarin cog
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
for filename in os.listdir('./cogs/slashes'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#===============================================================================================
        
#isi status
status = cycle([
    'r!help',
    "r!vote"
])

#===============================================================================================

#tulisan siap pada terminal dan status yg berganti2
@client.event
async def on_ready():
    change_status.start()
    print('main.py, siap ngebut!')
    
    channel = client.get_channel(839749452322963466)
    await channel.send(f"🟢 {client.user} telah online!")
    await client.get_channel(853227353169199115).send(f"🟢 {client.user} telah online!")
    
#===============================================================================================

#looping status
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    
#===============================================================================================

#nyalakan bot.
client.run(os.environ['BOT_TOKEN'])
