import discord
from discord.ext import commands
from db import *
import os

PREFIX = '.'

client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    # os.system('cls')
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 733403498766401554:
        client.load_extension(f'commands.{extension}')

@client.command()   
async def unload(ctx, extension):
    if ctx.author.id == 733403498766401554:
        client.unload_extension(f'commands.{extension}')

async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"commands.{filename[:-3]}")

async def main():
    async with client:
        await load_extensions()
        await client.start('NzMzOTY2MzgwNDk5NTk5MzYx.Gn-CR0.zLCfOl-Yg3Wwyuy2LtxzMwYFKu50SnZuCf6_Wg')

asyncio.run(main())