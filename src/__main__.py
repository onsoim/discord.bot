
from asyncio    import run
from bot        import BOT
from dotenv     import load_dotenv
from os         import getenv


async def main():
    bot = BOT(
        command_prefix = '',
    )

    load_dotenv(verbose=True)
    await bot.start(getenv('DISCORD_TOKEN'))


if __name__ == "__main__":
    run(main())
