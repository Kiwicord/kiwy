import discord
from discord.ext import commands, tasks
from flags import *
import asyncio
from emojis import Kiwicord
from db import *

class FlagQuiz(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def flag_setup(self, ctx):
        await setup_flag_quiz(ctx.guild.id, ctx.channel.id)
        await ctx.send(f'Dieser Channel wurde nun als Flaggen Channel eingerichtet')

    @commands.command()
    async def random_flag(self, ctx):
        guild = await get_channel(ctx.guild.id)
        channel = guild['channel']

        if ctx.channel.id == channel:

            random_flag = flags.aggregate([{'$sample': {'size': 1}}])
            for flag in random_flag:
                flag_embed = discord.Embed(color=0x77dd77, title='🚩 Errate diese Flagge!')
                link = flag['link']
                flag_embed.set_image(url=link)
                await ctx.send(embed=flag_embed)

            while True:
                response = await self.client.wait_for('message')
                if response.channel.id == channel:
                    if response.content == flag['name']:
                        income = random.randint(1, 10)
                        embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Richtig! Du hast **{income}**🥝 verdient.')
                        await update_wallet(response.author.id, income)
                        await response.reply(embed=embed)
                        await asyncio.sleep(1)
                        await self.random_flag(ctx)
                        return
                    else:
                        await response.add_reaction('❌')
    
def setup(client):
    client.add_cog(FlagQuiz(client))