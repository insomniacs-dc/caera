from __future__ import annotations

import enum
import time

import disnake
from disnake.ext import commands

from src.core import Cog
from src.utils.embeds import desc_embed
from src.utils.images import prepare_spotify_activity


class SpotifyOptions(enum.Enum):
    landscape = 1
    space = 2
    comet = 3


class Info(Cog):
    @commands.slash_command(name="ping")
    async def ping(self, inter: disnake.CmdInter) -> None:
        """Check the latency of the bot."""
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
        """View your or another member's avatar.

        Parameters
        ----------
        member: The member to check avatar of"""

        target = member or inter.user
        await inter.response.send_message(
            embed=desc_embed(
                inter,
                description=f"`{target.name}`'s avatar | [`Download 📥`]({target.display_avatar.url})",
            ).set_image(target.display_avatar.url)
        )

    @commands.slash_command(name="spotify")
    async def spotify(
        self,
        inter: disnake.CmdInter,
        member: disnake.Member | None = None,
        background: SpotifyOptions | None = None,
    ) -> None:
        """Displays the spotify activity of a member.

        Parameters
        ----------
        member: The member to check activity of
        background: The background to display in the banner
        """
        target: disnake.Member = member or inter.user
        activity = (
            data[0]
            if (
                data := [
                    act for act in target.activities if isinstance(act, disnake.Spotify)
                ]
            )
            else None
        )
        if not activity:
            return await inter.send(
                embed=disnake.Embed(
                    description=f"{target.mention} is not listening to Spotify",
                    color=disnake.Color.green(),
                ).set_author(name="Spotify Activity")
            )
        image = await prepare_spotify_activity(activity, background)
        artists = "`, `".join(artist for artist in activity.artists)
        embed = (
            disnake.Embed(
                color=disnake.Color.green(),
                description=f"""
**Track Title**: [`{activity.title}`]({activity.track_url})
**Artist**: `{artists}` 
**Album**: `{activity.album}`                             
                              """,
            )
            .set_author(name=activity.name, url=activity.track_url)
            .set_thumbnail(activity.album_cover_url)
        )
        embed.set_image(file=image)

        view = disnake.ui.View()
        view.add_item(
            disnake.ui.Button(
                style=disnake.ButtonStyle.link,
                label=activity.title,
                url=activity.track_url,
            )
        )
        await inter.send(embed=embed, view=view)


setup = Info.setup
