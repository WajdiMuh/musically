import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '-')

musicqueue = []

@client.event
async def on_ready():
    print(f'{client.user.display_name} has connected to Discord!')

@client.command(aliases=['p'])
async def play(ctx,songname):
    if len(musicqueue) == 0:
        await ctx.send(f'playing {songname}')
    else:
        await ctx.send(f'{songname} added to queue')
    musicqueue.append(songname)

@client.command()
async def clear(ctx):
    del musicqueue[:]
    await ctx.send(f'queue cleared')

@client.command(aliases=['q'])
async def queue(ctx):
    if len(musicqueue) == 0:
        await ctx.send(f'the queue is empty')
    else:
        await ctx.send("\n".join(musicqueue))

client.run(TOKEN)