import discord
from discord.ext import commands
from db import *
from emojis import Kiwicord

class Buy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def buy(self, ctx, id: str):
        await open_profile(ctx.author.id)
        error = discord.Embed(color=0x77dd77)
        money = await get_wallet(ctx.author.id)
        try:
            item = shop.find_one({'_id': id})
            if money >= item["cost"]:
                if item['_id'] == 'waterpass':
                    channel = self.client.get_channel(945401190705926144)
                    await channel.send(f'{ctx.author} hat sich gerade eben den **Waterpass** gekauft! <@733403498766401554> <@480265913656934410>')
                await buy(item['_id'], ctx.author.id)
                await update_wallet(ctx.author.id, -1*int(item["cost"]))
                embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Gekauft', description=f'Du hast erfolgreich **{item["name"]}** für **{item["cost"]:,}**🥝 gekauft!')
                await ctx.reply(embed=embed, mention_author=False)
            else:
                error.title = f'{Kiwicord.EXCLAMATION} Du hast nicht genügend Geld!'
                await ctx.reply(embed=error, mention_author=False)
                return
        except TypeError:
            error.title = f'{Kiwicord.EXCLAMATION} Dieses Item existiert nicht!'
            await ctx.reply(embed=error, mention_author=False)
            return  
    

async def setup(client):
    await client.add_cog(Buy(client))
