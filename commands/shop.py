import discord
from discord.ext import commands
from db import *
from emojis import Kiwicord

class Shop(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def shop(self, ctx):
        await open_profile(ctx.author.id)
        shop_items = await get_shop_items()
        embed = discord.Embed(color=0x77dd77, title='Shop')
        embed.set_footer(text='Erfahre mehr über ein Item indem du .item <ID> benutzt.')

        for item in shop_items:
            embed.add_field(name=f"{Kiwicord.DOT} {item['name']}", value=f'Kostet: **{item["cost"]:,}**🥝\nID: `{item["_id"]}`', inline=False)
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Shop(client))