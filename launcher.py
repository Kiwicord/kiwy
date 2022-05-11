import discord
from discord.ext import commands
from db import *
import os

PREFIX = '.'

client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')

@client.event
async def on_ready():
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

for filename in os.listdir("./commands"):
	if filename.endswith(".py"):
		client.load_extension(f"commands.{filename[:-3]}")

client.run('NzMzOTY2MzgwNDk5NTk5MzYx.XxK1dQ.erHhL_ZovZyaD1Ao67eWLDbR1UM')