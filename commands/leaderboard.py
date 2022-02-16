import discord
from discord.ext import commands
from db import *

class Leaderboard(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command(aliases=['Leaderboard','lb', 'top', 'rich', 'Lb', 'Top', 'Rich', 'LEADERBOARD', 'LB', 'TOP', 'RICH'])
    async def leaderboard(self, ctx):
        data = bank.find().sort('wallet' , -1)
        embed = discord.Embed(title='<a:kc_bewegendeszeichenlmao:934397592178135121> Leaderboard', description='Top 5 der reichsten User', color=0x77dd77)

        for i, x in enumerate(data, 1):
            embed.add_field(name=f'{i}.', value=f"<@{str(x['_id'])}>: **{int(x['wallet']):,}**🥝", inline=False)
            if i == 5:
                await ctx.reply(embed=embed, mention_author=False)
                return

    

def setup(client):
    client.add_cog(Leaderboard(client))
