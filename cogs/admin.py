import discord
import time
import asyncio
import random
import logging
from discord.ext.commands import Bot
from discord.ext import commands
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

#commands
class Admin:
    """admin Commands of axo"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, userName: discord.User and discord.Member):
        """Kick A User From The Server"""
        await self.bot.kick(userName)
        await self.bot.say("```{} has been kicked :boot:```".format(userName))

    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, userName: discord.User and discord.Member):
        """Ban A User From The Server"""
        await self.bot.ban(userName)
        await self.bot.say("```{} has been banned :bangbang:```".format(userName))

def setup(bot):
    bot.add_cog(Admin(bot))
    print("Admin Commands Ready")
