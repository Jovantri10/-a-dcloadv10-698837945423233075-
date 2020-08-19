import discord
import canvas as Painter
import requests
import datetime, time
from discord.ext import commands
import asyncio
from asyncio import sleep
from discord.utils import get
import keep_alive
from keep_alive import keep_alive
import udpy
from udpy import UrbanClient
import disputils
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import json
import os
import random
from random import randint
from PIL import Image
import requests
import deku as todo
import statcord
from deku import *

client = discord.Client
client = commands.Bot(command_prefix=["todo.","Todo."],owner_id=552492140270452736)
#Set the command prefix to what you preferrint(f'Logged in as {bot.user.name} - {bot.user.id}')
bot = client
todoroki = bot

async def statuschange():
	while not client.is_closed():
		await bot.wait_until_ready(
		)  # Makes the bot wait until it's fully ready before the stuff below are ran
		await bot.change_presence(
		    status=discord.Status.dnd,
		    activity=discord.Activity(
		        type=discord.ActivityType.watching,
		        name=f"{len(bot.guilds)} Guild's | todo.help",
		        url="https://www.twitch.tv/pkidz2123"))
		await asyncio.sleep(
		    8
		)  # Makes it wait another 8 seconds and then it'll go back to the top on playing because we used "while" which makes it look
		await bot.change_presence(
		    status=discord.Status.dnd,
		    activity=discord.Activity(
		        type=discord.ActivityType.listening,
		        name=f"Class 1-A with {len(bot.users)} hero",
		        url="https://www.twitch.tv/pkidz2123"))
		await asyncio.sleep(8)

extensions = ['Cogs.topgg','Cogs.image','Cogs.justme', 'Cogs.vaan', 'Cogs.commands', 'Cogs.api', 'Cogs.utils','Cogs.ownerr', 'Cogs.util', 'Cogs.jishaku','Cogs.helpo','Cogs.ksoft', 'Cogs.afk', 'Cogs.snipe', 'Cogs.membercount','Cogs.Members', 'Cogs.Owner']

if __name__ == '__main__':
	for extension in extensions:
		client.load_extension(extension)

bot.remove_command('help')
@bot.event
async def on_ready():
	print(f'Logged in as {bot.user.name} - {bot.user.id}')
#	bot.remove_command('help')

import statcord
key = 'statcord.com-c9AeEy6Wic9clB5nIxH0'
api = statcord.Client(bot, key)
api.start_loop()

@bot.event
async def on_command(ctx, *args):
	y = bot.get_channel(713061501333798932)
	lo = bot.get_channel(736792598458531892)
	await lo.send(f"**```{ctx.author} | {ctx.author.id} |\nUse {ctx.command.name} Commands\n-----------------------------------------------```**")
	api.command_run(ctx)

@todoroki.command(
    helpinfo='Looks up a sequence of numbers', aliases=['numbers', 'integers'])
async def oeis(ctx, *, number: str):
	'''
    Looks up a sequence of numbers
    '''
	req = requests.get('https://oeis.org/search?q={}&fmt=json'.format(
	    number)).json()['results'][0]
	numid = 'A' + str(req['number']).zfill(6)
	embed = discord.Embed(
	    title='**' + numid + '**',
	    url='https://oeis.org/{}'.format(numid),
	    description='**' + req['name'] + '**',
	    color=0xFF0000)
	embed.add_field(name="Numbers:", value=str(req['data']), inline=False)
	embed.set_image(url='https://oeis.org/{}/graph?png=1'.format(numid))
	embed.set_thumbnail(url='https://oeis.org/oeis_logo.png')
	embed.set_footer(text='OEIS', icon_url='https://oeis.org/oeis_logo.png')
	embed.set_author(
	    name='OEIS.org',
	    url='https://oeis.org/',
	    icon_url='https://oeis.org/oeis_logo.png')
	embed.timestamp = datetime.datetime.utcnow()
	await ctx.send(
	    '**Search result for:** ***{}...***'.format(number), embed=embed)


