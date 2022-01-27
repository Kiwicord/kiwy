import discord
from discord.ext import commands
from db import *

class Changelog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def changelog(self, ctx):
        if ctx.author.id == 733403498766401554:
            embed = discord.Embed(
                color=0x77dd77, 
                title='🥝 Kiwy Update 0.0.9', 
                description= 
                """
                **Neues Entertainer / Economy System!**
                .balance / .bal - Überprüfe dein Kontostand
                .deposit [Betrag] / .dep [Betrag] - Überweise Geld auf deine Bank
                .withdraw [Betrag] / .with [Betrag] - Hebe Geld von deiner Bank ab
                .work - Verdiene Geld! (60 Sekunden Cooldown)
                """
            )
            embed.set_image(url='https://cdn.discordapp.com/attachments/891724253517479946/924053372691157112/kc_news.png')
            await ctx.send(embed=embed)
        else:
            return

def setup(client):
    client.add_cog(Changelog(client))