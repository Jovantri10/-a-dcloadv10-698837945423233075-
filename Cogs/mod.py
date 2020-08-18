import discord
from discord.ext import commands
from discord import Embed
import datetime
import json
from datetime import datetime
from discord.utils import get
import asyncio
from asyncio import sleep

class Mod(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    print('Moderation cog ready')
  
  @commands.Cog.listener()
  async def error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f'```{error}```')
    elif isinstance(error, commands.BotMissingPermissions):
      await ctx.send(f'```{error}```')
    else:
      pass
  

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member = None, *, reason=None):
  	if member == None:
  		how = Embed(description='{}, Pls mention someone and input reason.'.format(ctx.author.mention), colour=ctx.author.colour)
  		await ctx.send(embed=how)
  	elif member.guild_permissions.administrator == True:
  		note = Embed(description='😕 Are u kidding? I dont can kick Moderator or Admin', colour=discord.Colour.red())
  		await ctx.send(embed=note)
  	elif reason == None:
  		return await ctx.send('Almost ready! Give the reason and try')
  	else:
  		await member.kick(reason=reason)
  		embed = Embed(description=f'<a:Chekbaru:712209716645724221> {member.name} has kicked with reason : {reason}', colour=discord.Colour.red())
  		await ctx.send(embed=embed)
  
  @commands.command()
  @commands.cooldown(1, 2, commands.BucketType.user)
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member = None, *, reason=None):
  	if member == None:
  		how = Embed(description='{}, Pls mentioned someone with input reason.'.format(ctx.author.mention), colour=ctx.author.colour)
  		await ctx.send(embed=how)
  	elif member.guild_permissions.administrator == True:
  		note = Embed(description='🙃 Are u kidding? I dont can to ban administrator / owner', colour=discord.Colour.red())
  		await ctx.send(embed=note)
  	elif reason == None:
  		return await ctx.send('Please enter a reason and try again')
  	else:
  		await member.ban(reason=reason)
  		embed = Embed(description=f'<a:Chekbaru:712209716645724221> {member.name} has **banned** because the reason : {reason}', colour=discord.Colour.red())
  		await ctx.send(embed=embed)
  
def setup(bot):
  bot.add_cog(Mod(bot))