held = ["https://cdn.discordapp.com/attachments/741845376314769468/743703038195138580/tenor_1.gif","https://cdn.discordapp.com/attachments/741845376314769468/743703037914251284/tenor_2.gif","https://cdn.discordapp.com/attachments/741845376314769468/743703037490626600/tenor_3.gif","https://cdn.discordapp.com/attachments/741845376314769468/743703037167796324/tenor_4.gif","https://cdn.discordapp.com/attachments/741845376314769468/743689816985698394/tenor.gif"]
lala = [0x1abc9c, 0x9b59b6, 0x99aab5, 0x7289da, 0xa84300, 0xf1c40f, 0xe91e63, 0x546e7a]
t = todoroki.command()
cd = commands.cooldown(1, 12, commands.BucketType.user)
owner = 552492140270452736

@bot.command()
@cd
async def bug(ctx, *, msg: str):
	own = bot.get_user(552492140270452736)
	lol = bot.get_channel(726671245621592175)
	serverinvite = await ctx.message.channel.create_invite(
	    reason='Requested by ' + str(ctx.message.author.name))
	color = discord.Color(value=0x00ff00)
	em = discord.Embed(color=color, title="Bug reported!")
	em.description = f"Bug : {msg}\nBug sent by {ctx.author}\nInvite : [Link]({serverinvite})"
	await lol.send(embed=em)
	await own.send(ctx.author.id)
	await ctx.send(
	    "Thanks for reporting that bug! We will send your report now!.")
	    
@bot.command()
@cd
async def suggest(ctx, *, msg: str):
	"""Got a PROB? Tell us about it...  """
	o = ''.join(list(msg))
	invite = await ctx.message.channel.create_invite(
	    reason='Requested by ' + str(ctx.message.author.name))
	lol = bot.get_channel(726827658528161804)
	color = discord.Color(value=0x00ff00)
	em = discord.Embed(color=color, title="Suggestion!")
	em.description = f"Suggest : ***{o}***\nID : ***{ctx.author.id}***\nServer : [Invite]({invite})"
	em.set_footer(text=f"Suggest sent by {ctx.message.author}")
	await lol.send(embed=em)
	await ctx.send("Thanks for Your Suggest!.")

