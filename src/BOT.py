
from discord                import Intents
from discord.ext.commands   import Bot

import os


class BOT(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(
            intents = Intents.default(),
            *args, **kwargs
        )

    async def load_extensions(self, cogs = 'discord_cogs'):
        for filename in os.listdir(f'./src/{cogs}'):
            if filename.endswith(".py"):
                await self.load_extension(f'{cogs}.{filename[:-3]}')

    async def on_ready(self):
        print('[*] Start bot')
