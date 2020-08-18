import discord
from discord.ext import commands
import canvas as Painter
import nekos
import pyshorteners
import random

def shorten(arg):

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(arg)

return x

class Images(commands.Cog):

def __init__(self, bot):

self.bot = bot

@commands.command(aliases=["wai"])
async def waifu(self, ctx):

embed = discord.Embed()

embed.description = "Here's some waifu pic owo"

embed.set_image(url = nekos.img("waifu"))

await ctx.send(file=discord.File(Painter.urltoimage(nekos.img("waifu")), 'ea.png'))

@commands.command()
async def baka(self, ctx, user: discord.Member = None):

msg = ""

embed = discord.Embed()

if user == None:

msg += "Looks like no one did something wrong ".format(ctx.author.mention)

embed.description = msg

embed.set_image(url = nekos.img("baka"))

else:

msg += "Looks like {} did something wrong to {} owo".format(user.mention, ctx.author.mention)

embed.description = msg

embed.set_image(url = nekos.img("baka"))

await ctx.send(embed = embed)

@commands.command()
async def hug(self, ctx, user: discord.Member = None):

yes = ["hug", "cuddle"]

yes_rand = random.choice(yes)

msg = ""

embed = discord.Embed()

if user == None:

msg += "{} hugged no one, sad <:feelsbadman:488514320708272139>".format(ctx.author.mention)

embed.description = msg

embed.set_image(url = nekos.img(yes_rand))

else:

msg += "{} hugged {} owo".format(ctx.author.mention, user.mention)

embed.description = msg

embed.set_image(url = nekos.img(yes_rand))

await ctx.send(embed = embed)

@commands.command()
async def kiss(self, ctx, user: discord.Member = None):

msg = ""

embed = discord.Embed()

if user == None:

msg += "{} kissed no one, sad <:feelsbadman:488514320708272139>".format(ctx.author.mention)

embed.description = msg

embed.set_image(url = nekos.img("kiss"))

else:

msg += "{} kissed {} owo".format(ctx.author.mention, user.mention)

embed.description = msg

embed.set_image(url = nekos.img("kiss"))

await ctx.send(embed = embed)


@commands.command()
async def pat(self, ctx, user: discord.Member = None):

msg = ""

embed = discord.Embed()

if user == None:

msg += "{} patted no one, sad <:feelsbadman:488514320708272139>".format(ctx.author.mention)

embed.description = msg

embed.set_image(url = nekos.img("pat"))

else:

msg += "{} patted {} owo".format(ctx.author.mention, user.mention)

embed.description = msg

embed.set_image(url = nekos.img("pat"))

await ctx.send(embed = embed)

def setup(bot):

bot.add_cog(Images(bot))