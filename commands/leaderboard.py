import discord
from discord.ext import commands
from db import *

class Leaderboard(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def leaderboard(self, ctx):
        data = bank.find().sort('wallet' , -1)
        embed = discord.Embed(title='Leaderboard', description='Top 10 reichsten Spieler', color=0x77dd77)

        for index, value in enumerate(data, 1):
            embed.add_field(name=f'{index}.', value=f'<@{str(value['_id'])}>: {str(value['wallet'])}', inline=False)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Leaderboard(client))