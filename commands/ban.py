import discord
from discord.ext import commands
from emojis import Kiwicord

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, *, reason='Kein Grund angegeben'):
        if member is None:
            error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Gib den User an der gebannt werden soll!')
            await ctx.reply(embed=error, mention_author=False)
            return

        if member == ctx.author:
            error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Du kannst dich selber nicht bannen!')
            await ctx.send(embed=error)
        embed1 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Gebannt!', description=f'Der Member {member.mention} wurde gebannt.')
        embed2 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Gebannt!', description=f'Du wurdest von **{ctx.guild.name}** gebannt.\n<:kc_punkt:924409447147786261> **{reason}**')
        await member.ban(reason=reason)
        await member.send(embed=embed2)
        await ctx.reply(embed=embed1, mention_author=False)

def setup(client):
    client.add_cog(Ban(client))