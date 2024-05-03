from __future__ import annotations
import disnake
from disnake.ext import commands

from src.core import Cog, consts
from src.utils.embeds import desc_embed


class VoiceCommands(Cog):
    qualified_name = "voice"

    @commands.slash_command(name="create_setup")
    async def _setup_channel(self, inter: disnake.CmdInter) -> None:
        await inter.send(embed=desc_embed(inter, "Setting up Voice features..."))
        channel_overwrites = disnake.PermissionOverwrite(
            connect=False, send_messages=False
        )
        category = await inter.guild.create_category(
            name="Caera", overwrites={inter.guild.default_role: channel_overwrites}
        )
        channel = await category.create_voice_channel(
            name="Create Your VC",
            overwrites={
                inter.guild.default_role: disnake.PermissionOverwrite(connect=True)
            },
        )
        await inter.edit_original_response(
            embed=disnake.Embed(
                description=f"Setup completed in {channel.mention}!",
                color=consts.BOT_ACCENT,
            )
        )


setup = VoiceCommands.setup
