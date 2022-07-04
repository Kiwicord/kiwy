import discord
from discord.ext import commands
from db import *
from emojis import Kiwicord

class Booster(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def booster(self, ctx, user: discord.Member=None):
        embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Booster von {ctx.author}')
        if user is None:
            await open_profile(ctx.author.id)
            booster = await get_booster(ctx.author.id)
            if booster == '1':
                embed.title = f'{Kiwicord.EXCLAMATION} Du hast momentan keinen Booster aktiv!'
                await ctx.reply(embed=embed, mention_author=False)
                return
            embed.description = f'Du bekommst momentan **{float(booster)*100}%** mehr 🥝'
            await ctx.reply(embed=embed, mention_author=False)
            return
        else:
            await open_profile(user.id)
            if await get_booster(user.id) == '1':
                embed.title = f'{Kiwicord.EXCLAMATION} Der User hat momentan keinen Booster aktiv!'
                await ctx.reply(embed=embed, mention_author=False)
                return
            embed.title = f'{Kiwicord.EXCLAMATION} Aktiver Booster von {user}'
            embed.description = f'{user.mention} bekommt momentan **{float(await get_booster(user.id))*100}%** mehr 🥝'
        await ctx.reply(embed=embed, mention_author=False)
async def setup(client):
    await client.add_cog(Booster(client))
