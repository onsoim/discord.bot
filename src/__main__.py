
from discord    import Intents
from src.BOT    import BOT

import asyncio
import os



async def main():
    bot = BOT(
        command_prefix = '',
        intents = Intents.all()
    )

    await bot.load_extensions('discord_cogs')
    await bot.start(os.getenv('DISCORD_TOKEN'))


if __name__ == "__main__":
    asyncio.run(main())
