import discord
from discord.ext import commands
from db import *

class A(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def a(self, ctx, *, amount=None):
        amount = int(amount)
        await open_profile(ctx.author.id)
        await update_wallet(ctx.author.id, amount)

async def setup(client):
    await client.add_cog(A(client))