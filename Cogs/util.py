import discord
import json
from discord import Embed, Colour
from discord.ext import commands
from datetime import datetime
import random

cr = [0x1abc9c, 0x9b59b6, 0x99aab5, 0x7289da, 0xa84300, 0xf1c40f, 0xe91e63, 0x546e7a]

class Util(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name = 'spotify', aliases = ['spot', 'spt'])
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def view_spotify(self, ctx, member : discord.Member = None):
		
		if member is None:
			
			member = ctx.author
			
			e = Embed(colour = random.choice(cr), timestamp = ctx.message.created_at)
			
			e.set_author(name='Spotify', icon_url = 'https://www.freepnglogos.com/uploads/spotify-logo-png/spotify-logo-transparent-spotify-logo-images-25.png')

			e.add_field(name = 'Title', value=f'**```{member.activity.title}```**')
			e.add_field(name = 'Track ID', value=f'**```{member.activity.track_id}```**')
			e.add_field(name = 'Artist', value=f'**```{member.activity.artist}```**')
			e.add_field(name = 'Album', value=f'**```{member.activity.album}```**')
			e.add_field(name = 'Duration', value=f'**```{member.activity.duration}```**')
			e.add_field(name = 'Link', value=f'[{member.activity.title}](https://open.spotify.com/track/{member.activity.track_id})', inline=True)

			e.set_thumbnail(url = member.activity.album_cover_url)
			
			await ctx.send(embed=e)
			
		else:
			
			a = Embed(colour = random.choice(cr), timestamp = datetime.utcnow())
			
			a.set_author(name = 'Spotify', icon_url = 'https://www.freepnglogos.com/uploads/spotify-logo-png/spotify-logo-transparent-spotify-logo-images-25.png')
			
			a.add_field(name = 'Title', value=f'**```{member.activity.title}```**')
			a.add_field(name = 'Track ID', value=f'**```{member.activity.track_id}```**')
			a.add_field(name = 'Artist', value=f'**```{member.activity.artist}```**')
			a.add_field(name = 'Album', value=f'**```{member.activity.album}```**')
			a.add_field(name = 'Duration', value=f'**```{member.activity.duration}```**')
			a.add_field(name = 'Link', value=f'[{member.activity.title}](https://open.spotify.com/track/{member.activity.track_id})', inline=True)
			
			a.set_thumbnail(url = member.activity.album_cover_url)
			
			await ctx.send(embed=a)
			
	@view_spotify.error
	async def view_spotify_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			e = Embed(colour = random.choice(cr), description = 'That member does not listening to spotify')
			await ctx.send(embed=e)
		
def setup(bot):
	bot.add_cog(Util(bot))