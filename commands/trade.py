import discord
from discord.ext import commands
from db import *
from emojis import Kiwicord

class Trade(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gift(self, ctx, member: discord.Member, item_id: str):
        inv = await get_inv(ctx.author.id)
        try:
            item_obj = shop.find_one({'_id': item_id})
            if item_id in inv:
                bank.update_one({'_id': ctx.author.id}, {'$pull': {'items': item_id}})
                bank.update_one({'_id': member.id}, {'$push': {'items': item_id}})
                embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.TADA} Item verschickt!', description=f'Du hast {member.mention} das Item {item_obj["name"]} gegeben!')
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
    client.add_cog(Trade(client))
