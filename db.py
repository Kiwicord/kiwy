import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://kiwious:iyCnc4g0DIv1XyUL@cluster0.ju2ct.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['Cluster0']
bank = db['kiwy-economy']
shop = db['kiwy-economy-shop']
inventory = db['kiwy-economy-inv']

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
                'items': {

                }
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

async def leaderboard():
    results = bank.find().sort('wallet', pymongo.ASCENDING)

    output = ''
    for r in str(results):
        output += r['wallet']
    return output
# --------------------------------------------------------

# shop system
# --------------------------------------------------------
async def create_new_item(_id, name: str, cost: int, emoji: str, description: str):
    if shop.find_one({'_id': _id}):
        return
    else:
        shop.insert_one(
            {
                '_id': _id,
                'name': name,
                'cost': cost,
                'emoji': emoji,
                'description': description
            }
        )

async def get_shop_items():
    return shop.find()

async def get_item(item_id):
    item = shop.find_one({'_id': item_id})
    return item

async def get_item_price(item_id):
    item = await get_item(item_id)
    price = item['cost']
    return price

# --------------------------------------------------------

# inv system
# --------------------------------------------------------

async def buy(_id, item_id: str):
    item = await get_item(item_id)

    inventory.insert_one({
        '_id': _id,
        'item_id': item_id,
        'item_name': item['name'],
        'item_emoji': item['emoji'],
        'item_description': item['description']
    })

# '_id': _id,
#                 'name': name,
#                 'cost': cost,
#                 'emoji': emoji,
#                 'description': description

async def get_inv(_id):
    return bank.find({'_id': _id})