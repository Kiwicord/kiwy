from discord.ext.commands import Bot as BotBase
from discord import Intents, Embed
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from os import getenv
from dotenv import load_dotenv

load_dotenv()

PREFIX='.'
OWNER_IDS = [733403498766401554]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.GUILD = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX, 
            owner_ids=OWNER_IDS,
            intents=Intents.all(),
        )
    
    def run(self, version):
        self.VERSION = version
        self.TOKEN = getenv('TOKEN')
        print('Bot is starting up...')
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print('Bot connected')
    
    async def on_disconnect(self):
        print('Bot disconnected')
    
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(891005230173544509)
            print('Bot is ready')

            channel = self.get_channel(891005230668460074)
            await channel.send('Online')

            embed = Embed(title='Jetzt Online', description='Der Kiwi-Bot ist nun online')
            await channel.send(embed=embed)
        else:
            print('Bot reconnected')

    async def on_message(self, message):
        pass

bot = Bot()