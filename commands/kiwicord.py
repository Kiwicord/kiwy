import discord
from discord.ext import commands
from db import *

class Kiwicord(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roles(self, ctx):
        banner_embed = discord.Embed(color=0x77dd77)
        banner_embed.set_image(url='https://cdn.discordapp.com/attachments/936991776122744834/942019177353469952/kc_rollen.png')

        main_embed = discord.Embed(
            color=0x77dd77,
            title='<a:kc_bewegendeszeichenlmao:934397592178135121> Rollenverzeichnis',
            description='<:kc_punkt:924409447147786261> **Teamrollen**\n<:kc_strich1:899571647890223124><:kc_strich2:899571647625965568><:kc_strich2:899571647625965568><:kc_strich2:899571647625965568><:kc_strich3:899571647705673730>\n<@&733403498766401554> » Inhaber\n<@&899573422667989003> » Teamleitung\n<@&845707696565125150> » Moderator\n<@&899572950209028127> » Supporter\n<@&899573999334461450> » Azubi\n\n<:kc_punkt:924409447147786261> **Normale Rollen**\n<:kc_strich1:899571647890223124><:kc_strich2:899571647625965568><:kc_strich2:899571647625965568><:kc_strich2:899571647625965568><:kc_strich3:899571647705673730>\n<@&934905301688258621> » Kiwy\n<@&845703962929266768> » Bot\n<@&939479466646851596> » Booster\n<@&922863570868383764> » Partner\n<@&919329781290532924> » VIP\n<@&899574259532300292> » Standard Rolle',
        )
        main_embed.set_footer(text='Stand: Februar 2022')
        await ctx.send(embed=banner_embed)
        await ctx.send(embed=main_embed)
  
def setup(client):
    client.add_cog(Kiwicord(client))
