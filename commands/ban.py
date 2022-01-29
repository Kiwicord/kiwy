import discord
from discord.ext import commands
from db import *
import random

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason='Kein Grund angegeben'):
        embed2 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Gebannt!', description=f'Du wurdest von **{ctx.guild.name}** gebannt.\n<:kc_punkt:924409447147786261> **{reason}**')
        await member.send(embed=embed2)
        await member.ban(reason=reason)
        embed1 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Gebannt!', description=f'Der Member {member.mention} wurde gebannt.')
        await ctx.send(embed=embed1)

def setup(client):
    client.add_cog(Ban(client))