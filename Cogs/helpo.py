import discord
from discord.ext import commands
import paginator
from disputils import BotEmbedPaginator
from discord import Embed
import random

held = ["https://cdn.discordapp.com/attachments/741845376314769468/743703038195138580/tenor_1.gif","https://cdn.discordapp.com/attachments/741845376314769468/743703037914251284/tenor_2.gif","https://cdn.discordapp.com/attachments/741845376314769468/743703037490626600/tenor_3.gif","https://cdn.discordapp.com/attachments/741845376314769468/743703037167796324/tenor_4.gif","https://cdn.discordapp.com/attachments/741845376314769468/743689816985698394/tenor.gif"]
lala = [0x1abc9c, 0x9b59b6, 0x99aab5, 0x7289da, 0xa84300, 0xf1c40f, 0xe91e63, 0x546e7a]

class Help(commands.Cog):
	"""Utility commands"""
	def __init__(self, bot):
		
		self.bot = bot
		self.bot.remove_command('help')
		
	@commands.command(aliases=["help"])
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def cmd(self, ctx):
	  try:
	    embed = discord.Embed(description=f"Hi {ctx.author}, My Prefix is `todo.`\nThis all list my commands\n\n**```play - skip - stop - queue - volume - pruning - shuffle - loop```**\n**```aes - twitter - reverse - b64dec - b64enc - notstonk - joox - screenshoot - fliptext - fancy - trash - achiv - captchatxt - caption - baby - sepia - respect - gray - art - disgusting - ferbtv - findlyrics - locate - 8ball - testmemory - emojify - minecraft - youtube```**\n**```spotify - translate - wiki - weather - urban - country - serverinvite - roleinfo - stats - channel-info - serverinfo - userinfo - userroles - topsecretloli - hayasaka - megumin - zerotwo - rem - ping - joined - top_role - afk```**\n**```asciify - f - f-leaderboard - meme - poll - pypi - membercount - invert - blur - pixelate - snow - gay - communist - sepia - gray - jpegify - cofee - nature - river - mountain - fish - home - randomimg - catfact - cat - dog - duck - goat - snake - animal```**", color=0x2f3136)
	    embed.set_footer(text=f"Executed by {ctx.author}")
	    embed.set_image(url=random.choice(held))
	    await ctx.send(embed=embed)
	  except Exception as e:
	    await ctx.send("Error | `{}`".format(e))
	    
def setup(bot):
	bot.add_cog(Help(bot))