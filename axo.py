# axo by zin

import discord
import time
import random
import logging
import giphypop
import safygiphy
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.ext.commands import command
from tabulate import tabulate
from discord.utils import find


startup_extensions = ["cogs.axomusic", "cogs.basiccmd", "cogs.axofunmodule", "cogs.admin","cogs.image", "cogs.discordbapi"]

bot = commands.Bot(command_prefix="?")
bot.remove_command('help')

@bot.event
async def on_ready():
    print ("axo is ready")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + str(bot.user.id))
    print ("___________________________")
    await bot.change_presence(game=discord.Game(name='?help'))


class Commands:
    def __init__(self, bot):
        self.bot = bot 


#for extension of music system
if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc ='{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run("NDI4MDk3NjI1NDM5MzM4NTA5.DaW6Ig.42RnQdPBpz3OT8kAEljAAZ_-Hmo")
