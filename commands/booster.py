import discord
from discord.ext import commands
from db import *
import random

class Booster(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def get(self, ctx):
        booster = await get_booster(ctx.author.id)
        booster = float(booster)
        

        normal_income = random.randint(1, 100)
        final_income = normal_income * booster
        await ctx.send(f'Normal Income: **{normal_income}**\nFinal Income: **{final_income}**')
        await update_wallet(ctx.author.id, final_income)

def setup(client):
    client.add_cog(Booster(client))