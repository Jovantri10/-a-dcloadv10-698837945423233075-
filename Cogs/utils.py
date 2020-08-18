import collections
import string
import urllib.parse
import random
import json
import discord
from discord.ext import commands

class Utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def github(self, ctx, gituser):
        if len(gituser)==0:
          await ctx.send("Input text after commands")
        else:
          await ctx.send('https://github.com/' + gituser)

    @commands.command(aliases=['5050', 'flip'])
    async def cointoss(self, ctx):
        choice = random.randint(1, 2)
        
        if choice == 1:
            await ctx.send('heads')
        
        if choice == 2:
            await ctx.send('tails')

def setup(bot):
    bot.add_cog(Utils(bot))