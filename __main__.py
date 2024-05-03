import asyncio
import os
import sys

import dotenv

from src.core.bot import Caera, main_logger

dotenv.load_dotenv()

DEBUG: bool = bool(os.getenv("DEBUG", False))
DEVELOPMENT: bool = bool(os.getenv("DEVELOPMENT", True))


async def main():

    bot = Caera(DEVELOPMENT, DEBUG)
    await bot.start()


if len(sys.argv) == 2:
    command = sys.argv[1]
    if command in ["fmt", "format"]:
        main_logger.info("Formatting Code ...")
        main_logger.info("Using black for format code: ")
        os.system("black .")
        main_logger.info("Using isort to sort imports: ")
        os.system("isort .")
        main_logger.info("Running linter (ruff)")
        os.system("ruff check .")

    exit()


asyncio.run(main())
