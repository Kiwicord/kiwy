import discord
from discord.ext import commands
from db import *

class Deposit(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.err = ''

    @commands.command(aliases=['dep'])
    async def deposit(self, ctx, amount=None):
        wallet_amt = await get_wallet(ctx.author.id)
        err_embed = discord.Embed(color=0x77dd77, title='')
        if amount is None:
            err_embed.title = '<a:kc_bewegendeszeichenlmao:934397592178135121> Bitte gib den Betrag an!'
            await ctx.send(embed=err_embed)

        if amount == 'all':
            amount = int(wallet_amt)
            if wallet_amt <= 0:
                embed_not_enough_money = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Du hast nicht genügend Geld!')
                await ctx.send(embed=embed_not_enough_money)
                return

        if wallet_amt < int(amount):
            embed_not_enough_money = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Du hast nicht genügend Geld!')
            await ctx.send(embed=embed_not_enough_money)
            return
        
        embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Überwiesen!', description=f'Du hast erfolgreich **{int(amount):,}**🥝 auf deine Bank überwiesen!')
        await open_profile(ctx.author.id)
        await deposit_amt(ctx.author.id, amount=int(amount))
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Deposit(client))