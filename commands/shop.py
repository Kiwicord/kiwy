import discord
from discord.ext import commands
from db import *
from emojis import Kiwicord

class Shop(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def buy(self, ctx, id: str):
        error = discord.Embed(color=0x77dd77)
        money = await get_wallet(ctx.author.id)
        try:
            item = shop.find_one({'_id': id})
            if money >= item["cost"]:
                await buy(item['_id'], ctx.author.id)
                embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Gekauft', description=f'Du hast erfolgreich **{item["name"]}** für **{item["cost"]:,}**🥝 gekauft!')
                await ctx.reply(embed=embed, mention_author=False)
            else:
                error.title = f'{Kiwicord.EXCLAMATION} Du hast nicht genügend Geld!'
                await ctx.reply(embed=error, mention_author=False)
                return
        except TypeError:
            error.title = f'{Kiwicord.EXCLAMATION} Dieses Item existiert nicht!'
            await ctx.reply(embed=error, mention_author=False)
            return

    @commands.command()
    async def inv(self, ctx):
        inv = await get_inv(ctx.author.id)
        embed = discord.Embed(color=0x77dd77, title=f"{Kiwicord.EXCLAMATION} {ctx.author}'s Inventar")

        for item in inv:
            amount = inv.count(item)
            i = shop.find_one({'_id': item})
            embed.add_field(name=i['name'], value=f"{i['description']}", inline=False)
            
        await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command()
    async def shop(self, ctx):
        shop_items = await get_shop_items()
        embed = discord.Embed(color=0x77dd77, title='Shop')

        for item in shop_items:
            embed.add_field(name=f"{Kiwicord.DOT} {item['name']}", value=f'{item["description"]}\nKostet: **{item["cost"]:,}**🥝', inline=False)
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Shop(client))