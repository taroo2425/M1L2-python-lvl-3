import discord
import random
from discord.ext import commands
from config import token

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah login sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send(f'halo aku adalah {client.user}!')

    #tugas
    if message.content.startswith('aku keren ngga?'):
        await message.channel.send("kamu adalah orang paling keren!!")

    elif message.content.startswith("$HA"):
        if len(message.content) > 4:
            count_HA = int(message.content[4:])
        else:
            count_HA = 4
        await message.channel.send("HA" * count_HA and "!!")

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Ini adalah echo-bot yang dibuat dengan pustaka discord.py!')

@client.command()
async def info(ctx):
    await ctx.send("""
/info = informasi tentang bot ini
/about = about atau tentang bot
/on_message = pesan dari user kepada bot
""")
    
#tugas 
@client.command()
async def lempar_dadu(ctx):
    dadu = random.randint(1, 6)
    await ctx.send(dadu)


client.run(token)

#MTI2NzQ3NTk4NTczODEwNDk2NQ.GEP-Gw.LIShIgNwscS2Ap_RvKcrRMSefw1v19fbP7yCpA