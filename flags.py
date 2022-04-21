from db import *
import random

async def setup_flag_quiz(guild, channel):
    flag_data.insert_one({'guild': guild,'channel': channel})

async def get_random_flag():
    all_flags = flags.find()
    return random.choice(all_flags)

async def send_flag(channel):
    pass

async def get_channel(guild):
    return flag_data.find_one({'guild': guild})

async def add_flag(img_link, name):
    flags.insert_one({'name': name, 'link': img_link})