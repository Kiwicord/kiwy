import discord
from discord.ext import commands
from db import *

class Withdraw(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.err = ''

    @commands.command(aliases=['with', 'With', 'WITH'])
    async def withdraw(self, ctx, amount=None):
        bank_amt = await get_bank(ctx.author.id)
        err_embed = discord.Embed(color=0x77dd77, title='')
        if amount is None:
            err_embed.title = '<a:kc_bewegendeszeichenlmao:934397592178135121> Bitte gib den Betrag an!'
            await ctx.reply(embed=err_embed, mention_author=False)
            return

        if amount == 'all':
            amount = int(bank_amt)
            if bank_amt < 0:
                embed_not_enough_money = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Du hast nicht genügend Geld!')
                await ctx.reply(embed=embed_not_enough_money, mention_author=False)
                return

        if bank_amt < int(amount):
            embed_not_enough_money = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Du hast nicht genügend Geld!')
            await ctx.reply(embed=embed_not_enough_money, mention_author=False)
            return
        
        embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Abgehoben!', description=f'Du hast erfolgreich **{int(amount):,}**🥝 von deiner Bank abgehoben!')
        await open_profile(ctx.author.id)
        await withdraw_amt(ctx.author.id, amount=int(amount))
        await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
    await client.add_cog(Withdraw(client))