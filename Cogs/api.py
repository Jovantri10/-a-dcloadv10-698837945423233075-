import discord
from discord.ext import commands
import os
import pyfiglet
import datetime
import canvas as Painter
import heapq
import random
import pkg_info
from pkg_info import get_pkg_info
import pyshorteners
import danksearch
import praw
import wikipedia
import json
import websocket
import psutil
import time
import random
import asyncio
import requests
from deku import *
import deku as todo
import bs4
from discord import Embed
import platform
import sys
from psutil import Process
from platform import python_version
from discord.ext import commands
from discord.ext.commands import command, BucketType, cooldown, Cog
import speedtest

import datetime
import typing
import sys
import asyncio
import collections
from discord import Embed
from discord import __version__ as discord_version

import discord, json, time, datetime, json, psutil, platform

cc = commands.command()
sm = commands.cooldown(1, 14, commands.BucketType.user)
cyan = 0, 255, 255
yell = 255, 255, 0 
ung = 191, 0, 255 
vi = 143, 0, 255
liyr = os.environ.get("LIYRIK")
q = os.environ.get("BRAINLY")
k = os.environ.get("KEYEMAS")
say = os.environ.get("SS")
go = os.environ.get("go")
key = os.environ.get("keygo")
numkey = os.environ.get("numbertoken")
joox = os.environ.get("JOOX")
twit = os.environ.get("TWIT")
memek = os.environ.get("MEMEK")
wea = os.environ.get("WEA")
load = os.environ.get("SHOTO")

