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
                title='🎉 Kiwy Update beta 0.1', 
                description='Nach 11 Tagen kommt jetzt endlich die Beta Version 0.1 raus! Sie beinhaltet hauptsächlich Änderungen in dem Entertainer Bereich.')
            embed.add_field(name='⛏ Work Command', 
            value=
            """
            **.work** - Arbeite und verdiene Geld mit einem einzigartigen Beruf. Dieser Befehl hat einen Cooldown von **1 Stunde**
            **.work list** - Such dir einen Beruf aus.
            **.work (Berufs-ID)** - Starte einen neuen Job.
            **.work resign** - Trete von deinem Job zurück. Du kannst erst nach **1 Stunde** erneut einen Job finden.
            """, inline=False
            )
            embed.add_field(name='🤝 Beg Command', 
            value=
            """
            **.beg** - Erbitte Geld. Dieser Command hat einen Cooldown von **5 Minuten**

            ⚠ Achtung! Es besteht eine Wahrscheinlichkeit dass man beim Benutzen vom **.beg** Command erwischt wird und man Strafgeld zahlen muss.




            """, inline=False
            )
            embed.add_field(name='🔭 In der Zukunft', 
            value=
            """
            ● Musik Funktion
            ● Moderator Befehle
            ● Fun Commands
            ...und der Bot wird überall erreichbar sein!
            """
            )
            embed.set_image(url='https://cdn.discordapp.com/attachments/891724253517479946/924053372691157112/kc_news.png')
            await ctx.send(embed=embed)
            msg = await ctx.send('<@&919280393893580800>')
            await asyncio.sleep(1)
            await msg.delete()
        else:
            return

def setup(client):
    client.add_cog(Changelog(client))