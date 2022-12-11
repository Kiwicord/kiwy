import discord
from discord.ext import commands
from discord.ui import Button, View
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
    async def flag(self, ctx):
        guild = await get_channel(ctx.guild.id)
        channel = guild['channel']

        if ctx.channel.id == channel:
            random_flag = flags.aggregate([{'$sample': {'size': 1}}])
            
            for flag in random_flag:
                flag_embed = discord.Embed(color=0x77dd77, title='🚩 Errate diese Flagge!')
                link = flag['link']
                flag_embed.set_image(url=link)

                button = Button(label='Flagge überspringen', style=discord.ButtonStyle.green, emoji='🤔')

                view = View()
                view.add_item(button)

                async def next_flag(interaction: discord.Interaction):
                    await update_wallet(ctx.author.id, amount= -1*100)
                    await interaction.channel.purge(limit=100)
                    await self.flag(ctx)
                    await ctx.author.send('Dir wurden **100🥝** abgezogen, weil du eine Flagge in <#987404727102873641> übersprungen hast.')
                    return
                
                button.callback = next_flag
                
                await ctx.send(embed=flag_embed, view=view)
                

            while True:
                response = await self.client.wait_for('message')
                if response.channel.id == channel:
                    if response.content == flag["name"]:
                        income = random.randint(5, 15)
                        embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Richtig! Du hast **{income}**🥝 verdient.')
                        await update_wallet(response.author.id, income)
                        await response.reply(embed=embed)
                        await asyncio.sleep(1)
                        await response.channel.purge(limit=100) 
                        await self.flag(ctx) 
                        return

                    if response.embeds: # if message has embed (skipped flag) 
                        return

                    if response.content != flag['name']:
                        await response.add_reaction('❌')
    
    @commands.command()
    async def add(self, ctx, link: str, *, name: str):
        if ctx.author.id == 733403498766401554:
            await add_flag(link, name)
            await ctx.send(f'Die Flagge von **{name}** wurde erfolgreich zur Datenbank hinzugefügt! 😺\n🔗 <{link}>')
        else:
            raise commands.CommandNotFound
    
async def setup(client):
    await client.add_cog(FlagQuiz(client))
