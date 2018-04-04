import discord
import time
import asyncio
import random
import logging
import requests
import io
import safygiphy
import urllib
import aiohttp
import giphypop
from discord.ext import commands
from imgurpython import ImgurClient

import re


g = safygiphy.Giphy()

bot = commands.Bot

log = logging.getLogger(__name__)

try:
    imgurclient = ImgurClient("98ec0261d35c1f8", "b399b4f68e0463acfa0ef3181d19c05ea2788ee7")
except KeyError:
    log.warn('Environment variable not found.')

#----------------------------------------------------------------------------------------------------------------------------------------------------
#NOT SAFE FOR WORK2
nsfwlinks = [
"https://image.ibb.co/cJZvzn/93ba26c0ed0aa57abdff4006ebd47dc3_anime_hot_anime_manga.jpg", 
"https://preview.ibb.co/mCuvzn/9107_sexy_xmas_cum_slut.gif", 
"https://image.ibb.co/mbUOkS/e6e1be6873d41628b7a9f2222c6b14c5.gif", 
"https://preview.ibb.co/e9Ejs7/Hadako_tan.png", 
"https://image.ibb.co/jTDcC7/tumblr_p39bv6_KTq_K1uv7tveo1_1280.png",
"https://cdnio.luscious.net/slywalker_96/738/lusciousnet_lusciousnet_big-ass-comp-v1_wwwpervifycom_1260_636946376.315x0.png",
"https://cdnio.luscious.net/unknown474/308396/368_1785757-aqua-kazuma_satou-kono_subarashii_se_01C9N8SATH92375CD1SQ0QECJH.315x0.jpg",
"https://cdnio.luscious.net/Fuwaaa/308369/0052_01C9M903T6CXXHNMMB5PBMFRM4.315x0.jpg",
"https://cdnio.luscious.net/shiningvoid/308324/54bf1940bcfc8a99a7ea2a57d6a0bc62_01C9K1P8D8SNX7W7WGRQXXZTFT.315x0.jpg",
"https://cdnio.luscious.net/reaper2855/290955/alice_01C9GNA6Q8GXBNGDP98VRWR6XK.315x0.jpg",
"https://cdn.discordapp.com/attachments/423498253007454211/428444849457594379/13_-_Copy.png",
"https://cdnio.luscious.net/Shifter00/308271/z_01C9GDJ02X6BYAB6HGCN3XZJYM.315x0.jpg",
"https://cdnio.luscious.net/Hencchi/304814/xtermination000yy_01C577BHH3V1DFDBSRVBK7DNEE.315x0.jpg",
"https://thumb-p5.xhcdn.com/000/134/966/505_1000.gif",
"https://i.imgur.com/M3lw19e.jpg",
"https://hijiribe.donmai.us/data/__yorha_no_2_type_b_nier_series_and_nier_automata_drawn_by_hews_hack__c792c49410320bf1a632acf76f2fe5f4.png",
"https://hijiribe.donmai.us/data/__yorha_no_2_type_b_nier_series_and_nier_automata_drawn_by_genjung__ed8e63d2cfe31f25c51ababa857cf90d.jpg",
"https://i.pinimg.com/736x/a1/d2/60/a1d2600a3883af42914dd48b351db938--naruto-girls-anime-girls.jpg",
"https://cdnio.luscious.net/unknown474/308404/340_1791836-kono_subarashii_sekai_ni_shukufuku_w_01C9NC7ZB8VR1KT8NGXA07N3D5.315x0.jpg",
"https://cdnio.luscious.net/unknown474/308404/339_1797603-kono_subarashii_sekai_ni_shukufuku_w_01C9NC7RJ3F4TYG9HX5QP1AGSH.1024x0.jpg",
"http://www.overwatchhentaidb.com/i?/upload/2017/11/13/20171113040921-970c7597-cu_s9999x200.jpg",
"http://www.overwatchhentaidb.com/i?/upload/2018/02/16/20180216023509-66c17356-cu_s9999x410.jpg",
"http://www.overwatchhentaidb.com/i?/upload/2017/12/02/20171202231840-b035c480-cu_s9999x200.png",
"http://www.overwatchhentaidb.com/i?/upload/2017/11/21/20171121211143-a3e54581-cu_s9999x200.png",
"http://www.overwatchhentaidb.com/i?/upload/2017/10/17/20171017013318-b7d4cdce-cu_s9999x200.jpg",
"http://www.overwatchhentaidb.com/i?/upload/2017/11/16/20171116075834-62d500bb-cu_s9999x200.jpg",
"http://www.overwatchhentaidb.com/i?/upload/2017/12/26/20171226072419-c570fef1-cu_s9999x200.png",
"http://www.overwatchhentaidb.com/i?/upload/2018/02/16/20180216023508-22494927-cu_s9999x200.jpg",
"http://www.overwatchhentaidb.com/i?/upload/2017/12/26/20171226072502-14776978-cu_s9999x200.jpg",
"http://www.overwatchhentaidb.com/i?/upload/2017/12/26/20171226072434-fd215ad9-cu_s9999x200.jpg",
"http://www.overwatchhentaidb.com/i?/upload/2017/12/26/20171226072123-95c463aa-cu_s9999x200.jpg",
"https://cdn.discordapp.com/attachments/428097987491659789/428449845381169162/aewaea.png"]
#----------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------
#for command ?hug
huglinks = ["https://media1.giphy.com/media/VGACXbkf0AeGs/giphy.gif", "https://media2.giphy.com/media/BXrwTdoho6hkQ/giphy.gif", "https://media1.giphy.com/media/bvFS4rALdNDag/giphy.gif", "https://media1.giphy.com/media/EvYHHSntaIl5m/giphy.gif", "https://media1.giphy.com/media/RmZemRytXqmic/giphy.gif", "https://media1.giphy.com/media/lXiRKBj0SAA0EWvbG/giphy.gif", "https://media0.giphy.com/media/du8yT5dStTeMg/giphy.gif", "https://media0.giphy.com/media/13YrHUvPzUUmkM/giphy.gif", "https://media1.giphy.com/media/143v0Z4767T15e/giphy.gif"]
huglinks2 = ["https://media2.giphy.com/media/3oz8xLz5gnSla2STE4/giphy.gif", "https://media1.giphy.com/media/iAvpVf8mOtqDK/giphy.gif"]
#----------------------------------------------------------------------------------------------------------------------------------------------------
#NOT SAFE FOR WORK
nsfwsub = "?nsfw `gonewild, RealGirls, nsfw, gonewildcurvy, NSFW_GIF, milf, ass, BusyPetite, nsfw_gifs, Boobies, cumsluts, ladybonersgw, rule34, Amateur, GoneWildPlus, AsiansGoneWild, TinyTits, GoneMild, OnOff, ginger, MorbidReality, Legal Teens`"
#----------------------------------------------------------------------------------------------------------------------------------------------------
tosscoin = [":sun_with_face: Heads, congratulations to whoever won", ":new_moon_with_face: Tails, congratulations to whoever won", ":sun_with_face: Heads, congratulations to whoever won", 
":new_moon_with_face: Tails, congratulations to whoever won", ":sun_with_face: Heads, congratulations to whoever won", ":new_moon_with_face: Tails, congratulations to whoever won", 
":sun_with_face: Heads, congratulations to whoever won", ":new_moon_with_face: Tails, congratulations to whoever won"]
#----------------------------------------------------------------------------------------------------------------------------------------------------
nicememe = ["https://memegenerator.net/img/instances/68470659/nice-meme.jpg",
"http://i0.kym-cdn.com/entries/icons/facebook/000/017/481/nicememe.jpg", 
"https://i.ytimg.com/vi/3hEf5RdDFFo/hqdefault.jpg",
"https://media0.giphy.com/media/26n3JnLG4uA5HsmHe/giphy.gif", 
"https://media1.giphy.com/media/3ov9jGH3Wtz7kwUaZi/giphy.gif"]
#----------------------------------------------------------------------------------------------------------------------------------------------------

