import discord
from discord.ext import commands
from db import *


class Work(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 3600, commands.BucketType.user)
    @commands.group(invoke_without_command=True)
    async def work(self, ctx, option=None):
        jobs = await get_jobs()
        current_job = await get_current_job(ctx.author.id)
        job = current_job['job']

        joblist = []
        for job in jobs:
            joblist.append(job['_id'])
        
        try:             
            if option is None:
                if job == 'unemployed':
                    await ctx.send('Du bist momentan arbeitslos!\nFinde einen job mit -work list')
                user = bank.find_one({'_id': ctx.author.id})
                user_job = user['job']
                worktable = await get_job(user_job)
                income = worktable['income']
                job_name = worktable['name']
                await update_wallet(ctx.author.id, income)
                work_embed = discord.Embed(color=0x77dd77, title='<a:kc_bewegendeszeichenlmao:934397592178135121> Gute Arbeit!', description=f'Du hast als **{job_name}** gearbeitet und hast **{income:,}**🥝 verdient')
                await ctx.send(embed=work_embed)
                
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
                    await ctx.send(embed=new_work_embed)
        except:
            pass
    
    @work.command(name='list')
    async def list(self, ctx):
        embed = discord.Embed(title='<a:kc_bewegendeszeichenlmao:934397592178135121> Jobs', color=0x77dd77)
        jobs = await get_jobs()
        for job in jobs:
            embed.add_field(name=f'{job["name"]}', value=f'Beschreibung: {job["description"]}\nStündliches Einkommen: **{job["income"]:,}**🥝\nID: `{job["_id"]}`', inline=False)
        embed.set_footer(text='Um zu arbeiten, führe .work (ID vom Job) aus')
        await ctx.send(embed=embed)
                
def setup(client):
    client.add_cog(Work(client))