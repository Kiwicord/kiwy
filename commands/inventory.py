import discord
from discord.ext import commands
from db import *
from emojis import Kiwicord

class Inventory(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Inventory', 'INVENTORY', 'inv', 'Inv', 'INV'])
    async def inventory(self, ctx, member: discord.Member=None):
        await open_profile(ctx.author.id)
        inv = await get_inv(ctx.author.id)
        embed = discord.Embed(color=0x77dd77, title=f"{Kiwicord.EXCLAMATION} {ctx.author}'s Inventar")

        if member is None:
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
        else:
            await open_profile(member.id)
            embed = discord.Embed(color=0x77dd77, title=f"{Kiwicord.EXCLAMATION} {member}'s Inventar")
            inv_member = await get_inv(member.id)
            if len(inv_member) == 0:
                embed.title = f'{Kiwicord.EXCLAMATION} Der User besitzt momentan keine Items!'
                embed.set_footer(text='Besuche den Shop indem du .shop ausführst um Items zu kaufen.')
                await ctx.reply(embed=embed, mention_author=False)
                return

            for item in await get_shop_items():
                amount = inv_member.count(item["_id"])
                if amount > 0:
                    embed.add_field(name=f"{Kiwicord.DOT} {item['name']}", value=f"ID: `{item['_id']}`\nStückzahl: `{amount}`", inline=False)
            embed.set_footer(text='Erfahre mehr über ein Item indem du .item <ID> benutzt.')
            await ctx.reply(embed=embed, mention_author=False)
    

def setup(client):
    client.add_cog(Inventory(client))