@todoroki.command(aliases=["trg"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def triggered(ctx):
	if len(ctx.message.mentions) == 0:
		gola = 'https://useless-api--vierofernando.repl.co/triggered?image=' + str(
		    ctx.author.avatar_url) + '&increment=5'.replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(gola), 'vierofernando.png'))
	try:
		go = 'https://useless-api--vierofernando.repl.co/triggered?image=' + str(
		    ctx.message.mentions[0].avatar_url) + '&increment=5'.replace(
		        '.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(go), 'vierofernando.png'))
	except Exception as e:
		await ctx.send(f"```404 ~> {e}```")

@t
@cd
async def ping(ctx):
	ping = client.latency
	ping = round(ping * 1000)
	await ctx.send("<:wipii:736786400069943398> Pong! `{} ms`".format(ping))

@t
@cd
async def contributors(ctx):
	await ctx.send(
	    f"<a:ncgaes:713235013809864774> ***SPECIAL THANKS***\n**```{bot.get_user(661200758510977084).name}#{bot.get_user(661200758510977084).discriminator} | {bot.get_user(271576733168173057).name}#{bot.get_user(271576733168173057).discriminator} | {bot.get_user(493768058012172288).name}#{bot.get_user(493768058012172288).discriminator} | {bot.get_user(524969551419670559).name}#{bot.get_user(524969551419670559).discriminator}```**"
	)

@todoroki.command(aliases=["jpgif"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def jpegify(ctx):
	if len(ctx.message.mentions) == 0:
		gola = 'https://api.alexflipnote.dev/filter/jpegify?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(gola), 'jpegify.png'))
	if len(ctx.message.mentions) == 1:
		go = 'https://api.alexflipnote.dev/filter/jpegify?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(go), 'jpegify.png'))

@todoroki.command(aliases=["snw"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def snow(ctx):
	if len(ctx.message.mentions) == 0:
		gola = 'https://api.alexflipnote.dev/filter/snow?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(file=discord.File(Painter.urltoimage(gola), 'snow.png'))
	if len(ctx.message.mentions) == 1:
		go = 'https://api.alexflipnote.dev/filter/snow?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(file=discord.File(Painter.urltoimage(go), 'snow.png'))

@todoroki.command(aliases=["bisex"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def gay(ctx):
	if len(ctx.message.mentions) == 0:
		gola = 'https://api.alexflipnote.dev/filter/gay?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(file=discord.File(Painter.urltoimage(gola), 'gay.png'))
	if len(ctx.message.mentions) == 1:
		go = 'https://api.alexflipnote.dev/filter/gay?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(file=discord.File(Painter.urltoimage(go), 'gay.png'))

@todoroki.command(aliases=["cmnst"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def communist(ctx):
	if len(ctx.message.mentions) == 0:
		gola = 'https://api.alexflipnote.dev/filter/communist?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(gola), 'idontlikethis.png'))
	if len(ctx.message.mentions) == 1:
		go = 'https://api.alexflipnote.dev/filter/communist?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(go), 'idonlikethis.png'))

@t
@cd
async def fml(ctx):
	aq = requests.get('https://api.alexflipnote.dev/fml').json()["text"]
	await ctx.send(aq)

@todoroki.command(aliases=["plt"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def pixelate(ctx):
	if len(ctx.message.mentions) == 0:
		gola = 'https://api.alexflipnote.dev/filter/pixelate?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(gola), 'pixelalex.png'))
	if len(ctx.message.mentions) == 1:
		go = 'https://api.alexflipnote.dev/filter/pixelate?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(go), 'pixelalex.png'))

@todoroki.command(aliases=["blr"])
@commands.cooldown(1, 12, commands.BucketType.user)
async def blur(ctx):
	if len(ctx.message.mentions) == 0:
		gola = 'https://api.alexflipnote.dev/filter/blur?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(file=discord.File(Painter.urltoimage(gola), 'blur.png'))
	if len(ctx.message.mentions) == 1:
		go = 'https://api.alexflipnote.dev/filter/blur?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(file=discord.File(Painter.urltoimage(go), 'blur.png'))

@t
@cd
async def invert(ctx):
	if len(ctx.message.mentions) == 0:
		gola5 = 'https://nezumiyuiz.glitch.me/api/invert?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(gola5), 'bangepguigans.png'))
	else:
		s = 'https://nezumiyuiz.glitch.me/api/invert?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(s), 'bangpeguigans.png'))
		await ctx.send(f"```404 ~> {e}```")

@t
@cd
async def goat(ctx):
	await ctx.send(
	    file=discord.File(
	        Painter.urltoimage('https://placegoat.com/' +
	                           str(random.randint(500, 700))), 'goat.png'))

@t
@cd
async def snake(ctx):
	await ctx.send(
	    file=discord.File(
	        Painter.urltoimage('https://fur.im/snek/i/' +
	                           str(random.randint(1, 874)) +
	                           '.png'), 'snek.png'))

@t
@cd
async def iotd(ctx):
	data = todo.jsonisp(
	    'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'
	)['images'][0]
	embed = discord.Embed(
	    title=data['copyright'],
	    url=data['copyrightlink'],
	    color=discord.Color.from_rgb(201, 160, 112))
	embed.set_image(url='https://bing.com' + data['url'])
	await ctx.send(embed=embed)

@t
@cd
async def trash(ctx):
	if len(ctx.message.mentions) == 0:
		await ctx.send('Please mention someone!')
	else:
		async with ctx.message.channel.typing():
			av = ctx.message.author.avatar_url
			toTrash = ctx.message.mentions[0].avatar_url
			url = 'https://api.alexflipnote.dev/trash?face=' + str(av).replace(
			    'webp', 'png') + '&trash=' + str(toTrash).replace(
			        'webp', 'png')
			data = Painter.urltoimage(url)
			await ctx.send(file=discord.File(data, 'trash.png'))

@t
@cd
async def textimg(ctx, *args):
	if len(args) == 0:
		await ctx.send("Input the text!")
	if len(' '.join(list(args))) > 50:
		await ctx.send("The word is limit")
	else:
		async with ctx.message.channel.typing():
			txt = todo.urlify(' '.join(args))
			data = Painter.urltoimage(
			    'https://useless-api--vierofernando.repl.co/texttoimage?text='
			    + str(txt))
			await ctx.send(file=discord.File(data, 'viero.png'))

@t
@cd
async def captchatxt(ctx, *args):
	async with ctx.message.channel.typing():
		if len(args) == 0:
			await ctx.send("Input the Text!")
		else:
			capt = todo.urlify(' '.join(args))
			data = Painter.urltoimage(
			    'https://api.alexflipnote.dev/captcha?text=' + str(capt))
			await ctx.send(file=discord.File(data, 'captcha.png'))

@t
@cd
async def serverinvite(ctx):
	if not ctx.message.author.guild_permissions.create_instant_invite:
		await ctx.send(':x: Sorry u dont have perms')
	else:
		serverinvite = await ctx.message.channel.create_invite(
		    reason='Requested by ' + str(ctx.message.author.name))
		await ctx.send('<a:load:713196760264212570> Succes! Link: **<' +
		               str(serverinvite) + '>**')

@todoroki.command(aliases=["disg"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def disgusting(ctx):
	if len(ctx.message.mentions) == 0:
		gola = 'https://useless-api--vierofernando.repl.co/disgusting?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(gola), 'vierofernando.png'))
	if len(ctx.message.mentions) == 1:
		go = 'https://useless-api--vierofernando.repl.co/disgusting?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(go), 'vierofernando.png'))

@todoroki.command()
async def duck(ctx):
	await ctx.send(
	    file=discord.File(
	        Painter.urltoimage(
	            todo.jsonisp('https://random-d.uk/api/v2/random?format=json')
	            ['url']), 'duck.png'))

@todoroki.command(aliases=["ftv"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def ferbtv(ctx):
	if len(ctx.message.mentions) == 0:
		gy = 'https://useless-api--vierofernando.repl.co/ferbtv?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(gy), 'vierofernando.png'))
	else:
		bbi = 'https://useless-api--vierofernando.repl.co/ferbtv?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(bbi), 'vierofernando.png'))

@todoroki.command(aliases=["art"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def artmeme(ctx):
	if len(ctx.message.mentions) == 0:
		golam = 'https://useless-api--vierofernando.repl.co/art?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(golam), 'vierofernando.png'))
	else:
		uu = 'https://useless-api--vierofernando.repl.co/art?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(uu), 'vierofernando.png'))

@todoroki.command(aliases=["gray"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def grayscale(ctx):
	if len(ctx.message.mentions) == 0:
		golat = 'https://useless-api--vierofernando.repl.co/grayscale?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(golat), 'vierofernando.png'))
	else:
		g = 'https://useless-api--vierofernando.repl.co/grayscale?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(g), 'vierofernando.png'))

@todoroki.command(aliases=["resp"])
@commands.cooldown(1, 8, commands.BucketType.user)
async def respect(ctx):
	if len(ctx.message.mentions) == 0:
		golay = 'https://useless-api--vierofernando.repl.co/respects?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(golay), 'vierofernando.png'))
	else:
		f = 'https://useless-api--vierofernando.repl.co/respects?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(f), 'vierofernando.png'))

@todoroki.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def sepia(ctx):
	if len(ctx.message.mentions) == 0:
		gola5 = 'https://nezumiyuiz.glitch.me/api/sepia?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(gola5), 'bangepguigans.png'))
	else:
		s = 'https://nezumiyuiz.glitch.me/api/sepia?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(s), 'bangpeguigans.png'))

@todoroki.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def baby(ctx):
	if len(ctx.message.mentions) == 0:
		gola1 = 'https://useless-api--vierofernando.repl.co/baby?image=' + str(
		    ctx.author.avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(gola1), 'vierofernando.png'))
	else:
		b = 'https://useless-api--vierofernando.repl.co/baby?image=' + str(
		    ctx.message.mentions[0].avatar_url).replace('.webp', '.png')
		await ctx.send(
		    file=discord.File(Painter.urltoimage(b), 'credittonull#8626.png'))

@t
@cd
async def achiv(ctx, *args):
	async with ctx.message.channel.typing():
		if len(args) == 0:
			await ctx.send("Input the Text!")
		else:
			capt = todo.urlify(' '.join(args))
			data = Painter.urltoimage(
			    'https://api.alexflipnote.dev/achievement?text=' + str(capt))
			await ctx.send(file=discord.File(data, 'credittoalex.png'))

@todoroki.command()
@commands.cooldown(1, 6, commands.BucketType.user)
async def catfact(ctx):
	cat = requests.get("https://some-random-api.ml/facts/cat").json()['fact']
	em = discord.Embed(
	    title=
	    "<a:boosterinbgsd:712992968990130189> Cat Fact <a:boosterinbgsd:712992968990130189>",
	    description=f"**```{cat}```**\n-CatFact",
	    color=discord.Color.blue())
	await ctx.send(embed=em)

@todoroki.command(helpinfo='Wikipedia summary', aliases=['w', 'wiki'])
@commands.cooldown(1, 4, commands.BucketType.user)
async def wikipedia(ctx, *, query: str):
	'''
    Uses Wikipedia APIs to summarise search
    '''
	sea = requests.get(
	    ('https://en.wikipedia.org//w/api.php?action=query'
	     '&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop='
	     ).format(query)).json()['query']

	if sea['searchinfo']['totalhits'] == 0:
		await ctx.send('Sorry, your search could not be found.')
	else:
		for x in range(len(sea['search'])):
			article = sea['search'][x]['title']
			req = requests.get(
			    'https://en.wikipedia.org//w/api.php?action=query'
			    '&utf8=1&redirects&format=json&prop=info|images'
			    '&inprop=url&titles={}'.format(
			        article)).json()['query']['pages']
			if str(list(req)[0]) != "-1":
				break
		else:
			await ctx.send('Sorry, your search could not be found.')
			return
		article = req[list(req)[0]]['title']
		arturl = req[list(req)[0]]['fullurl']
		artdesc = requests.get(
		    'https://en.wikipedia.org/api/rest_v1/page/summary/' +
		    article).json()['extract']
		lastedited = datetime.datetime.strptime(req[list(req)[0]]['touched'],
		                                        "%Y-%m-%dT%H:%M:%SZ")
		embed = discord.Embed(
		    title='**' + article + '**',
		    url=arturl,
		    description=artdesc,
		    color=0x3FCAFF)
		embed.set_footer(
		    text='Wiki entry last modified',
		    icon_url=
		    'https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png'
		)
		embed.set_author(
		    name='Wikipedia',
		    url='https://en.wikipedia.org/',
		    icon_url=
		    'https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png'
		)
		embed.timestamp = lastedited
		await ctx.send(
		    '**Search result for:** ***"{}"***:'.format(query), embed=embed)

@bot.event
async def on_guild_join(guild):
	lol = bot.get_channel(726676707226157076)
	em = discord.Embed(color=discord.Color(value=0x2f3136))
	em.title = f"Todoroki kun bot has arrived in new guids!"
	em.description = f"<a:HatiMel:712209640750055464> Server Name : **{guild}**\n<a:HatiMel:712209640750055464> Server Count : {len(bot.guilds)} servers!"
	await lol.send(embed=em)

@bot.command(aliases=['topgg',"invite"])
async def vote(ctx):
	y = "You can vote me every 12 hours! Remember!"
	vote = "https://top.gg/bot/714330708365148190"
	embed = discord.Embed(
	    title=
	    "<a:verify10:698678441502965851> VOTE OR INVITE ME <a:verify10:698678441502965851>"
	)
	embed.description = f"*{y}*\nVote or Invite me on here \n [Here Love -]({vote})"
	embed.timestamp = ctx.message.created_at
	embed.color = discord.Color.blue()
	embed.set_footer(text=f"{ctx.author.name}")
	embed.set_thumbnail(url=bot.user.avatar_url)
	await ctx.send(embed=embed)

@bot.event
async def on_guild_remove(guild):
	lol = bot.get_channel(726827078543999099)
	em = discord.Embed(color=discord.Color(value=0x2f3136))
	em.title = f"Todoroki Kun bot has been removed from guild"
	em.description = f"<a:Chekbaru:712209716645724221> Server : **{guild}**\n<a:Chekbaru:712209716645724221> Server Count : {len(bot.guilds)} Servers"
	await lol.send(embed=em)

@bot.command(aliases=["urb"])
@commands.is_nsfw()
@commands.cooldown(1, 3, commands.BucketType.user)
async def urban(ctx, *, arg=None):

	if arg == None:
		embederror = discord.Embed()
		embederror.title = ":x: Invalid argument"
		embederror.description = "**Todo.urban [search]**"
		embederror.color = discord.Color.red()
		return await ctx.send(embed=embederror)
	try:
		urban = UrbanClient()

		defs = urban.get_definition(arg)

		def0 = defs[0]

		def1 = defs[1]

		def2 = defs[2]

		def3 = defs[3]

		def4 = defs[4]

		embeds = [
		    discord.Embed(
		        title=f"Urban Dictionary - {arg}",
		        description=def0.definition,
		        color=discord.Color.green()),
		    discord.Embed(
		        title=f"Urban Dictionary - {arg}",
		        description=def1.definition,
		        color=discord.Color.green()),
		    discord.Embed(
		        title=f"Urban Dictionary - {arg}",
		        description=def2.definition,
		        color=discord.Color.green()),
		    discord.Embed(
		        title=f"Urban Dictionary - {arg}",
		        description=def3.definition,
		        color=discord.Color.green()),
		    discord.Embed(
		        title=f"Urban Dictionary - {arg}",
		        description=def4.definition,
		        color=discord.Color.green())
		]

		paginator = BotEmbedPaginator(ctx, embeds)

		await paginator.run()

	except Exception:

		await ctx.send(f"Can't find **{arg}** in Urban Dictionary.")

@bot.command()
@commands.is_owner()
async def ay(ctx, *, msg: str):
	await ctx.send(msg)
	await ctx.message.delete()

@bot.command()
async def say(ctx, *, msg: str):
	await ctx.send(msg)

@bot.command()
@commands.is_owner()
async def connect(ctx, type=None):
	if type == "serv":
		ser = len(bot.guilds)
		await ctx.send(f'Am connected to {ser} servers')
	elif type == "user":
		user = len(bot.users)
		await ctx.send(f'Am connected to {user} users')
	elif type == None:
		embed = discord.Embed(title="CONNECTED")
		embed.color = discord.Color.blue()
		s = "Van connect serv"
		u = "Van connect user"
		embed.description = f"{s}\n{u}"
		await ctx.send(embed=embed)

@bot.command(aliases=['bot'])
@commands.is_owner()
async def reboot(ctx):
	await ctx.send('<a:fastdance3:712218698248880158> Restarting....')
	os.execv(sys.executable, [sys.executable] + sys.argv)

@bot.command(helpinfo='Searches for YouTube videos', aliases=['yt'])
@commands.cooldown(1, 4, commands.BucketType.user)
async def youtube(ctx, *, query: str):
	'''
    Uses YouTube Data v3 API to search for videos
    '''
	req = requests.get((
	    'https://www.googleapis.com/youtube/v3/search?part=id&maxResults=1'
	    '&order=relevance&q={}&relevanceLanguage=en&safeSearch=moderate&type=video'
	    '&videoDimension=2d&fields=items%2Fid%2FvideoId&key=').format(query) +
	                   os.environ['YOUTUBE_API_KEY'])
	await ctx.send('**Video URL: https://www.youtube.com/watch?v={}**'.format(
	    req.json()['items'][0]['id']['videoId']))

start_time = time.time()
bot.launch_time = datetime.datetime.utcnow()

@bot.command(aliases=['up', 'upt'])
@commands.is_owner()
async def uptime(ctx):
	delta_uptime = datetime.datetime.utcnow() - bot.launch_time
	hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)
	await ctx.send(
	    f"<a:d0n3:712988326390530090> I am online since <a:d0n3:712988326390530090> ```{days}d, {hours}h, {minutes}m, {seconds}s```"
	)

@bot.command(helpinfo='For when plain text just is not enough')
async def emojify(ctx, *, text: str):
	'''
    Converts the alphabet and spaces into emoji
    ''' ""
	author = ctx.message.author
	emojified = '⬇ Copy and paste this: ⬇\n'
	formatted = re.sub(r'[^A-Za-z ]+', "", text).lower()
	if text == '':
		await ctx.send('Remember to say what you want to convert!')
	else:
		for i in formatted:
			if i == ' ':
				emojified += '     '
			else:
				emojified += ':regional_indicator_{}: '.format(i)
		if len(emojified) + 2 >= 2000:
			await ctx.send('Your message in emojis exceeds 2000 characters!')
		if len(emojified) <= 25:
			await ctx.send('Your message could not be converted!')
		else:
			await author.send('`' + emojified + '`')

@bot.command(
    helpinfo='Shows MC account info, skin and username history',
    aliases=['skin', 'mc'])
async def minecraft(ctx, username='Van'):
	'''
   Shows MC account info, skin and username history
    '''
	uuid = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'.
	                    format(username)).json()['id']

	url = json.loads(
	    base64.b64decode(
	        requests.get(
	            'https://sessionserver.mojang.com/session/minecraft/profile/{}'
	            .format(uuid)).json()['properties'][0]['value']).decode(
	                'utf-8'))['textures']['SKIN']['url']

	names = requests.get(
	    'https://api.mojang.com/user/profiles/{}/names'.format(uuid)).json()
	history = "**Name History:**\n"
	for name in reversed(names):
		history += name['name'] + "\n"

	await ctx.send('**Username: `{}`**\n**Skin: {}**\n**UUID: {}**'.format(
	    username, url, uuid))

@client.command()
async def userroles(ctx, member: discord.Member = None):
	'''
  ➜  Give info about u roles
  '''
	if member == None:
		member = ctx.author
		roles = [role for role in member.roles]

		embed = discord.Embed(title=f"{member.name}'s roles", color=0x2f3136)
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(
		    name=f"Roles ({len(roles)})",
		    value=" ".join([role.mention for role in roles]))
		await ctx.send(embed=embed)
	else:
		roles = [role for role in member.roles]

		embed = discord.Embed(title=f"{member.name}'s roles", color=0x2f3136)
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(
		    name=f"Roles ({len(roles)})",
		    value=" ".join([role.mention for role in roles]))
		await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def roleinfo(ctx, *, role: discord.Role = None):
	"""➜  Info about a role"""
	if role == None:
		await ctx.send(":x: | Role not found")
	else:
		colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
		colour = int(colour, 16)
		embed = discord.Embed(
		    colour=discord.Colour(value=colour),
		    timestamp=datetime.datetime.utcnow())
		embed.add_field(name="Role Name", value=format(role.name))
		embed.add_field(name="Role ID", value=format(role.id))
		embed.add_field(name="For Guild", value=format(role.guild))
		embed.add_field(name="Hoist", value=format(role.hoist))
		embed.add_field(name="Role Position", value=format(role.position))
		embed.add_field(
		    name="Mentionable Role", value=format(role.mentionable))
		embed.add_field(name="Role Created At", value=format(role.created_at))
		await ctx.send(embed=embed)

keep_alive()
client.loop.create_task(statuschange())
client.run(os.environ.get("BABI"))