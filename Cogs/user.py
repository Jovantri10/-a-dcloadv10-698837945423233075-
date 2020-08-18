import discord
from discord.ext import commands
import datetime
from random import randint
import asyncio
from discord import Forbidden
from discord.utils import get
from discord import Embed
from datetime import datetime

class User(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    print('Cogs User Ready')
  
  @commands.command(aliases=['nick-edit', 'setnick'])
  @commands.has_permissions(manage_nicknames=True)
  async def nickedit(self, ctx, member : discord.Member = None, *, rename):
    if member == None:
      return await ctx.send('Please mention user then enter new nickname.', delete_after=10)
    else:
      await member.edit(nick=rename)
      embed = Embed(title='User command', description=f'<a:oweo:712882838331981854> successfully change {member} nickname to {member.mention}', colour=discord.Colour.green(), timestamp=datetime.utcnow())
      embed.set_footer(text=f'Changed by {ctx.author}')
      await ctx.send(embed=embed, delete_after=15)
      await ctx.message.delete()
  
  @nickedit.error
  async def nickedit_error(self,ctx, error):
    if isinstance(error, commands.CheckFailure):
      embed = Embed(title='Error', description=f'{error}', colour=discord.Colour.red(), timestamp=datetime.utcnow())
      await ctx.send(embed=embed)
  
  @commands.command(aliases=['nick-reset', 'resetnick'])
  @commands.has_permissions(manage_nicknames=True)
  async def nickreset(self, ctx, member : discord.Member):
    if member == None:
      return await ctx.send('Please mention user.', delete_after=10)
    else:
      await member.edit(nick=None)
      embed = discord.Embed(title='User command', description=f'<a:oweo:712882838331981854> successfully reset {member} nickname', colour=discord.Colour.green(), timestamp=datetime.utcnow())
      embed.set_footer(text=f'Reset by {ctx.author}')
      await ctx.send(embed=embed, delete_after=15)
      await ctx.message.delete()
  
  @nickreset.error
  async def nickreset_error(self,ctx, error):
    if isinstance(error, commands.CheckFailure):
      embed = Embed(title='Error', description=f'{error}', colour=discord.Colour.red(), timestamp=datetime.utcnow())
      await ctx.send(embed=embed)
      
  @commands.command(pass_context=True, aliases=['ra', 'role-add'])
  @commands.has_permissions(manage_roles=True)
  async def roleadd(self, ctx, member : discord.Member = None, *, role):
    ROLE = discord.utils.get(ctx.guild.roles, name=role)
    if member == None:
      return await ctx.send('Please mention user')
    else:
      await member.add_roles(ROLE)
      embed = Embed(title='User command', description=f'<a:oweo:712882838331981854> successfully add {role} role to {member.mention}', colour=discord.Colour.green(), timestamp=datetime.utcnow())
      embed.set_footer(text=f'Added by {ctx.author}')
      await ctx.send(embed=embed, delete_after=15)
      await ctx.message.delete()
  
  @roleadd.error
  async def roleadd_error(self,ctx, error):
    if isinstance(error, commands.CheckFailure):
      embed = Embed(title='Error', description=f'{error}', colour=discord.Colour.red(), timestamp=datetime.utcnow())
      await ctx.send(embed=embed)
      
  @commands.command(aliases=['role-remove', 'rr'])
  @commands.has_permissions(manage_roles=True)
  async def roleremove(self, ctx, member : discord.Member = None, *, role : discord.Role = None):
    if member == None:
      await ctx.send('Please Mention user and role name')
    else:
      await member.remove_roles(role)
      embed = Embed(title='User command', description=f'<a:oweo:712882838331981854> successfully remove {role} from {member.mention}', colour=discord.Colour.green(), timestamp=datetime.utcnow())
      embed.set_footer(text=f'Remove by {ctx.author}')
      await ctx.send(embed=embed, delete_after=15)
      await ctx.message.delete()
  
  @roleremove.error
  async def roleremove_error(self,ctx, error):
    if isinstance(error, commands.CheckFailure):
      embed = Embed(title='Error', description=f'{error}', colour=discord.Colour.red(), timestamp=datetime.utcnow())
      await ctx.send(embed=embed)
  
def setup(client):
  client.add_cog(User(client))