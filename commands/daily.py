import discord
from discord.ext import commands
from db import *
import random

class Daily(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Daily', 'DAILY'])
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        booster = await get_booster(ctx.author.id)
        income = random.randint(10000, 20000) * float(booster)
        embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Geld abgeholt!', description=f'Du hast dein tägliches Geld in Höhe von **{int(income):,}**🥝 abgeholt!')
        await update_wallet(ctx.author.id, income)
        await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
    await client.add_cog(Daily(client))