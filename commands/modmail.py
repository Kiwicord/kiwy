import discord 
from discord.ext import commands

class Modmail(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        channel_exists = discord.utils.get(self.client.get_guild(845217487419211776).text_channels,name="support-" + str(message.author).lower().replace("#", "").replace(" ", "-").replace("|", "-"))
    
        if message.author.id == self.client.user.id:
            return
        if message.author != message.author.bot:
            if not message.guild:
                if channel_exists:
                    embed = discord.Embed(color=0x77dd77)
                    embed.add_field(name="**⚠ New Message ⚠**", value=f"**User: **{message.author.mention}\n**Message: **{message.content}\n**User-ID: ** {message.author.id}")
                    embed.set_footer(text="Use '.reply UserId' to send a message to the User")
                    msg1 = await self.client.get_guild(845217487419211776).get_channel(channel_exists.id).send(embed=embed)
                    await message.add_reaction('✅')
                else:
                    guild = self.client.get_guild(845217487419211776)
                    category = discord.utils.get(guild.categories, name='│🥝 × Modmail')
                    new_channel = await guild.create_text_channel(name=f"support-{message.author}", reason="New ModMail ticket created.", category=category)
                    msg = await self.client.get_guild(845217487419211776).get_channel(new_channel.id).send(f"⚠️ **Neues Ticket** ⚠️\n**User:** {message.author.mention}\n**User-ID:** {message.author.id}\n\n**Nachricht:** {message.content}")
                    await message.add_reaction('✅')
                    await new_channel.set_permissions(target=guild.get_role(845217487419211776), view_channel=False)



        await self.client.process_commands(message)