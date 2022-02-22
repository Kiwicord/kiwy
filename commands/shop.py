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
                if item['_id'] == 'waterpass':
                    channel = self.client.get_channel(942179139660685322)
                    await channel.send(f'{ctx.author} hat sich gerade eben den **Waterpass** gekauft! <@733403498766401554> <@480265913656934410>')
                await buy(item['_id'], ctx.author.id)
                await update_wallet(ctx.author.id, -1*int(item["cost"]))
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

        if len(inv) == 0:
            embed.title = f'{Kiwicord.EXCLAMATION} Du hast momentan keine Items!'
            embed.set_footer(text='Besuche den Shop indem du .shop ausführst um Items zu kaufen.')
            await ctx.reply(embed=embed, mention_author=False)
            return

        for item in await get_shop_items():
            amount = inv.count(item["_id"])
            if amount > 0:
                embed.add_field(name=f"{Kiwicord.DOT} {item['name']}", value=f"ID: `{item['_id']}`\nStückzahl: `{amount}`", inline=False)
        embed.set_footer(text='Erfahre mehr über ein Item indem du .item <ID> benutzt.')
        await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command()
    async def shop(self, ctx):
        shop_items = await get_shop_items()
        embed = discord.Embed(color=0x77dd77, title='Shop')
        embed.set_footer(text='Erfahre mehr über ein Item indem du .item <ID> benutzt.')

        for item in shop_items:
            embed.add_field(name=f"{Kiwicord.DOT} {item['name']}", value=f'Kostet: **{item["cost"]:,}**🥝\nID: `{item["_id"]}`', inline=False)
        await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command()
    async def item(self, ctx, item_id: str):
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
    
    @commands.command()
    async def use(self, ctx, item_id: str):
        inv = await get_inv(ctx.author.id)
        try:
            item_obj = shop.find_one({'_id': item_id})
            if item_obj['type'] == 'collectible':
                error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Dieses Item kannst du nicht benutzen!')
                await ctx.reply(embed=error, mention_author=False)
                return
            else:
                if item_id in inv:
                    bank.update_one({'_id': ctx.author.id}, {'$pull': {'items': item_id}})
                    bank.update_one({'_id': ctx.author.id}, {'$set': {'active_booster': item_obj['value']}})
                    embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.TADA} BOOSTER AKTIVIERT!', description=f'Du bekommst ab jetzt **{float(item_obj["value"])*100}%** mehr 🥝!')
                    await ctx.reply(embed=embed, mention_author=False)
                    return
                else:
                    error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Du besitzt dieses Item nicht!')
                    await ctx.reply(embed=error, mention_author=False)
                    return
        except TypeError:
            error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Dieses Item existiert nicht!')
            await ctx.reply(embed=error, mention_author=False)
            return

def setup(client):
    client.add_cog(Shop(client))