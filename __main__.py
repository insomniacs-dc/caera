import asyncio

import dotenv

from src.core.bot import Caera

dotenv.load_dotenv()


async def main():
    bot = Caera()
    await bot.start()


asyncio.run(main())
