import discord
from discord.ext import commands
from db import *
from emojis import *

class Item(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def item(self, ctx, item_id: str):
        await open_profile(ctx.author.id)
        inv = await get_inv(ctx.author.id)
        try:
            amount = inv.count(item_id)
            item = shop.find_one({'_id': item_id})
            embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Informationen über: {item["name"]}', description=f'{item["description"]}\n\nName: **{item["name"]}**\nKostet: **{item["cost"]:,}**🥝\nID: `{item_id}`\n\nDu besitzt: `{amount}`')
            embed.set_thumbnail(url=item['image_url'])
            embed.set_footer(text=f'Um dieses Item zu kaufen, benutze: .buy {item_id}')
            await ctx.reply(embed=embed, mention_author=False)
        except TypeError:
            error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Dieses Item gibt es nicht!')
            await ctx.reply(embed=error, mention_author=False)
    
async def setup(client):
    await client.add_cog(Item(client))