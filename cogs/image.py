import logging
import os
import random
import requests
import discord
from discord.ext import commands
from imgurpython import ImgurClient

log = logging.getLogger(__name__)

try:
    imgurclient = ImgurClient("98ec0261d35c1f8", "b399b4f68e0463acfa0ef3181d19c05ea2788ee7")
except KeyError:
    log.warn('Environment variable not found.')


class Image:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def imgrand(self):
        """Shows the user a random image from imgur"""
        rand = random.randint(0, 59)  # 60 results generated per page
        items = imgurclient.gallery_random(page=0)
        await self.bot.say(items[rand].link)

    @commands.command(pass_context=True)
    async def imgsearch(self, ctx, *text: str):
        """Allows the user to search for an image from imgur"""
        rand = random.randint(0, 59)
        if text == ():
            await self.bot.say('`Please enter a search term`')
        elif text[0] != ():
            items = imgurclient.gallery_search(" ".join(text[0:len(text)]), advanced=None, sort='viral', window='all',
                                               page=0)
            if len(items) < 1:
                await self.bot.say('`Your search gave no results`')
            else:
                await self.bot.say(items[rand].link)

    @commands.command(pass_context=True)
    async def imgtop(self, ctx, *text: str):
        """Shows the top image from a specified subrreddit"""
        if text == ():
            await self.bot.say('`Please enter a subbreddit`')
        elif text[0] != ():
            items = imgurclient.subreddit_gallery(" ".join(text[0:len(text)]), sort='top', window='day', page=0)
            if len(items) < 1:
                await self.bot.say('`This subreddit section does not exist, try funny`')
            else:
                await self.bot.say(items[0].link)

    @commands.command(pass_context=True)
    async def imgnew(self, ctx, *text: str):
        """Shows the newest image from a specified subreddit"""
        if text == ():
            await self.bot.say('`Please enter a subbreddit`')
        elif text[0] != ():
            items = imgurclient.subreddit_gallery(" ".join(text[0:len(text)]), sort='time', window='day', page=0)
            if len(items) < 1:
                await self.bot.say('`This subreddit section does not exist, try funny`')
            else:
                await self.bot.say(items[0].link)


def setup(bot):
    bot.add_cog(Image(bot))
    print("Image Ready")

