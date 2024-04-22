import logging
import os

import disnake
from disnake.ext import commands

from src.core.setups import Cog, create_logging_setup

main_logger = logging.getLogger("caera")

create_logging_setup(main_logger)


class Caera(commands.Bot):
    logger = main_logger
    version = "0.0.1a"

    def __init__(self) -> None:
        command_sync_flags = commands.CommandSyncFlags.default()
        command_sync_flags.sync_commands_debug = True
        super().__init__(
            command_prefix="c!",
            intents=disnake.Intents.all(),
            command_sync_flags=command_sync_flags,
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

    async def start(self) -> None:
        await self.setup()
        await super().start(os.environ["BOT_TOKEN"])
