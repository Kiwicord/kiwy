import discord
from discord.ext import commands
from emojis import Kiwicord

class CommandErrorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            seconds = round(error.retry_after)
            hours = int(seconds / 3600)
            minutes = int(seconds / 60)

            if seconds > 60 and minutes < 60:
                msg1 = f'Dieser Befehl hat noch ein Cooldown! Versuch es nochmal in **{minutes} Minuten**'.format(error.retry_after)

                embed1 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Cooldown aktiv!', description=msg1)
                await ctx.reply(embed=embed1, mention_author=False)
                return
                

            if minutes > 60:
                msg2 = f'Dieser Befehl hat noch ein Cooldown! Versuch es nochmal in **{hours} Stunden**'.format(error.retry_after)

                embed2 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Cooldown aktiv!', description=msg2)
                await ctx.reply(embed=embed2, mention_author=False)
                return
                

            msg3 = f'Dieser Befehl hat noch ein Cooldown! Versuch es nochmal in **{seconds} Sekunden**'.format(error.retry_after)
            embed3 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Cooldown aktiv!', description=msg3)
            await ctx.reply(embed=embed3, mention_author=False)
            return
        
        if isinstance(error, commands.CommandNotFound):
            embedlol = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Dieser Befehl wurde nicht gefunden!')
            await ctx.reply(embed=embedlol, mention_author=False)
        
        if isinstance(error, commands.MissingPermissions):
            error_embed = discord.Embed(color=0x77dd77, title=f'{Kiwicord.EXCLAMATION} Dazu hast du keine Rechte!')
            await ctx.reply(embed=error_embed, mention_author=False)

        if isinstance(error, commands.CommandError):
            if isinstance(error, commands.CommandOnCooldown):
                return
            if isinstance(error, commands.CommandNotFound):
                return
            if isinstance(error, commands.MissingPermissions):
                return
            embed = discord.Embed(title="Fehler!", color=0x77dd77, description=f"```{error}```")
            embed.set_footer(text="Um den Fehler zu reporten, wende dich bitte an das Serverteam.")
            ctx.command.reset_cooldown(ctx)
            await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(CommandErrorHandler(client)) 
