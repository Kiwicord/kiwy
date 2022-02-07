import discord
from discord.ext import commands
from db import *
import random

class Daily(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        income = random.randint(1000, 10000)
        embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Geld abgeholt!', description=f'Du hast dein tägliches Geld in Hähe von **{int(income):,}**🥝 abgeholt!')
        await update_wallet(ctx.author.id, income)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Daily(client))