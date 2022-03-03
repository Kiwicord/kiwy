import discord
from discord.ext import commands
from db import *
from emojis import Kiwicord

class Use(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def use(self, ctx, item_id: str):
        await open_profile(ctx.author.id)
        inv = await get_inv(ctx.author.id)
        try:
            item_obj = await get_item(item_id)
            if item_id in inv:
                if item_obj['type'] == 'booster':
                    await use_booster(ctx.author.id, item_id)
                    embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.TADA} BOOSTER AKTIVIERT!', description=f'Du bekommst ab jetzt **{float(item_obj["value"])*100}%** mehr 🥝!')
                    await ctx.reply(embed=embed, mention_author=False)
                    return
                
                if item_obj['type'] == 'color':
                    role = discord.utils.get(ctx.guild.roles, id=int(item_obj['color']))
                    await use_item(ctx.author.id, item_obj['_id'])
                    await ctx.author.add_roles(role)
                    color_embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.TADA} Item aktiviert!', description=f'Du hast erfolgreich das Item **{item_obj["name"]}** aktiviert!')
                    await ctx.reply(embed=color_embed, mention_author=False)

                else:
                    await use_item(ctx.author.id, item_id)
                    embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.TADA} Item aktiviert!', description=f'Du hast erfolgreich das Item **{item_obj["name"]}** aktiviert!')
                    await ctx.reply(embed=embed, mention_author=False)
                    return
            else:
                error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Du besitzt dieses Item nicht!')
                await ctx.reply(embed=error, mention_author=False)
                return
        except TypeError:
            error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Dieses Item existiert nicht!')
            await ctx.reply(embed=error, mention_author=False)
            return

def setup(client):
    client.add_cog(Use(client))