import os

import disnake
from disnake.ext import commands


class Caera(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix="c!", intents=disnake.Intents.all())
        self.load_extension("jishaku")

    async def setup(self) -> None: ...

    async def start(self) -> None:
        await self.setup()
        await super().start(os.environ["BOT_TOKEN"])
