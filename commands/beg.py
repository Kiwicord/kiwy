import discord
from discord.ext import commands
from db import *
import random

class Beg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, int(60*5), commands.BucketType.user)
    async def beg(self, ctx):
        wallet = await get_wallet(ctx.author.id)

        PROB = ['yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no','no','no','no', ]

        income = random.randint(10, 250)
        embed_fail = discord.Embed(color=0xff6961, title='<a:7732exclamationred:939902470111522856> Erwischt!', description=f'Du wurdest beim Geld erbitten erwischt! Du zahlst **{income}**🥝 als Strafgeld.')
        embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Jemand zahlt!', description=f'Irgendwer hat dir **{int(income):,}**🥝 auf die Hand gegeben.')
        CHANCE = random.choice(PROB)
        if CHANCE == 'yes':
            await update_wallet(ctx.author.id, income)
            await ctx.reply(embed=embed, mention_author=False)
            return

        if CHANCE == 'no':
            if wallet < income:
                embed_no_money = discord.Embed(color=0xff6961, title='<a:7732exclamationred:939902470111522856> Ignoriert!', description=f'Du wurdest beim Geld erbitten ignoriert. Du bekommst kein Geld. Geh arbeiten du fauler Sack!')
                await ctx.reply(embed=embed_no_money, mention_author=False)
                return
            await update_wallet(ctx.author.id, -1*int(income))
            await ctx.reply(embed=embed_fail, mention_author=False)
            return

def setup(client):
    client.add_cog(Beg(client))
