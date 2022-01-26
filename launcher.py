import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
from db import *

from commands.balance import Balance
from commands.deposit import Deposit
from commands.withdraw import Withdraw

PREFIX = '.'

load_dotenv()

client = commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def setup():
    await client.wait_until_ready()
    client.add_cog(Balance(client))
    client.add_cog(Deposit(client))
    client.add_cog(Withdraw(client))

client.loop.create_task(setup())

client.run(getenv('TOKEN'))