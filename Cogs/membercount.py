import discord
from discord.ext import commands
import os
import praw
import json
import random
import asyncio
import urllib3
import requests
import bs4
from discord import *

bot = commands.Bot(command_prefix="d/", owner_id=524969551419670559)

class Membercount(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  def is_owner():
	  async def predicate(ctx):
		  return ctx.author.id == 524969551419670559

	  return commands.check(predicate)
    
    
  @commands.command()
  async def membercount(self, ctx):

    await self.bot.request_offline_members()

    bots = [x for x in ctx.guild.members if x.bot]
    human = [x for x in ctx.guild.members if not x.bot]

    offline = [user for user in ctx.guild.members if user.status == discord.Status.offline]

    dnd = [user for user in ctx.guild.members if user.status == discord.Status.dnd]

    online = [user for user in ctx.guild.members if user.status == discord.Status.online]

    idle = [user for user in ctx.guild.members if user.status == discord.Status.idle]

    embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Colour.blue())
    embed.add_field(name=f"Members on This server : {len(ctx.guild.members)}", value=f":black_circle: Offline : {len(offline)}\n:red_circle: DND : {len(dnd)}\n:yellow_circle: Idle: {len(idle)}\n:green_circle: Online: {len(online)}", inline=False)
    embed.add_field(name="Human Count", value=len(human), inline=False)
    embed.add_field(name="Bot Counts", value=len(bots), inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/713061501333798932/719852524701614141/3208_RainbowSquirtleSquadStrut.gif")
    await ctx.send(embed=embed)
    
def setup(bot):
  m = Membercount(bot)
  bot.add_cog(m)