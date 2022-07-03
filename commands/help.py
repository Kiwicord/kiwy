import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        if ctx.guild.id == 845217487419211776:
            embed = discord.Embed(title="Alle Befehle", description="Benutze .help <befehl> für mehr Infos von einem Command.", color=0x77dd77)
            embed.add_field(name="Moderation", value="`ban`, `kick`, `knastadd`, `knastremove`")
            embed.add_field(name="Spaß", value="keine 😳")
            embed.add_field(name="Casino/Economy", value="`balance`, `beg`, `booster`, `buy`, `daily`, `deposit`, `inventory`, `item`, `items`, `leaderboard`, `rob`, `send`, `shop`, `slots`, `use`, `withdraw`, `work`")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Alle Befehle", description="Benutze .help <befehl> für mehr Infos von einem Command.", color=0x77dd77)
            embed.add_field(name="Moderation", value="`ban`, `kick`")
            embed.add_field(name="Spaß", value="keine 😳")
            embed.add_field(name="Casino/Economy", value="`balance`, `beg`, `booster`, `buy`, `daily`, `deposit`, `inventory`, `item`, `items`, `leaderboard`, `rob`, `send`, `shop`, `slots`, `use`, `withdraw`, `work`")
            await ctx.send(embed=embed)            
    
    @help.command()
    async def ban(self, ctx):
        embed = discord.Embed(title="Ban", description="Bannt einen User vom Server.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.ban <Member#0000> [Grund]`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)
    
    @help.command()
    async def kick(self, ctx):
        embed = discord.Embed(title="Kick", description="Kickt einen User vom Server.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.kick <Member#0000> [Grund]`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def knastadd(self, ctx):
        if ctx.guild.id == 845217487419211776:
            embed = discord.Embed(title="Knastadd", description="Schickt einen User in den Knast.", color=0x77dd77)
            embed.add_field(name="Syntax", value="`.knastadd <Member#0000>`")
            embed.set_footer(text="<> - Erforderlich, [] - Optional")
            await ctx.send(embed=embed)
        else:
            raise commands.CommandNotFound

    @help.command()
    async def knastremove(self, ctx):
        if ctx.guild.id == 845217487419211776:
            embed = discord.Embed(title="Knastremove", description="Entlässt einen User aus dem Knast.", color=0x77dd77)
            embed.add_field(name="Syntax", value="`.knastremove <Member#0000>`")
            embed.set_footer(text="<> - Erforderlich, [] - Optional")
            await ctx.send(embed=embed)
        else:
            raise commands.CommandNotFound

    @help.command()
    async def balance(self, ctx):
        embed = discord.Embed(title="Balance", description="Zeigt deinen Kontostand an.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.balance [@User#1234]`")
        embed.add_field(name="Aliases", value="`bal`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def beg(self, ctx):
        embed = discord.Embed(title="Beg", description="Erbitte Geld. Es besteht eine Wahrscheinlichkeit dass man erwischt wird und man Strafgeld zahlen muss.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.beg`")
        embed.add_field(name="Cooldown", value="`1 Minute`")
        await ctx.send(embed=embed)

    @help.command()
    async def booster(self, ctx):
        embed = discord.Embed(title="Booster", description="Zeigt deinen aktuellen Booster an.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.booster [@User#1234]`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def buy(self, ctx):
        embed = discord.Embed(title="Buy", description="Kaufe ein Item aus dem Shop.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.buy <itemID>`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def daily(self, ctx):
        embed = discord.Embed(title="Daily", description="Bekomme jeden Tag Geld.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.daily`")
        embed.add_field(name="Cooldown", value="`24 Stunden`")
        await ctx.send(embed=embed)

    @help.command()
    async def deposit(self, ctx):
        embed = discord.Embed(title="Deposit", description="Überweise Geld auf die Bank.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.deposit <Betrag> / <all>`")
        embed.add_field(name="Aliases", value="`dep`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def inventory(self, ctx):
        embed = discord.Embed(title="Inventory", description="Zeigt dein Inventar an.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.inventory [@User#1234]`")
        embed.add_field(name="Aliases", value="`inv`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def item(self, ctx):
        embed = discord.Embed(title="Item", description="Zeigt mehr Informationen über ein Item an.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.item <itemID>`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def items(self, ctx):
        embed = discord.Embed(title="Items", description="Zeigt deine aktiven Items an.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.items [@User#1234]`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def leaderboard(self, ctx):
        embed = discord.Embed(title="Leaderboard", description="Zeigt die reichsten User an. Geld welches auf der Bank liegt, zählt nicht.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.leaderboard`")
        embed.add_field(name='Aliases', value='`top`, `rich`, `lb`')
        await ctx.send(embed=embed)

    @help.command()
    async def rob(self, ctx):
        embed = discord.Embed(title="Rob", description="Raube einen User aus. Du brauchst mindestens **10,000**🥝 um einen Raub zu starten. Du hast eine **50.0%** Chance, dass der Raub schief geht.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.rob <@User#1234>`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def send(self, ctx):
        embed = discord.Embed(title="Send", description="Überweise Geld an ein anderen User.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.send <@User#1234> <Betrag>`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def shop(self, ctx):
        embed = discord.Embed(title="Shop", description="Öffnet dn Shop.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.shop`")
        await ctx.send(embed=embed)

    @help.command()
    async def slots(self, ctx):
        embed = discord.Embed(title="Slots", description="Spiel Roulette. Du hast eine **33.3%** Chance um zu gewinnen.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.slots <Betrag>`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def use(self, ctx):
        embed = discord.Embed(title="Use", description="Benutze ein Item, welches in deinem Inventar ist.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.use <itemID>`")
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def withdraw(self, ctx):
        embed = discord.Embed(title="Withdraw", description="Heb Geld von deiner Bank ab.", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.withdraw <Betrag>`")
        embed.add_field(name='Aliases', value='`with`')
        embed.set_footer(text="<> - Erforderlich, [] - Optional")
        await ctx.send(embed=embed)

    @help.command()
    async def work(self, ctx):
        embed = discord.Embed(title="Work", description="Arbeite und verdiene dein Gehalt. Erforderlich ist ein Job. Erfahre mehr mit `.work list`", color=0x77dd77)
        embed.add_field(name="Syntax", value="`.work`")
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Help(client))