class FunCommands:
    """Commands of axo"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True)
    async def hug(self, ctx, *, member : discord.Member = None):
        """To Hug someone - ?hug @[username or hug yourself ;( """
        embed = discord.Embed(color = discord.Color(0).gold())
        if member is None:
                embed.description = "{} has been hugged!".format(ctx.message.author.mention)
                embed.set_image(url = "https://media2.giphy.com/media/svXXBgduBsJ1u/giphy.gif")
                await self.bot.say(embed = embed)
        else:
            if member.id == ctx.message.author.id:
                    embed.description = "{} hugged themselves!".format(ctx.message.author.mention)
                    embed.set_image(url = random.choice(huglinks2))
                    await self.bot.say(embed = embed)
            else:
                    embed.description = "{} has been hugged by!".format(member.mention) + "{}!".format(ctx.message.author.mention)
                    embed.set_image(url = random.choice(huglinks))
                    await self.bot.say(embed = embed)

    @commands.command(pass_context=True)
    async def nsfw(self, ctx, *text: str):
        """Shows the top image from a specified subrreddit"""
        if text == ():
            await self.bot.say(nsfwsub)
        elif text[0] != ():
            items = imgurclient.subreddit_gallery(" ".join(text[0:len(text)]), sort='top', window='day', page=0)
            if len(items) < 1:
                await self.bot.say('This subreddit section does not exist, try funny')
            else:
                await self.bot.say(items[0].link)
    
    @commands.command(pass_context = True)
    async def rnsfw(self, ctx, *, member : discord.Member = None):
        """NSFW - Not Safe For Work 18+ - Use at your own risk!"""
        embed = discord.Embed(color = discord.Color(0).gold())
        if member is None:
                embed.description = "{} is a nasty motherfucker".format(ctx.message.author.mention)
                embed.set_image(url = random.choice(nsfwlinks))
                await self.bot.say(embed = embed)

    @commands.command(pass_context = True)
    async def flip(self, ctx):
        """To Flip A Coin"""
        embed = discord.Embed(color = discord.Color(0).gold())
        embed.description = random.choice(tosscoin)
        await self.bot.say(embed = embed)

    @commands.command(pass_context = True)
    async def roll(self, ctx):
        """To roll A Number 1 to 10"""
        embed = discord.Embed(color = discord.Color(0).gold())
        embed.description = "{}".format(random.randint(1, 10))
        await self.bot.say(embed = embed)

    @commands.command(pass_context = True)
    async def dice(self, ctx):
        """To roll A die"""
        embed = discord.Embed(color = discord.Color(0).gold())
        embed.description = "{}".format(random.randint(1, 6))
        await self.bot.say(embed = embed)

    @commands.command(pass_context = True)
    async def nicememe(self, ctx, *, member : discord.Member = None):
        """Nice Meme!"""
        embed = discord.Embed(footer = "sent by axo", color = discord.Color(0).gold())
        if member is None:
                embed.description = "{} salutes you with your fancy meme".format(ctx.message.author.mention)
                embed.set_image(url = random.choice(nicememe))
                await self.bot.say(embed = embed)
        else:
            if member.id == ctx.message.author.id:
                    embed.description = "{} salutes himself!".format(ctx.message.author.mention)
                    embed.set_image(url = random.choice(huglinks2))
                    await self.bot.say(embed = embed)
            else:
                    embed.description = "What a nice meme {}!".format(member.mention)
                    embed.set_image(url = random.choice(nicememe))
                    await self.bot.say(embed = embed)

    @commands.command(pass_context=True)
    async def gif(self, ctx, *, gif = None):
        """Search for some giphy!"""
        try:
            self.giphy = giphypop.Giphy()
            channel = ctx.message.channel
            author  = ctx.message.author
            server  = ctx.message.server

            if not gif == None:
                gif = re.sub(r'([^\s\w]|_)+', '', gif)
            my_gif = None
            if gif == None:
                # Random
                try:
                    my_gif = self.giphy.random_gif()
                except Exception as e:
                    print(e)
                    my_gif = None
            else:
                try:
                    my_gif = self.giphy.search(phrase=gif, limit=20)
                    my_gif = list(my_gif)
                    my_gif = random.choice(my_gif)
                except Exception as e:
                    print(e)
                    my_gif = None
            try:
                gif_url = my_gif["original"]["url"].split("?")[0]
                print(gif_url)
            except:
                gif_url = None
                print(gif_url)
            try:
                title = my_gif["raw_data"]["title"]
                print(title)
            except:
                title = "Gif for \"{}\"".format(gif)
                
            # Download Image
            #await Message.Embed(title=title, image=gif_url, url=gif_url, color=ctx.author).say(ctx)
            try:
                await self.bot.say(gif_url)
            except:
                return
        except:
            return


def setup(bot):
    bot.add_cog(FunCommands(bot))
    print("Fun Commands Ready")