from discord.ext import commands
import discord
from discord import Permissions
import sys
import asyncio
import sys
import canvas as Painter
import algorithm
from subprocess import run, PIPE
from inspect import isawaitable
from asyncio import sleep
import os 
import deku as todo
from deku import *

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.protected_files = [ # CONFIDENTIAL FILES
            os.environ['BABI'],
            os.environ['KSOFT_TOKEN'],
            os.environ['YOUTUBE_API_KEY']
        ]

    async def cog_check(self, ctx):
        if not await ctx.bot.is_owner(ctx.author):
            raise commands.NotOwner('Owner only.')
        return True
       
        
    @commands.command(name='status')
    async def change_status(self, ctx, status: str = ""):
        """Change bot's status between: offline, idle, dnd and online"""
        status = status.lower()
        if status == 'offline' or status == 'off' or status == 'invisible':
            discordStatus = discord.Status.invisible
        elif status == 'idle':
            discordStatus = discord.Status.idle
        elif status == 'dnd' or status == 'disturb':
            discordStatus = discord.Status.dnd
        else:
            discordStatus = discord.Status.online
        await self.bot.change_presence(status=discordStatus)

    @commands.command(name='name')
    async def change_name(self, ctx, *, name = None):
        """Change bot's name in the guild"""
        await ctx.guild.me.edit(nick=name)

def setup(bot):
    bot.add_cog(owner(bot))