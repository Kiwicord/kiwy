import discord
from discord.ext import commands
from db import *
from emojis import Kiwicord

class Knast(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def knastadd(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, id=946455955418284034)
        role_standard = discord.utils.get(ctx.guild.roles, id=899574259532300292)
        embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} {member} wurde in den Knast geschickt!')
        await ctx.reply(embed=embed, mention_author=False)
        await member.add_roles(role)
        await member.remove_roles(role_standard)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def knastremove(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, id=946455955418284034)
        role_standard = discord.utils.get(ctx.guild.roles, id=899574259532300292)
        embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} {member} wurde aus dem Knast geschickt!')
        await ctx.reply(embed=embed, mention_author=False)
        await member.add_roles(role_standard)
        await member.remove_roles(role)

def setup(client):
    client.add_cog(Knast(client))