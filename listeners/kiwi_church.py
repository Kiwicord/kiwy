import discord
from discord.ext import commands
from db import *
import random

class KiwiChurch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 934860620745015296:
            if message.content != '<:kiwi_beten:934860398304329778>':
                await message.delete()
                
def setup(client):
    client.add_cog(KiwiChurch(client))