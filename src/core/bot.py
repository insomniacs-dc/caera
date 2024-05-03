import logging
import os

import asyncpg
import disnake
from disnake.ext import commands

from src.core.setups import Cog, create_logging_setup

main_logger = logging.getLogger("caera")

create_logging_setup(main_logger)


class Caera(commands.Bot):
    DEVELOPMENT: bool
    DEBUG: bool
    logger = main_logger
    version = "0.0.1a"
    cogs: dict[str, Cog]
    pool: asyncpg.Pool

    def __init__(self, dev: bool, debug: bool) -> None:
        self.DEVELOPMENT = dev
        self.DEBUG = debug
        command_sync_flags = commands.CommandSyncFlags.default()
        if self.DEBUG:
            command_sync_flags.sync_commands_debug = True
        super().__init__(
            command_prefix="c!",
            intents=disnake.Intents.all(),
            command_sync_flags=command_sync_flags,
            help_command=None,
        )
        self.load_extension("jishaku")

    async def on_ready(self) -> None:
        self.logger.info("Bot is online! ✅")

    async def setup(self) -> None:
        for ext in filter(
            lambda f: f.endswith(".py") and not f.startswith("_s"),
            os.listdir("src/exts"),
        ):
            self.logger.info(f"Loading {ext} ⭕")
            self.load_extension(f"src.exts.{ext.replace('.py','')}")
            self.logger.info(f"Loaded {ext} ✅")
        self.pool = await asyncpg.create_pool(os.getenv("PGSQL_URI"))
        with open("schema.sql", "r") as file:
            queries = file.read().strip().split(";")
            for query in queries:
                if query:
                    await self.pool.execute(query)

    async def start(self) -> None:
        await self.setup()
        await super().start(os.environ["BOT_TOKEN"])
