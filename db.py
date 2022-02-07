import pymongo
from pymongo import MongoClient
import asyncio

cluster = MongoClient('mongodb+srv://kiwious:iyCnc4g0DIv1XyUL@cluster0.ju2ct.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['Cluster0']
bank = db['kiwy-economy']
shop = db['kiwy-economy-shop']
inventory = db['kiwy-economy-inv']
work = db['kiwy-work-table']

# main economy
# --------------------------------------------------------
async def open_profile(_id):
    if bank.find_one({'_id': _id}):
        return
    else:
        bank.insert_one(
            {
                '_id': _id,
                'wallet': 0,
                'bank': 0,
                'job': 'unemployed'
            }
        )

async def get_wallet(_id):
    await open_profile(_id)
    user = bank.find_one({'_id': _id})
    return user['wallet']

async def get_bank(_id):
    await open_profile(_id)
    user = bank.find_one({'_id': _id})
    return user['bank']

async def update_wallet(_id, amount):
    await open_profile(_id)
    wallet_amt = await get_wallet(_id)
    bank.update_one({'_id': _id,}, {'$set': {'wallet': wallet_amt+int(amount)}})

async def update_bank(_id, amount):
    await open_profile(_id)
    bank_amt = await get_bank(_id)
    bank.update_one({'_id': _id,}, {'$set': {'bank': bank_amt+int(amount)}})

async def deposit_amt(_id, amount):
    await open_profile(_id)
    await update_wallet(_id, -1*amount)
    await update_bank(_id, amount)

async def withdraw_amt(_id, amount):
    await open_profile(_id)
    await update_bank(_id, -1*amount)
    await update_wallet(_id, amount)

async def get_current_job(_id):
    return bank.find_one({'_id': _id})
# --------------------------------------------------------

async def get_jobs():
    return work.find()

async def get_job(job_id):
    return work.find_one({'_id': job_id})