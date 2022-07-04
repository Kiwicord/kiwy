import discord
from discord.ext import commands
from emojis import Kiwicord
from google_play_cards import SERIAL
import random
from discord.ui import Button, View
import asyncio

class GooglePlayCardGenerator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def googleplay(self, ctx):
        
        await ctx.message.delete()

        view = View()

        button5 = Button(label='5 Euro', emoji='🎫', style=discord.ButtonStyle.green)
        button15 = Button(label='15 Euro', emoji='🎫', style=discord.ButtonStyle.green)
        button25 = Button(label='25 Euro', emoji='🎫', style=discord.ButtonStyle.green)
        button50 = Button(label='50 Euro', emoji='🎫', style=discord.ButtonStyle.green)

        embed = discord.Embed(color=0x77dd77, title='🎫 Google Play Karten Generator', description='Bitte wähle das Guthaben aus, um deine Google Play Karte zu erstellen.')
        embed.set_thumbnail(url='https://lh3.googleusercontent.com/k-2BsI5KgLC2JxQd2rFA-3RHg8-tvoXjinZFNvZLnGlbcxR8xkVM9GW3tqBK5xbTSJKr3-Ei2SVuDoAuYaR3-AL5DVlV5vNj10d6x-604UYNa0sfGEU=s0')
        
        async def callback_5(interaction):
            button5.disabled = True
            embed1 = discord.Embed(color=0x77dd77, title='🎫 Deine 5 Euro Google Play Karte:', description=random.choice(SERIAL))
            embed1.set_thumbnail(url='https://lh3.googleusercontent.com/k-2BsI5KgLC2JxQd2rFA-3RHg8-tvoXjinZFNvZLnGlbcxR8xkVM9GW3tqBK5xbTSJKr3-Ei2SVuDoAuYaR3-AL5DVlV5vNj10d6x-604UYNa0sfGEU=s0')
            await interaction.response.send_message(embed=embed1, ephemeral=True)
            await msg.edit(view=view)
            return
        

        async def callback_15(interaction):
            button15.disabled = True
            embed1 = discord.Embed(color=0x77dd77, title='🎫 Deine 15 Euro Google Play Karte:', description=random.choice(SERIAL))
            embed1.set_thumbnail(url='https://lh3.googleusercontent.com/k-2BsI5KgLC2JxQd2rFA-3RHg8-tvoXjinZFNvZLnGlbcxR8xkVM9GW3tqBK5xbTSJKr3-Ei2SVuDoAuYaR3-AL5DVlV5vNj10d6x-604UYNa0sfGEU=s0')
            await interaction.response.send_message(embed=embed1, ephemeral=True)
            await msg.edit(view=view)
            return

        async def callback_25(interaction):
            button25.disabled = True
            embed1 = discord.Embed(color=0x77dd77, title='🎫 Deine 25 Euro Google Play Karte:', description=random.choice(SERIAL))
            embed1.set_thumbnail(url='https://lh3.googleusercontent.com/k-2BsI5KgLC2JxQd2rFA-3RHg8-tvoXjinZFNvZLnGlbcxR8xkVM9GW3tqBK5xbTSJKr3-Ei2SVuDoAuYaR3-AL5DVlV5vNj10d6x-604UYNa0sfGEU=s0')
            await interaction.response.send_message(embed=embed1, ephemeral=True)
            await msg.edit(view=view)
            return

        async def callback_50(interaction):
            button50.disabled = True
            embed1 = discord.Embed(color=0x77dd77, title='🎫 Deine 50 Euro Google Play Karte:', description=random.choice(SERIAL))
            embed1.set_thumbnail(url='https://lh3.googleusercontent.com/k-2BsI5KgLC2JxQd2rFA-3RHg8-tvoXjinZFNvZLnGlbcxR8xkVM9GW3tqBK5xbTSJKr3-Ei2SVuDoAuYaR3-AL5DVlV5vNj10d6x-604UYNa0sfGEU=s0')
            await interaction.response.send_message(embed=embed1, ephemeral=True)
            await msg.edit(view=view)
            return
        
        button5.callback = callback_5
        button15.callback = callback_15
        button25.callback = callback_25
        button50.callback = callback_50

        view.add_item(button5)
        view.add_item(button15)
        view.add_item(button25)
        view.add_item(button50)

        msg = await ctx.send(embed=embed, view=view)

async def setup(client):
    await client.add_cog(GooglePlayCardGenerator(client))
