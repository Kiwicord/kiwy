import discord
from discord.ext import commands
from db import *

class Send(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.err = ''

    @commands.command(aliases=['Send', 'SEND', 'pay', 'PAY'])
    async def send(self, ctx, member : discord.Member, amount : int=None):
        wallet_amt = await get_wallet(ctx.author.id)
        err_embed = discord.Embed(color=0x77dd77, title='')
        if member == ctx.author:
            e_embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Du kannst dir selber kein Geld senden!')
            await ctx.reply(embed=e_embed, mention_author=False)
            return
        if amount is None:
            err_embed.title = '<a:kc_bewegendeszeichenlmao:934397592178135121> Bitte gib den Betrag an!'
            await ctx.reply(embed=err_embed, mention_author=False)

        if wallet_amt < int(amount):
            embed_not_enough_money = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Du hast nicht genügend Geld!')
            await ctx.reply(embed=embed_not_enough_money, mention_author=False)
            return
        
        embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Geld gesendet!', description=f'Du hast erfolgreich **{int(amount):,}**🥝 an {member.mention} gesendet!')
        await open_profile(ctx.author.id)
        await open_profile(member.id)
        await update_wallet(member.id, amount=amount)
        await update_wallet(ctx.author.id, amount=-1*amount)
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Send(client))