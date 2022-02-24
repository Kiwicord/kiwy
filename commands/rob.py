import discord
from discord.ext import commands
from db import *
import random

class Rob(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Rob', 'ROB'])
    async def rob(self, ctx, user : discord.Member):
        await open_profile(ctx.author.id)
        await open_profile(user.id)

        START_AMOUNT = 10000
        CHANCE = ['yes', 'no']
        chance = random.choice(CHANCE)
        
        try:
            target_wallet = await get_wallet(user.id)
            robber_wallet = await get_wallet(ctx.author.id)
            rob_amount = random.randrange(int(target_wallet))
            rob_embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Ausgeraubt!', description=f'Du hast {user.mention} ausgeraubt und dadurch **{int(rob_amount):,}**🥝 verdient.')

            if user.id == 712341730480881707 or 400341760569507841:
                return
                
            if robber_wallet >= START_AMOUNT:

                if rob_amount <= 3:
                    fail_embed = discord.Embed(color=0xff6961, title='<a:7732exclamationred:939902470111522856> Der User hat nicht genügend Geld!')
                    await ctx.reply(embed=fail_embed, mention_author=False)
                    return
                
                if chance == 'yes':
                    await update_wallet(user.id, -1*rob_amount)
                    await update_wallet(ctx.author.id, rob_amount)
                    await ctx.reply(embed=rob_embed, mention_author=False)

                elif chance == 'no':
                    failed_rob = discord.Embed(color=0xff6961, title='<a:7732exclamationred:939902470111522856> Polizei alamiert!', description=f'Du wurdest beim ausrauben erwischt. Du zahlst **{START_AMOUNT:,}**🥝 als Strafe')
                    await update_wallet(ctx.author.id, -1*START_AMOUNT)
                    await ctx.reply(embed=failed_rob, mention_author=False)
                    return
            else:
                not_enough_money = discord.Embed(color=0xff6961, title='<a:7732exclamationred:939902470111522856> Nicht genügend Geld!', description=f'Du brauchst mindestens **{START_AMOUNT:,}**🥝 um einen Raub zu starten.')
                await ctx.reply(embed=not_enough_money, mention_author=False)
                    
        except ValueError:
            fail_embed = discord.Embed(color=0xff6961, title='<a:7732exclamationred:939902470111522856> Der User hat nicht genügend Geld!')
            await ctx.reply(embed=fail_embed, mention_author=False)

def setup(client):
    client.add_cog(Rob(client))
