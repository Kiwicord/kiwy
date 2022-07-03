import discord
from discord.ext import commands
from emojis import Kiwicord

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, *, reason='Kein Grund angegeben'):
        role = discord.utils.find(lambda r: r.name == '│📋 × Moderator', ctx.message.guild.roles)


        if member is None:
            error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Gib den User an der gekickt werden soll!')
            await ctx.reply(embed=error, mention_author=False)
            return

        
        if role in member.roles:
            error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Stop!', description=f'Du kannst {member.mention} nicht kicken!')
            await ctx.send(embed=error)
            return

        if member == ctx.author:
            error = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Du kannst dich selber nicht kicken!')
            await ctx.send(embed=error)
            return
        embed1 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Gekickt!', description=f'Der Member {member.mention} wurde gekickt.')
        embed2 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Gekickt!', description=f'Du wurdest von **{ctx.guild.name}** gekickt.\n<:kc_punkt:924409447147786261> **{reason}**')
        await member.kick(reason=reason)
        await member.send(embed=embed2)
        await ctx.reply(embed=embed1, mention_author=False)

async def setup(client):
    await client.add_cog(Kick(client))