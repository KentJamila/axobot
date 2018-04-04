import dbl
import discord
from discord.ext import commands

import aiohttp
import asyncio
import logging


class DiscordBotsOrgAPI:
    """Handles interactions with the discordbots.org API"""

    def __init__(self, bot):
        self.bot = bot
        self.bot_id = None
        self.token = 'dbl_token'  #  set this to your DBL token
        self.dblpy = dbl.Client(self.bot, self.token)

    async def __ainit__(self):
        await self.bot.wait_until_ready()
        self.bot_id = self.bot.user.id

    def guild_count(self):
        """Gets the guild count from the bot object"""
        try:
            return len(self.bot.guilds)
        except AttributeError:
            return len(self.bot.servers)

    async def generate_widget_small(
            self,
            bot_id: int = None,
            avabg: str = '2C2F33',
            lcol: str = '23272A',
            rcol: str = '2C2F33',
            ltxt: str = 'FFFFFF',
            rtxt: str = 'FFFFFF'
    ):
        """This function is a coroutine.

        Generates a custom large widget. Do not add `#` to the color codes (e.g. #FF00FF become FF00FF).

        Parameters
        ==========

        bot_id: int
            The bot_id of the bot you wish to make a widget for.
        avabg: str
            The hex color code of the background of the avatar (if the avatar has transparency).
        lcol: str
            The hex color code of the left background color.
        rcol: str
            The hex color code of the right background color.
        ltxt: str
            The hex color code of the left text.
        rtxt: str
            The hex color code of the right text.

        Returns
        =======

        URL of the widget: str
        """
        if bot_id is None:
            bot_id = self.bot_id
        url = 'https://discordbots.org/api/widget/lib/{0}.png?avatarbg={1}&lefttextcolor={2}&righttextcolor={3}&leftcolor={4}&rightcolor={5}'.format(
            bot_id, avabg, ltxt, rtxt, lcol, rcol)

        return url


def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))
    print("API Ready")