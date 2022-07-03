import discord
from discord.ext import commands
from db import *
from emojis import Kiwicord

class Items(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def items(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author

        active_items = await get_active_items(user.id)

        if len(active_items) == 0:
            err = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Du hast momentan keine aktiven Items!')
            await ctx.reply(embed=err, mention_author=False)
            return

        embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Deine aktiven Items')

        for item in await get_shop_items():
            amount = active_items.count(item["_id"])
            if amount > 0:
                embed.add_field(name=f"{Kiwicord.DOT} {item['name']}", value=f'ID: `{item["_id"]}`', inline=False)

        await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
    await client.add_cog(Items(client))