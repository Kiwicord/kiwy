import pymongo
from pymongo import MongoClient
import asyncio

cluster = MongoClient('mongodb+srv://kiwious:iyCnc4g0DIv1XyUL@cluster0.ju2ct.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['Cluster0']
bank = db['kiwy-economy']
shop = db['kiwy-shop-items']
inventory = db['kiwy-economy-inv']
work_db = db['kiwy-work-table']

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
                'job': 'unemployed',
                'items': [],
                'active_booster': '1'
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
    #if _id == 931973678021873795:
        #return
    booster = await get_booster(_id)
    booster = float(booster)
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

# job
# --------------------------------------------------------

async def get_jobs():
    return work_db.find()

async def get_job(job_id):
    return work_db.find_one({'_id': job_id})

# shop
# --------------------------------------------------------
async def buy(item_id, user_id):
    bank.update_one({'_id': user_id}, {'$push': {'items': item_id}})

async def get_inv(user_id):
    user = bank.find_one({'_id': user_id})
    user_inv = user['items']
    return user_inv

async def get_shop_items():
    return shop.find()

async def get_item(item_id):
    return shop.find_one({'_id': item_id})

async def get_booster(_id):
    user = bank.find_one({'_id': _id})
    return user['active_booster']

async def get_active_items(_id):
    user = bank.find_one({'_id': _id})
    return user['active_items']

async def use_item(_id, item_id):
    bank.update_one({'_id': _id}, {'$pull': {'items': item_id}})
    bank.update_one({'_id': _id}, {'$push': {'active_items': item_id}})

async def use_booster(_id, booster_id):
    booster = await get_booster(booster_id)
    bank.update_one({'_id': _id}, {'$pull': {'items': booster_id}})
    bank.update_one({'_id': _id}, {'$push': {'active_items': booster_id }})
    bank.update_one({'_id': _id}, {'$set': {'active_booster': float(booster)}})