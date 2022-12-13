
from asyncio    import run
from bot        import BOT


async def main():
    bot = BOT(
        command_prefix = '',
    )

    await bot.load_extensions()
    await bot.start()


if __name__ == "__main__":
    run(main())
