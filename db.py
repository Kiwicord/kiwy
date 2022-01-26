import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://kiwious:iyCnc4g0DIv1XyUL@cluster0.ju2ct.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['Cluster0']
bank = db['kiwy-economy']

# check profile for user
async def open_profile(_id):
    if bank.find_one({'_id': _id}):
        return
    else:
        bank.insert_one(
            {
                '_id': _id,
                'wallet': 0,
                'bank':0,
            }
        )

async def get_wallet(_id):
    user = bank.find_one({'_id': _id})
    return user['wallet']

async def get_bank(_id):
    user = bank.find_one({'_id': _id})
    return user['bank']

async def update_wallet(_id, amount):
    wallet_amt = await get_wallet(_id)
    bank.update_one({'_id': _id,}, {'$set': {'wallet': wallet_amt+int(amount)}})

async def update_bank(_id, amount):
    bank_amt = await get_bank(_id)
    bank.update_one({'_id': _id,}, {'$set': {'bank': bank_amt+int(amount)}})

async def deposit_amt(_id, amount):
    await update_wallet(_id, -1*amount)
    await update_bank(_id, amount)

async def withdraw_amt(_id, amount):
    await update_bank(_id, -1*amount)
    await update_wallet(_id, amount)