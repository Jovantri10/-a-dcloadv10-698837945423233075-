import discord
from discord.ext import commands
import os
import praw
import json
import time
import random
import asyncio
import requests
import bs4
from googletrans import Translator
import datetime

bot = commands.Bot(command_prefix="d/")

class Events(commands.Cog):
  
  def __init__(self, bot):

    self.bot = bot

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):

    if isinstance(error, commands.BotMissingPermissions):

      msg = "```"

      msg += f"Bot missing permission(s): {' '.join(error.missing_perms)}"

      msg += "```"

      await ctx.send(msg)
    
    elif isinstance(error, commands.CommandOnCooldown):
      
      if ctx.author.id == 552492140270452736:
        
        await ctx.reinvoke()
        
        return
      
      msg = "```"
      
      msg += "{}".format(error)
      
      msg += "```"
      
      await ctx.send(msg)
      
    elif isinstance(error, commands.CheckFailure):

      if ctx.author.id == 524969551419670559:

        await ctx.reinvoke()

        return

      msg = "```"

      msg += f"{error}"

      msg += "```"

      await ctx.send(msg)

def setup(bot):
  bot.add_cog(Events(bot))