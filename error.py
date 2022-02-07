import discord
from discord.ext import commands

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
                await ctx.send(embed=embed1)
                return
                

            if minutes > 60:
                msg2 = f'Dieser Befehl hat noch ein Cooldown! Versuch es nochmal in **{hours} Stunden**'.format(error.retry_after)

                embed2 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Cooldown aktiv!', description=msg2)
                await ctx.send(embed=embed2)
                return
                

            msg3 = f'Dieser Befehl hat noch ein Cooldown! Versuch es nochmal in **{seconds} Sekunden**'.format(error.retry_after)
            embed3 = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Cooldown aktiv!', description=msg3)
            await ctx.send(embed=embed3)
            return
        
        if isinstance(error, commands.CommandNotFound):
            embedlol = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Dieser Befehl wurde nicht gefunden!')
            await ctx.reply(embed=embedlol, mention_author=False)

        if isinstance(error, commands.CommandError):
            if isinstance(error, commands.CommandOnCooldown):
                return
            if isinstance(error, commands.CommandNotFound):
                return
            embed = discord.Embed(title="Fehler!", color=0x77dd77, description=f"```{error}```")
            embed.set_footer(text="Um den Fehler zu reporten, wende dich bitte an das Serverteam.")

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandErrorHandler(client)) 
