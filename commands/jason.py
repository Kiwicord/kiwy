import discord
from discord.ext import commands

class Jason(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def jason(self, ctx):
        embed =  discord.Embed(title='', description='<@745717254678904862>')
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Jason(client))