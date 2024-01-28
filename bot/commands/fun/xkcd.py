import json
import random

import aiohttp

from bot.base import Command
from bot.config import Embed


class cmd(Command):
    """A discord command instance."""

    name = "xkcd"
    usage = "xkcd"
    description = "Sends a XKCD comic strip"

    async def execute(self, arguments, message) -> None:
        xkcd_url = (
            "https://xkcd.com/info.0.json"
        )
        
        id: str

        if len(arguments) > 0:
            id = arguments

            xkcd_url = (
                "https://xkcd.com/" + id + "/info.0.json"
            )

        async with aiohttp.ClientSession() as session:
            async with session.get(gigaurl) as result:
                if result.status != 200:
                    embed = Embed(title="XKCD API Request Failed", description="How sad. :(")
                    embed.set_color("red")
                    await message.channel.send(embed=embed)
                    return

                comic = await result.json(content_type=None)

        id = str(comic["num"])
        
        # send the image
        embed = Embed(title="#" + id + " — " + comic["safe_title"])
        embed.set_footer(text=comic["alt"])
        embed.set_image(
            url=comic["img"]
        )
        await message.channel.send(embed=embed)
