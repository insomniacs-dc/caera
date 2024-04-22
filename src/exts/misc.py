import time

import disnake
from disnake.ext import commands

from src.core.consts import BOT_ACCENT
from src.core.setups import Cog
from src.utils.embeds import desc_embed


class Misc(Cog):
    @commands.slash_command(name="ping")
    async def ping(self, inter: disnake.CmdInter) -> None:
        start = time.perf_counter()
        await inter.send(embed=desc_embed(inter, "Getting ping... 🏓"))
        diff = time.perf_counter() - start
        await inter.edit_original_response(
            embed=desc_embed(
                inter,
                f"**Websocket Latency**: `{self.bot.latency*1000:.2f}ms`\n**REST Latency**: `{diff*1000:.2f}ms`",
            )
        )

    @commands.slash_command(name="avatar")
    async def avatar(
        self, inter: disnake.CmdInter, member: disnake.Member | None = None
    ) -> None:
        target = member or inter.user
        await inter.response.send_message(
            embed=desc_embed(
                inter,
                description=f"`{target.name}`'s avatar | [`Download 📥`]({target.display_avatar.url})",
            ).set_image(target.display_avatar.url)
        )


setup = Misc.setup
