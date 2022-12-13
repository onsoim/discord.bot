
from discord                import Intents
from discord.ext.commands   import Bot
from dotenv                 import load_dotenv
from os                     import getenv, listdir


class BOT(Bot):
    load_dotenv(verbose=True)

    def __init__(self, *args, **kwargs):
        super().__init__(
            intents = Intents.default(),
            *args, **kwargs
        )

    async def load_extensions(self, cogs = 'cogs'):
        for filename in listdir(f'./src/{cogs}'):
            if filename.endswith(".py"):
                await self.load_extension(f'{cogs}.{filename[:-3]}')

    async def on_ready(self):
        print('[*] Start bot')

    async def start(self, token: str = getenv('DISCORD_TOKEN'), *, reconnect: bool = True) -> None:
        return await super().start(token, reconnect=reconnect)
