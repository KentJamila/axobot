import discord
import time
import asyncio
import random
import logging
from discord.ext import commands
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')


helpcmd = """

`
Try to keep in mind that these are the commands that axo bot currently have!
Basic:
  banned     List of Banned Members
  info       Shows the info a person - ?info @[name].
  rules      List of Server Rules
  serverinfo Shows information of the server.
  ping       Wanna check my ping huh?
Fun:
  dice       To roll A die
  flip       To Flip A Coin
  hug        To Hug someone - ?hug @[username or hug yourself ;( 
  nicememe   Nice Meme!
  rnsfw      Random NSFW Pictures - Use at your own risk!
  nsfw       NSFW - Not Safe For Work 18+ - Use at your own risk!
  roll       To roll A Number 1 to 10
  search     Google image search.
Image:
  gif        Search for some giphy!
  imgnew     Shows the newest image from a specified subreddit
  imgrand    Shows the user a random image from imgur
  imgsearch  Allows the user to search for an image from imgur
  imgtop     Shows the top image from a specified subrreddit
Music:
  disconnect Stops playing audio and disconnect the voice channel.
  join       Joins a voice channel.
  pause      Pauses the currently played song.
  play       Plays a song.
  resume     Resumes the currently played song.
  skip       To skip a song.
  songinfo   Shows the info of the currently playing song.
  stop       Stops playing audio and leaves the voice channel.
  summon     Summons the bot to join your voice channel.
  volume     Sets the volume of the currently playing song.

`
"""
#commands
class Commands:
    """Commands of axo"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def ping(self,ctx):
        """Show the bot's ping"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        await self.bot.say("`My Ping Is {}ms`".format(round((t2-t1)*1000)))

    @commands.command(pass_context=True)
    async def help(self, member : discord.Member):
        embed = discord.Embed(title="axo's commands", color=0xFFFF00)
        embed.description = helpcmd
        embed.set_footer(text="axo © 2018")
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def info(self, ctx, user: discord.Member):
        """Shows the info a person - ?info @[name]."""
        try:
            embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xFFFF00)
            embed.add_field(name="Name", value=user.name, inline=True)
            embed.add_field(name="ID", value=user.id, inline=True)
            embed.add_field(name="Status", value=user.status, inline=True)
            embed.add_field(name="Highest Role", value=user.top_role, inline=True)
            embed.add_field(name="Joined", value=user.joined_at)
            embed.set_thumbnail(url=user.avatar_url)
            await self.bot.say(embed=embed)
        except:
            return

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        """Shows information of the server."""
        embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0xFFFF00)
        embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
        embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Server Roles", value=len(ctx.message.server.roles), inline=True)
        embed.add_field(name="Server Members", value=len(ctx.message.server.members))
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def rules(self, ctx):
        """List of Server Rules"""
        await self.bot.say("""Please try to keep a few guidelines in mind:

        1. No Descrimination
        2.  Bullying is prohibited
        3. This is an English/Filipino only server
        4. Don't ask other users for any kind of personal information
        5. Don't link to anything illegal or against Discord ToS
        6. Avoid spamming
        7. Use "Push to Talk" if you have a bad microphone.
        -Please mute your microphone @ Music Channel and Take A Break Channel. Thank you! 
        You're welcome to discuss other games/memes/topics""")


    @commands.command(pass_context = True)
    async def banned(self, ctx):
        """List of Banned Members"""
        x = await self.bot.get_bans(ctx.message.server)
        x = '\n'.join([y.name for y in x])
        embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFF00)
        return await self.bot.say(embed = embed)

def setup(bot):
    bot.add_cog(Commands(bot))
    print("Basic Commands Ready")