import discord
from discord.ext import commands
from db import *
import random

EMOJIS = ['<:kiwi_disguised:941275906377396225>', '<:kiwi_hearts:941275654685597696>', '<:kiwi_sunglasses:941275906197049355>']

class Slots(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Slots', 'SLOTS'])
    async def slots(self, ctx, amt : int):
        await open_profile(ctx.author.id)
        amt = int(amt)
        wallet_amount = await get_wallet(ctx.author.id)

        chance1 = random.choice(EMOJIS)
        chance2 = random.choice(EMOJIS)
        chance3 = random.choice(EMOJIS)


        if wallet_amount < amt:
            not_enough_money = discord.Embed(color=0xff6961, title='<a:7732exclamationred:939902470111522856> Nicht genügend Geld!')
            await ctx.reply(embed=not_enough_money, mention_author=False)
            return
        
        if chance1 == chance2 and chance1 == chance3:
            win_embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Gewonnen!', description=f'> {chance1}  {chance2}  {chance3}\nDu hast **{amt:,}**🥝 verdient.')
            await update_wallet(ctx.author.id, amt)
            await ctx.reply(embed=win_embed, mention_author=False)
            return
        else:
            loose_embed = discord.Embed(color=0xff6961,title='<a:7732exclamationred:939902470111522856> Verloren!', description=f'> {chance1}  {chance2}  {chance3}\nDu hast **{amt:,}**🥝 verloren.')
            await update_wallet(ctx.author.id, -1*amt)
            await ctx.reply(embed=loose_embed, mention_author=False)
            return
        

def setup(client):
    client.add_cog(Slots(client))