from __future__ import annotations

import datetime
import typing

import disnake
from disnake.ext import commands

from src.core import consts

if typing.TYPE_CHECKING:
    from src.core.bot import Caera


def desc_embed(
    ctx: disnake.Interaction | commands.Context[Caera], description: str
) -> disnake.Embed:
    return disnake.Embed(
        description=description,
        color=consts.BOT_ACCENT,
        timestamp=datetime.datetime.now(),
    ).set_footer(
        text=f"{ctx.bot.user.name} | v{ctx.bot.version}",
        icon_url=ctx.bot.user.display_avatar,
    )