class Api(commands.Cog):
    
    def __init__(self, bot):

        self.bot = bot
     #   member = ctx.author
        #1
        self.bot.emoji_balance = os.environ.get("BAL")+str(" - Hypesquad Balance\n")
        #2
        self.bot.emoji_bravery = os.environ.get("BRA")+str(" - Hypesquad Bravery\n")
        #3
        self.bot.emoji_brilliance = os.environ.get("BRIL")+str(" - Hypesquad Brilliance\n")
        #4
        self.bot.emoji_devbadge = os.environ.get("VBD")+str(" - Verified Bot Developer\n")
        #5
        self.bot.emoji_earlysupporter = os.environ.get("ES")+str(" - Early Supporter\n")
        
    @commands.command(aliases=["memberinfo","ui"], brief="User not found. Try again")
    @commands.guild_only()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def userinfo(self, ctx, user: discord.Member=None):
        await ctx.channel.trigger_typing()
        if user is None:
            user = ctx.author

        roles = [f"`{r.name}`" for r in user.roles if r.name != "@everyone"][::-1]
        
        ip = "\u200b"
        if user.public_flags.partner:
          ip += os.environ.get("PAR")+str(" - Discord Partner\n")
        if user.public_flags.staff:
          ip += os.environ.get("STA")+str(" - Discord Staff\n")
        if user.public_flags.hypesquad:
          ip += os.environ.get("HE")+str(" - Hypesquad Event\n")
        if user.public_flags.bug_hunter:
          ip += os.environ.get("BH")+str(" - Bug Hunter Level 1\n")
        if user.public_flags.bug_hunter_level_2:
          ip += os.environ.get("GBH")+str(" - Bug Hunter Level 2\n")
        if user.public_flags.hypesquad_brilliance:
          ip += self.bot.emoji_brilliance
        if user.public_flags.hypesquad_bravery:
          ip += self.bot.emoji_bravery
        if user.public_flags.hypesquad_balance:
          ip += self.bot.emoji_balance
        if user.public_flags.verified_bot_developer:
          ip += self.bot.emoji_devbadge
        if user.public_flags.early_supporter:
          ip += self.bot.emoji_earlysupporter
    #    if user.public_flags.
        if user.activity is not None:
            if user.activity.type is discord.ActivityType.listening:
                _type = "Listening to"
                activity = user.activity.title
            elif user.activity.type is discord.ActivityType.streaming:
                _type = "Streaming"
                activity = user.activity.name
            elif user.activity.type is discord.ActivityType.watching:
                _type = "Watching"
                activity = user.activity.name
            else:
                _type = "Playing"
                activity = user.activity.name
        else:
            _type = "Playing"
            activity = "Nothing"

        if user.status is discord.Status.online:
            status = "https://i.imgur.com/WcPjzNt.png"
        elif user.status is discord.Status.idle:
            status = "https://i.imgur.com/UdRIQ2S.png"
        elif user.status is discord.Status.dnd:
            status = "https://i.imgur.com/voWO5qd.png"
        else:
            status = "https://i.imgur.com/8OOawcF.png"

        embed = discord.Embed(description=f"User ID: {user.id}", color=0x2f3136)

        embed.set_author(name=str(user), icon_url=status)
        embed.set_thumbnail(url=user.avatar_url)
        #embed.add_field(name="Badges", value=ip or "None")
        embed.add_field(name="Display Name", value=user.display_name)
        embed.add_field(
            name="Status", value=str(user.status).replace("dnd", "do not disturb").title())
        if user.mobile_status is not discord.Status.offline or user.is_on_mobile():
            embed.add_field(name="Platform", value="Mobile")
        elif user.desktop_status is not discord.Status.offline:
            embed.add_field(name="Platform", value="Desktop")
        elif user.web_status is not discord.Status.offline:
            embed.add_field(name="Platform", value="Web")
        else:
            embed.add_field(name="Platform", value="None")
        embed.add_field(name=_type, value=activity)
        embed.add_field(name="Color", value=str(user.color))
  #      embed.add_field(name="Badges", value=ip or "None")
        if user.voice is not None:
            embed.add_field(name="Voice Channel", value="\U0001f509" + user.voice.channel.name)
            if user.voice.mute or user.voice.self_mute:
                embed.add_field(name="Muted?", value="Yes")
            else:
                embed.add_field(name="Muted?", value="No")
            if user.voice.deaf or user.voice.self_deaf:
                embed.add_field(name="Deafened?", value="Yes")
            else:
                embed.add_field(name="Deafened?", value="No")
        else:
            embed.add_field(name="Voice Channel", value="None")
        if user.top_role is ctx.guild.default_role:
            embed.add_field(name="Top Role", value=user.top_role.name)
        else:
            embed.add_field(name="Top Role", value=user.top_role.mention)
        embed.add_field(name="Joined Server", value=user.joined_at.strftime("%b %-d, %Y"))
        embed.add_field(name="Badges", value=ip or "None")
        if user.bot:
            embed.add_field(name="Bot?", value="Yes")
        else:
            embed.add_field(name="Bot?", value="No")
        embed.add_field(name="Joined Discord", value=user.created_at.strftime("%b %-d, %Y"))
        if roles:
            embed.add_field(
                name=f"Roles ({len(roles)})", value=", ".join(roles), inline=False)
        else:
            embed.add_field(name="Roles", value="`No roles`")        
            
        delta = datetime.datetime.utcnow() - user.created_at

        y = int(delta.total_seconds()) // 31557600  #* Number of seconds in 365.25 days
        mo = int(delta.total_seconds()) // 2592000 % 12  #* Number of seconds in 30 days
        d = int(delta.total_seconds()) // 86400 % 30  #* Number of seconds in 1 day
        h = int(delta.total_seconds()) // 3600 % 24  #* Number of seconds in 1 hour
        mi = int(delta.total_seconds()) // 60 % 60  #* etc.
        se = int(delta.total_seconds()) % 60

        footer = []
        if y != 0:
            footer.append(f"{y} {'year' if y == 1 else 'years'}, ")
        if mo != 0:
            footer.append(f"{mo} {'month' if mo == 1 else 'months'}, ")
        if d != 0:
            footer.append(f"{d} {'day' if d == 1 else 'days'}, ")
        if h != 0:
            footer.append(f"{h} {'hour' if h == 1 else 'hours'}, ")
        if mi != 0:
            footer.append(f"{mi} {'minute' if mi == 1 else 'minutes'}, ")
        footer.append(f"and {se} {'second' if se == 1 else 'seconds'}.")

        embed.set_footer(
            text=user.name + " has been on Discord for roughly " + "".join(footer))

        if user.premium_since is not None:
            await ctx.send(content="\U0001f537 This member is a Nitro server booster since "
                                   f"{user.premium_since.strftime('%b %-d, %Y')}!",
                           embed=embed)
        else:
            await ctx.send(embed=embed)
        
    @commands.command(aliases=["guildinfo","si"])
    @commands.guild_only()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def serverinfo(self, ctx):
      try:
        await ctx.channel.trigger_typing()
        s = ctx.guild

        on_members = [m for m in s.members if m.status is not discord.Status.offline]
        bots = [m for m in s.members if m.bot]
        anim_emojis = [e for e in s.emojis if e.animated]

        embed = discord.Embed(
            title=s.name, description=f"Server ID: {s.id}", color=discord.Colour.dark_blue())
        embed.set_thumbnail(url=s.icon_url)
        embed.set_image(url=s.banner_url)

        embed.add_field(
            name="Members", value=f"{s.member_count} (Online: {len(on_members)})")
        embed.add_field(name="Roles", value=len(s.roles))
        embed.add_field(name="Text Channels", value=len(s.text_channels))
        embed.add_field(name="Voice Channels", value=len(s.voice_channels))
        embed.add_field(name="Categories", value=len(s.categories))
        if anim_emojis:
            embed.add_field(
                name="Custom Emojis",
                value=f"{len(s.emojis)} out of {s.emoji_limit} (Animated: {len(anim_emojis)})")
        else:
            embed.add_field(name="Custom Emojis", value=f"{len(s.emojis)} out of {s.emoji_limit}")
        embed.add_field(name="Bots", value=len(bots))
        try:
            if await s.webhooks():
                embed.add_field(name="Webhooks", value=len(await s.webhooks()))
            else:
                embed.add_field(name="Webhooks", value="None")
        except:
            embed.add_field(name="Webhooks", value="Unknown")
        embed.add_field(name="File Size Upload Limit", value=f"{s.filesize_limit // 1000000} MB")
        embed.add_field(name="Bitrate Limit", value=f"{int(s.bitrate_limit // 1000)} kbps")
        if s.premium_tier:
            embed.add_field(name="Nitro Server Boost Status", value=f"Level {s.premium_tier}")
        else:
            embed.add_field(name="Nitro Server Boost Status", value="No Levels Achieved")
        if s.premium_subscription_count:
            embed.add_field(name="Nitro Server Boosts", value=s.premium_subscription_count)
        else:
            embed.add_field(name="Nitro Server Boosts", value="None")
        if s.system_channel is not None:
            embed.add_field(name="System Channel", value=s.system_channel.mention)
        else:
            embed.add_field(name="System Channel", value="No System Channel")
        embed.add_field(name="Region", value=str(s.region).replace(
            "-", " ").replace("south", "south ").replace("hong", "hong ").title().replace(
                "Us", "U.S.").replace("Eu ", "EUR ").replace("Vip", "V.I.P."))
        if s.mfa_level:
            embed.add_field(name="Requires 2FA?", value="Yes")
        else:
            embed.add_field(name="Requires 2FA?", value="No")
        embed.add_field(name="Default Notification Level",
                        value=str(s.default_notifications)[18:].replace("_", " ").title())
        embed.add_field(name="Verification Level", value=str(s.verification_level).capitalize())
        embed.add_field(name="Explicit Content Filter",
                        value=str(s.explicit_content_filter).replace("_", " ").title())
        if s.afk_channel is not None:
            if s.afk_timeout // 60 == 1:
                minute_s = " minute"
            else:
                minute_s = " minutes"
            embed.add_field(
                name="AFK Channel", value="\U0001f509" + s.afk_channel.name + " after " + str(
                    s.afk_timeout // 60) + minute_s)
        else:
            embed.add_field(name="AFK Channel", value="No AFK channel")
        embed.add_field(name="Server Created", value=s.created_at.strftime("%b %-d, %Y"))
        if s.features:
            embed.add_field(
                name="Server Features",
                value="`" + "`, `".join([f.replace("_", " ") for f in s.features]) + "`",
                inline=False)
        embed.add_field(
            name="Server Owner", value=s.owner.mention + " (User ID: " + str(s.owner_id) + ")",
            inline=False)
        
        delta = datetime.datetime.utcnow() - s.created_at
        
        y = int(delta.total_seconds()) // 31557600  #* Number of seconds in 365.25 days
        mo = int(delta.total_seconds()) // 2592000 % 12  #* Number of seconds in 30 days
        d = int(delta.total_seconds()) // 86400 % 30  #* Number of seconds in 1 day
        h = int(delta.total_seconds()) // 3600 % 24  #* Number of seconds in 1 hour
        mi = int(delta.total_seconds()) // 60 % 60  #* etc.
        se = int(delta.total_seconds()) % 60
     #YANG COPAS DOSA
        footer = []
        if y != 0:
            footer.append(f"{y} {('year' if y == 1 else 'years')}, ")
        if mo != 0:
            footer.append(f"{mo} {'month' if mo == 1 else 'months'}, ")
        if d != 0:
            footer.append(f"{d} {'day' if d == 1 else 'days'}, ")
        if h != 0:
            footer.append(f"{h} {'hour' if h == 1 else 'hours'}, ")
        if mi != 0:
            footer.append(f"{mi} {'minute' if mi == 1 else 'minutes'}, ")
        footer.append(f"and {se} {'second' if se == 1 else 'seconds'}.")

        embed.set_footer(text=s.name + " has been around for roughly " + "".join(footer))

        await ctx.send(embed=embed)
      except Exception as e:
        await ctx.send(e)
        # YANG COPAS MAMAKNYA MATI
        #SUSAH SUSAH W FIX, TINGGAL COPAS KAU, PERGI SANA
    @commands.command()
    async def stats(self, ctx):
      try:
        embed = discord.Embed(
            description=f"User ID: {self.bot.user.id}",
            timestamp=datetime.datetime.utcnow(),
            color=discord.Colour.default())
        embed.add_field(name="Server Count", value=f"{len(self.bot.guilds):,} servers")
        embed.add_field(name="User Count", value=f"{len(self.bot.users):,} unique users")
        embed.add_field(
            name="Channel Count",
            value=f"{len(list(self.bot.get_all_channels()) + self.bot.private_channels):,} "
                  "channels")
        embed.add_field(name="Discord.py version", value=discord.__version__)
        embed.add_field(name="Cpu Count", value=f"{psutil.cpu_count()}")
        embed.add_field(name="Cpu Usage", value=f"{psutil.cpu_percent()} %")
        embed.set_author(name="Todoroki's Bot : Statistics", icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Statistic of Todoroki Shouto Bot")
      except:
        return

    @commands.command(aliases=["uwubot"])
    async def botinfo(self, ctx):
      try:
        app = await self.bot.application_info()

        embed = discord.Embed(
            title=str(self.bot.user), description=app.description +
            f"\n\n**User/Client ID**: {app.id}", color=discord.Colour.default())

        embed.set_thumbnail(url=app.icon_url)
        embed.add_field(name="Version", value="2.3.5")
        embed.add_field(name="Author", value=app.owner)
        embed.add_field(name="Server Count", value=len(self.bot.guilds))
        embed.add_field(
            name="Language",
            value=f"Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}")
        embed.add_field(
            name="Library", value="[discord.py](https://github.com/Rapptz/discord.py)")
        embed.add_field(
            name="License", value="[GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)")
        embed.add_field(name="Github Repo", value="https://github.com/Jovantri10/TodorokiShouto",
                        inline=False)
        embed.set_footer(text=f"Dedicated to {self.bot.get_user(self.bot.owner_id)}")

        await ctx.send(embed=embed)
      except Exception as e:
        await ctx.send(e)
        
    @cc   
    @sm   
    async def lyrics(self, ctx, *args):
      try:
        piu = todo.urlify(' '.join(args))
        txt1 = todo.urlify(piu.split('[')[1][:-2])
        txt2 = todo.urlify(piu.split('[')[2][:-1])
        uy = requests.get(liyr+txt1+txt2).json()["lyrics"]
        embed=discord.Embed(color=discord.Color.blue(), description=uy)
        await ctx.send(embed=embed)
      except Exception as e:
        await ctx.send("```{}```".format(e))
      
      
    @cc 
    @sm    
    async def emote(self, ctx):
      try:
        data = todo.insp('https://discordemoji.com/')
        byEmote = data.split('<div class="float-right"><a href="')
        del byEmote[0]
        alls = []
        for i in range(0, len(byEmote)):
            if byEmote[i].startswith('http'): alls.append(byEmote[i].split('"')[0])
        embed = discord.Embed(colour=discord.Colour.from_rgb(255, 255, 255))
        embed.set_image(url=random.choice(alls))
        embed.set_footer(text="© to null#2144")
        await ctx.send(embed=embed)    
      except Exception as e:
        await ctx.send(f"```{e}```")
        
    @cc   
    @sm    
    async def weather(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Please input the city after commands")
      try:
        bav = todo.urlify(' '.join(args))
        t = requests.get(wea+str(bav)+k).json()["respon"]["tempat"]
        c = requests.get(wea+str(bav)+k).json()["respon"]["cuaca"]
        d = requests.get(wea+str(bav)+k).json()["respon"]["deskripsi"]
        s = requests.get(wea+str(bav)+k).json()["respon"]["suhu"]
        ke = requests.get(wea+str(bav)+k).json()["respon"]["kelembapan"]
        ud = requests.get(wea+str(bav)+k).json()["respon"]["udara"]
        an = requests.get(wea+str(bav)+k).json()["respon"]["angin"]
        memew = discord.Embed(color=discord.Colour.from_rgb(0, 250, 154), description="<a:dcloadv10:698837945423233075> Please waittinngg....")
        embed = discord.Embed(color=discord.Colour.from_rgb(0, 250, 154), title="WEATHER", description=f"Location : **{t}**\nWeather : **{c}**\nDescription : **{d}**\nTemperature : **{s}**\nHumidity : **{ke}**\nAir : **{ud}**\nWind : **{an}**")
        msg = await ctx.send(embed=memew)
        await asyncio.sleep(5)
        await msg.edit(embed=embed)
      except Exception:
        await ctx.send(f"")
        
        
    @cc   
    @sm    
    async def twitter(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Couldnt find someting, pls input twitter user after commands")
      try:
        z = todo.urlify(' '.join(args))
        n = requests.get(twit+str(z)+memek).json()["result"]["name"]
        sn = requests.get(twit+str(z)+memek).json()["result"]["screen_name"]
        d = requests.get(twit+str(z)+memek).json()["result"]["description"]
        pp = requests.get(twit+str(z)+memek).json()["result"]["profilepicture"]
        pb = requests.get(twit+str(z)+memek).json()["result"]["profilebanner"]
        f = requests.get(twit+str(z)+memek).json()["result"]["followers"]
        fol = requests.get(twit+str(z)+memek).json()["result"]["following"]
        li = requests.get(twit+str(z)+memek).json()["result"]["likes"]
        tw = requests.get(twit+str(z)+memek).json()["result"]["tweet"]
        joi = requests.get(twit+str(z)+memek).json()["result"]["joined"]
        embed = discord.Embed(color=discord.Colour.from_rgb(0, 255, 255), description=f"Tag : **{sn}**\nBanner : **[Link]({pb})**\nFollowers : **{f}**\nFollowing : **{fol}**\nLikes : **{li}**\nTweet : **{tw}**\nJoined : **{joi}**\nBio : *{d}*")
        embed.set_author(name=n or "-", icon_url="https://cdn.discordapp.com/attachments/730367960572493828/738343583861702666/124021.png")
        embed.set_thumbnail(url=pp)
        pv = discord.Embed(color=discord.Color.blue(), description="<a:dcloadv10:698837945423233075> Please waitting, getting data....")
        ty = await ctx.send(embed=pv)
        await asyncio.sleep(6)
        await ty.edit(embed=embed)
      except Exception:
        await ctx.send(f"")
        
        
    @cc   
    @sm     
    async def joox(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Pls input song after commands")
      try:
        o = todo.urlify(' '.join(args))
        t = requests.get(joox+str(o)).json()[0]["judul"]
        u = requests.get(joox+str(o)).json()[0]["songid"]
        paa = requests.get(joox+str(o)).json()[0]["penyanyi"]
        i = requests.get(joox+str(o)).json()[0]["album"]
        embed = discord.Embed(color=discord.Colour.from_rgb(0, 255, 255), description=f"Song ID : **{u}**\nArtist : **{paa}**\nAlbum : **{i}**")
        embed.set_author(name=t, icon_url="https://cdn.discordapp.com/attachments/730367960572493828/738319347390349403/JOOX.png")
        await ctx.send(embed=embed)
      except Exception:
        await ctx.send(f"")
      
    @cc  
    @sm   
    async def rem(self, ctx):
      y = requests.get('http://nezumiyuiz.glitch.me/api/rem').json()["url"]
      await ctx.send(file=discord.File(Painter.urltoimage(y), 'rem.png'))
    
    @cc 
    @sm
    async def chika(self, ctx, *args):
      t = requests.get('https://nezumiyuiz.glitch.me/api/chika').json()["url"]
      await ctx.send(file=discord.File(Painter.urltoimage(t), 'chika.png'))
    @cc 
    @sm
    async def hayasaka(self, ctx, *args):
      t = requests.get('https://nezumiyuiz.glitch.me/api/hayasaka').json()["url"]
      await ctx.send(file=discord.File(Painter.urltoimage(t), 'hayasaka.png'))
      
    @cc 
    @sm
    async def kaguya(self, ctx, *args):
      t = requests.get('https://nezumiyuiz.glitch.me/api/kaguyashinomiya').json()["url"]
      await ctx.send(file=discord.File(Painter.urltoimage(t), 'kaguya.png'))
     
    @cc  
    @sm   
    async def megumin(self, ctx, *args):
      y = requests.get('http://nezumiyuiz.glitch.me/api/megumin').json()["url"]
      await ctx.send(file=discord.File(Painter.urltoimage(y), 'megumin.png'))
    
    @cc  
    @sm   
    async def oyasumi(self, ctx):
      y = requests.get('http://nezumiyuiz.glitch.me/api/oyasumi').json()["url"]
      await ctx.send(file=discord.File(Painter.urltoimage(y), 'oyasumi.png'))
    
    @commands.command(aliases=["b64enc"])
    @sm   
    async def b64encode(self, ctx, *args):
      try:
        oy = todo.urlify(' '.join(args))
        ip = requests.get('http://nezumiyuiz.glitch.me/api/base64?text='+str(oy)).json()["base64"]["encode"]
        await ctx.send(ip)
      except Exception as e:
        await ctx.send(f"```ERROR ||{e}||```")
        
    @commands.command(aliases=["b64dec"])
    @sm   
    async def b64decode(self, ctx, *args):
      try:
        oy = todo.urlify(' '.join(args))
        ip = requests.get('http://nezumiyuiz.glitch.me/api/base64?text='+str(oy)).json()["base64"]["decode"]
        await ctx.send(ip)
      except Exception as e:
        await ctx.send(f"```ERROR ||{e}||```")
        
    @cc   
    @sm     
    async def brainly(self, ctx, *args):
      try:
        o = todo.urlify(' '.join(args))
        t = requests.get(q+str(o)+k).json()[0]["title"]
        u = requests.get(q+str(o)+k).json()[0]["url"]
        embed = discord.Embed(color=discord.Colour.from_rgb(0, 255, 255), description=f"**[{t}]({u})**\nSource : [Here](https://brainly.co.id)\nLink Tugas : [Here]({u})")
        embed.set_author(name=t, icon_url="https://cdn.discordapp.com/attachments/730367960572493828/737997714444255282/Screen_20200729_183739_e001.jpg")
        yu = load
        pg = await ctx.send(embed=yu)
        await asyncio.sleep(5)
        await pg.edit(embed=embed)
      except Exception as e:
        await ctx.send(f"```{e}```")
      

    @cc 
    @sm  
    async def google(self, ctx, *args):
      if len(args)==0:
        y = await ctx.send("Searching.......")
        await y.edit(content="Couldn't find what what :V")
      try:
        y = todo.urlify(' '.join(args))
        q = requests.get(go+str(y)+key).json()["query"]["q"]
        ur = requests.get(go+str(y)+key).json()["query"]["url"]
        des = requests.get(go+str(y)+key).json()["knowledge_graph"][0]["description"]
        embed = discord.Embed(color = discord.Colour.from_rgb(255, 255, 0), description=f"**[{q}]({ur})**\n*{des}*")
        embed.set_author(name=q, icon_url='https://cdn.discordapp.com/attachments/730367960572493828/737808399831662694/socialmediaicon_29.png')
        embed.set_footer(text="© Google.com")
        await ctx.send(embed=embed)
      except Exception as e:
        await ctx.send(f"```ERORR BANGG ~> {e}```")
        
    @commands.command(aliases=["screenshoot"])
    @commands.is_nsfw()
    @sm 
    async def ss(self, ctx, *args):
      try:
        o = todo.urlify(' '.join(args))
        yeyy = say+str(o)+'&thumb_width=600&quality=80'
        await ctx.send(file=discord.File(Painter.urltoimage(yeyy), 'screenshoot.png'))
      except Exception as e:
        await ctx.send(f"```{e}```")
      
    @commands.command(pass_context=True)
    @commands.is_owner()
    async def rp(self, ctx, *args):
        if ctx.message.author.id==Config.owner.id:
            try:
                user_to_send = self.bot.get_user(int(args[0]))
                em = discord.Embed(title="Hi, "+user_to_send.name+"! the bot owner sent a response for your suggest and bug!", description=' '.join(list(args)[1:len(list(args))]), colour=discord.Colour.from_rgb(101, 150, 142))
                await user_to_send.send(embed=em)
                await ctx.message.add_reaction('<a:ncgaes:713235013809864774>')
            except Exception as e:
                await ctx.send(f' | Error: `{e}`')
        else:
            await ctx.send('You are not the bot owner. Go get a life.')
    
    @cc
    @sm  
    async def notstonk(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Input text tolol")
      try:
        join = todo.urlify(' '.join(args))
        y = 'https://nezumiyuiz.glitch.me/api/notstonks?avatar='+str(ctx.author.avatar_url).replace('.webp', '.png')+'&text='+str(join)
        await ctx.send(file=discord.File(Painter.urltoimage(y), 'bangpeguigans.png'))
      except Exception as e:
        await ctx.send(f"```{e}```")
        
    @cc 
    @sm 
    async def cofee(self, ctx):
      t = requests.get('https://coffee.alexflipnote.dev/random.json').json()["file"]
      await ctx.send(file=discord.File(Painter.urltoimage(t), 'ea.png'))
      
    @cc
    @sm  
    async def quoteimg(self, ctx):
      url = 'https://quoteimg.glitch.me/generate?height=1080&width=1080&invert=true'
      await ctx.send(file=discord.File(Painter.urltoimage(url), 'ea.png'))
    @cc 
    @sm 
    async def nature(self, ctx):
      n = "https://source.unsplash.com/1600x900/?nature,water"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'nature.png'))
    @cc 
    @sm 
    async def mountain(self, ctx):
      n = "https://source.unsplash.com/1600x900/?nature,mountain"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'mountain.png'))
    @cc 
    @sm 
    async def home(self, ctx):
      n = "https://source.unsplash.com/1600x900/?house,cloud"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'house.png'))
      
    @cc
    @sm  
    async def randomimg(self, ctx):
      br = 'https://loremflickr.com/320/240'
      await ctx.send(file=discord.File(Painter.urltoimage(br), 'random.png'))
     
    @cc 
    @sm  
    async def randomuser(self, ctx, *args):
      await ctx.send("Haha bitj")
      
      
    @cc 
    @sm  
    async def book(self, ctx, *args):
      await ctx.send("Owo try kidding? Cringe")
      
    @cc 
    @sm 
    async def fish(self, ctx):
      n = "https://source.unsplash.com/1600x900/?nature,fish"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'fish.png'))
    @cc 
    @sm 
    async def animal(self, ctx):
      n = "https://source.unsplash.com/1600x900/?nature,animal"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'animal.png'))
    @cc 
    @sm 
    async def river(self, ctx):
      n = "https://source.unsplash.com/1600x900/?nature,river"
      await ctx.send(file=discord.File(Painter.urltoimage(n), 'river.png'))
      
    @cc
    @sm 
    async def kanyequote(self, ctx):
      k = requests.get('https://api.kanye.rest/').json()["quote"]
      await ctx.send(f"```{k}```-Kanye West")

    @cc 
    @sm 
    async def movie(self, ctx, *args):
      tol = todo.urlify(' '.join(args))
      name = requests.get('http://api.tvmaze.com/singlesearch/shows?q='+str(tol)).json()["name"]
      url = requests.get('http://api.tvmaze.com/singlesearch/shows?q='+str(tol)).json()["url"]
      lang = requests.get('http://api.tvmaze.com/singlesearch/shows?q='+str(tol)).json()["language"]
      type = requests.get('http://api.tvmaze.com/singlesearch/shows?q='+str(tol)).json()["type"]
      sta = requests.get('http://api.tvmaze.com/singlesearch/shows?q='+str(tol)).json()["status"]
      embed = discord.Embed(color = discord.Color.green())
      embed.add_field(name="Name", value=f"**```{name}```**")
      embed.add_field(name="URL", value=f"**[{name}]({url})**")
      embed.add_field(name="Language", value=f"**```{lang}```**")
      embed.add_field(name="Tag", value=f"**```{type}```**")
      embed.add_field(name="Status", value=f"**```{sta}```**")
      
      await ctx.send(embed=embed)
    
    @cc 
    @sm   
    async def pixabay(self, ctx, *args):
      pol = todo.urlify(' '.join(args))
      idi = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["id"]
      totk = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["total"]
      toth = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["totalHits"]
      pur = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["pageURL"]
      ty = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["type"]
      ta = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["tags"]
      vi = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["views"]
      do = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["downloads"]
      fa = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["favorites"]
      li = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["likes"]
      com = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["comments"]
      uid = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["user_id"]
      us = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][0]["user"]
      im = requests.get('https://pixabay.com/api/?key=17529787-353264308afb5a00d34d02ba0&q='+str(pol)).json()["hits"][random.randint(0, 5)]["largeImageURL"]
      embed = discord.Embed(color = discord.Color.blue(), description=f"***PIXABAY SEARCHING***\n\nTotal Image : `{totk}`\nTotal Hits : `{toth}`\nID : `{idi}`\nPage : [CLICK HERE]({pur})\nType : `{ty}`\nTags : `{ta}`\nViews : `{vi}`\nDownloads : `{do}`\nFavorites : `{fa}`\nLikes : `{li}`\nComments : `{com}`\nUser ID : `{uid}`\nUser : `{us}`")
      embed.set_image(url=im)
      await ctx.send(embed=embed)
    
    @cc 
    @sm  
    async def anime(self, ctx, *args):
      await ctx.send("```Anime commands on fixed!! Just waitting```")
      
    @cc 
    @sm   
    async def country(self, ctx, *args):
      if len(args)==0:
        await ctx.send("***`Todo.country [country]`***")
      else:
        y = todo.urlify(' '.join(args))
        n = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["name"]
        adc = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["alpha2Code"]
        c = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["capital"]
        r = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["region"]
        sr = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["subregion"]
        p = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["population"]
        t = requests.get('https://restcountries.eu/rest/v2/name/'+str(y)).json()[0]["timezones"]
        embed = discord.Embed(title=n, color=discord.Color.blue(), description=f"Name : **{n}**\nAliases : **{adc}**\nCapital : **{c}**\nRegion : **{r}**\nSubregion : **{sr}**\nPopulation : **{p}**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730294436701012029/735080496656285746/unnamed.gif")
        await ctx.send(embed=embed)
      #except Exception:
        #await ctx.send("Cant find that on country list")
    @cc 
    @sm   
    async def news(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Give the topic news, like this \n***`Todo.news [news]`***")
      else:
        tj = todo.urlify(' '.join(args))
        st = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["status"]
        tr = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["totalResults"]
        d = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["description"]
        t = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["title"]
        a = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["author"]
        ur = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["url"]
        ut = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["urlToImage"]
        pa = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["publishedAt"]
        co = requests.get('http://newsapi.org/v2/everything?q='+str(tj)+'&from=2020-06-21&sortBy=publishedAt&apiKey=f4b326ef98094fa492b9e4605d3a8159').json()["articles"][0]["content"]
        embed = discord.Embed(title="NEWS!", color=discord.Color.blue(), description=f"Status : `{st}`\nResults : `{tr}`\n\nTitle : **`{t}`**\nAuthor : **`{a}`**\nURL : **[{t}]({ur})**\nPublished At : **`{pa}`**\nContent : ***`{co}`***")
        #Description : ***`{d}`***")
        embed.set_thumbnail(url=ut)
        await ctx.send(embed=embed)
      
    @cc 
    @sm   
    async def aes(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Please input the text!")
      if len(' '.join(list(args)))>100:
        await ctx.send("Yea spam, no bish leave")
      else:
        y = todo.urlify(' '.join(args))
        u = requests.get('https://nezumiyuiz.glitch.me/api/aesthetic?text='+str(y)).json()["aesthetic"]
        await ctx.send(u)
    @cc 
    @sm   
    async def aessc(self, ctx, *args):
      y = todo.urlify(' '.join(args))
      u = requests.get('https://nezumiyuiz.glitch.me/api/aesthetic?text='+ctx.channel).json()["aesthetic"]
      await ctx.send(u)
    @cc 
    @sm 
    async def reverse(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Please input text for reversed")
      if len(' '.join(list(args)))>100:
        await ctx.send("Yea spam, no bish leave")
      else:
        u = todo.urlify(' '.join(args))
        o = requests.get('https://nezumiyuiz.glitch.me/api/reverse?text='+str(u)).json()["reverse"]
        await ctx.send(o)
    @cc
    @sm 
    async def fancy(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Input text!")
      if len(' '.join(list(args)))>100:
        await ctx.send("Yea spam, no bish leave")
      else:
        y = todo.urlify(' '.join(args))
        o = requests.get('https://nezumiyuiz.glitch.me/api/fancy?text='+str(y)).json()["fancy"]
        await ctx.send(o)
    @cc
    @sm 
    async def fliptext(self, ctx, *args):
      if len(args)==0:
        await ctx.send("Input text!")
      if len(' '.join(list(args)))>100:
        await ctx.send("Yea spam, no bish leave")
      else:
        y = todo.urlify(' '.join(args))
        o = requests.get('https://nezumiyuiz.glitch.me/api/fliptext?text='+str(y)).json()["fliptext"]
        await ctx.send(o)
        
    @cc 
    @sm
    async def zerotwo(self, ctx, *args):
      t = requests.get('https://nezumiyuiz.glitch.me/api/zerotwo').json()["url"]
      await ctx.send(file=discord.File(Painter.urltoimage(t), 'zerotwo.png'))
    
    @cc 
    @sm   
    async def findip(self, ctx, *args):
      if (args)==0:
        await ctx.send("Please input ip after ***`Todo.ip [ip]`***")
      try:
        urli = todo.urlify(' '.join(args))
        i = requests.get('https://ipapi.co/'+str(urli)+'/json/').json()["ip"]
        c = requests.get('https://ipapi.co/'+str(urli)+'/json/').json()["city"]
        r = requests.get('https://ipapi.co/'+str(urli)+'/json/').json()["region_code"]
        embed = discord.Embed(title=i, color=discord.Color.blue(), description=f"City : **`{c}`**\nAliases City : **`{r}`**\n")
        await ctx.send(embed=embed)
      except Exception:
        await ctx.send("Cant find the ip, sorry:v")
    
    @cc 
    @sm 
    async def sof(self, ctx, *args):
      if len(list(args))==0:
        await ctx.send("Input the questions")
      try:
        t = todo.urlify(' '.join(args))
        ti = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["title"]
        li = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["link"]
        ia = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["is_answered"]
        ac = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["answer_count"]
        vw = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["view_count"]
        qi = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["question_id"]
        pi = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["owner"]["profile_image"]
        dn = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["owner"]["display_name"]
        ui = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["owner"]["user_id"]
        ut = requests.get("https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q="+str(args)).json()["items"][0]["owner"]["user_type"]
        embed = discord.Embed(color=discord.Color.blue(), description=f"**[{ti}]({li})**\nAnswered : **{ia}**\nAnswer Count : **{ac}**\nView Count : **{vw}**\nQuestion ID : **{qi}**\n\nBy : **{dn}**\nID : **{ui}**\nType : **{ut}**\n")
        embed.set_thumbnail(url=pi)
        embed.set_footer(text="© Stackoverflow.com")
        await ctx.send(embed=embed)
      except Exception as e:
        await ctx.send(f"Error | `{e}`")
  
        
def setup(bot):
  bot.add_cog(Api(bot))