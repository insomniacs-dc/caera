from __future__ import annotations

import asyncio
import random
from io import BytesIO

import aiohttp
import disnake
from PIL import Image, ImageDraw, ImageFilter, ImageFont

session = aiohttp.ClientSession()


def _prepare_spotify(
    banner: bytes, activity: disnake.Spotify, background: int | None = None
) -> BytesIO:

    background = Image.open(
        f"assets/spotify_bg_{background or random.choice([1,2,3]) }.png"
    ).filter(ImageFilter.GaussianBlur(10))
    album = Image.open(BytesIO(banner)).resize((300, 300))
    background.paste(album, (15, 80))

    draw = ImageDraw.ImageDraw(background)

    draw.text(
        (350, 270),
        activity.title,
        font=ImageFont.truetype(
            "assets/Exo2-Medium.ttf",
            50,
        ),
        fill=disnake.Color(0xFFFFFF).to_rgb(),
    )
    draw.text(
        (350, 340),
        ", ".join(activity.artists),
        font=ImageFont.truetype(
            "assets/Exo2-Medium.ttf",
            30,
        ),
        fill=disnake.Color(0xFFFFFF).to_rgb(),
    )

    io = BytesIO()
    background.save(io, format="png")
    io.seek(0)
    return io


async def prepare_spotify_activity(
    activity: disnake.Spotify, background: int
) -> disnake.File:
    banner = await (await session.get(activity.album_cover_url)).read()
    loop = asyncio.get_event_loop()
    byte_data = await loop.run_in_executor(
        None, _prepare_spotify, banner, activity, background
    )
    return disnake.File(byte_data, filename="spotify.png")
