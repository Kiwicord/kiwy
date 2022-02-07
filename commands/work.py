import discord
from discord.ext import commands
from db import *


class Work(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 3600, commands.BucketType.user)
    @commands.group(name='work', invoke_without_command=True)
    async def work(self, ctx, option=None):
        await open_profile(ctx.author.id)
        jobs = await get_jobs()
        current_job = bank.find_one({'_id': ctx.author.id})
        job = current_job['job']

        joblist = []
        for job in jobs:
            joblist.append(job['_id'])
        
        # try:             
        if option is None:
            if current_job['job'] == 'unemployed':
                embed_unemployed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Arbeitslos!', description='Du bist momentan arbeitslos. Finde einen Job mit **.work list**.')
                await ctx.reply(embed=embed_unemployed, mention_author=False)
                ctx.command.reset_cooldown(ctx)
                return
            
            user = bank.find_one({'_id': ctx.author.id})
            user_job = user['job']
            worktable = await get_job(user_job)
            income = worktable['income']
            job_name = worktable['name']
            await update_wallet(ctx.author.id, income)
            work_embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Gute Arbeit!', description=f'Du hast als **{job_name}** gearbeitet und hast **{income:,}**🥝 verdient')
            await ctx.reply(embed=work_embed, mention_author=False)
            
        embed = discord.Embed(title='<a:kc_bewegendeszeichenlmao:934397592178135121> Jobs', color=0x77dd77)
        
        if option is not None:  
            # if option == 'list':
            #     jobs = await get_jobs()
            #     for job in jobs:
            #         embed.add_field(name=f'{job["name"]}', value=f'Beschreibung: {job["description"]}\nStündliches Einkommen: **{job["income"]:,}**🥝\nID: `{job["_id"]}`', inline=False)
            #     embed.set_footer(text='Um zu arbeiten, führe .work (ID vom Job) aus')
            #     await ctx.send(embed=embed)
            
            if option in joblist:
                final_job = await get_job(option)
                bank.update_one({'_id': ctx.author.id,}, {'$set': {'job': option}})
                new_work_embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Willkommen auf der neuen Arbeit!', description=f'Du arbeitest nun als **{final_job["name"]}**! Dein Einkommen beträgt nun **{final_job["income"]:,}**🥝')
                ctx.command.reset_cooldown(ctx)
                await ctx.reply(embed=new_work_embed, mention_author=False)
            elif option not in joblist:
                embed_not_found = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Dieser Beruf wurde nicht gefunden!')
                embed_not_found.set_footer('Tipp: benutze .work list um einen Job zu finden.')
                await ctx.reply(embed=embed_not_found, mention_author=False)
                ctx.command.reset_cooldown(ctx)
                return
        # except:
        #     pass
    
    @work.command(name='list')
    async def list(self, ctx):
        await open_profile(ctx.author.id)
        embed = discord.Embed(title='<a:kc_bewegendeszeichenlmao:934397592178135121> Jobs', color=0x77dd77)
        jobs = await get_jobs()
        for job in jobs:
            embed.add_field(name=f'» {job["name"]}', value=f'● Beschreibung: {job["description"]}\n● Stündliches Einkommen: **{job["income"]:,}**🥝\n● ID: `{job["_id"]}`', inline=False)
        embed.set_footer(text='Um zu arbeiten, führe .work (ID vom Job) aus')
        await ctx.reply(embed=embed, mention_author=False)

    @work.command()
    async def resign(self, ctx):
        await open_profile(ctx.author.id)
        current_job = await get_current_job(ctx.author.id)
        job = current_job['job']
        if job == 'unemployed':
            embed_unemployed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Du bist arbeitslos und kannst nicht von deiner Arbeit zurücktreten!')
            await ctx.reply(embed=embed_unemployed, mention_author=False)
            return
        
        if job != 'unemployed':
            bank.update_one({'_id': ctx.author.id,}, {'$set': {'job': 'unemployed'}})
            embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Ciao!', description='Du bist nun von deinem Job zurückgetreten.\nDu kannst erst in **1 Stunde** einen neuen Job finden.')
            await ctx.reply(embed=embed, mention_author=False)
            return

                
def setup(client):
    client.add_cog(Work(client))
