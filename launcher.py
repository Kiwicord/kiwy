import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
from db import *

from commands.balance import Balance
from commands.deposit import Deposit
from commands.withdraw import Withdraw
from commands.work import Work
from commands.changelog import Changelog
# from commands.ban import Ban
from commands.send import Send
from commands.daily import Daily

from error import CommandErrorHandler

from listeners.kiwi_church import KiwiChurch

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
    client.add_cog(Work(client))
    client.add_cog(CommandErrorHandler(client))
    client.add_cog(Changelog(client))
    client.add_cog(Leaderboard(client))
    # client.add_cog(Ban(client))
    client.add_cog(KiwiChurch(client))
    # client.add_cog(Shop(client))
    client.add_cog(Send(client))
    client.add_cog(Daily(client))

client.loop.create_task(setup())

client.run('NzMzOTY2MzgwNDk5NTk5MzYx.XxK1dQ.MEildqfX5bMb13iWqfSvcC62va8')
