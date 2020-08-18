import discord
from discord.ext import commands
import canvas as Painter
import aiohttp
import os
import deku as myself
from deku import *
import json
import random

ksoft_token = os.environ.get("KSOFT_TOKEN")

class Ksoft(commands.Cog):
  
  def __init__(self, bot):
    
    self.bot = bot

  @commands.command()
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def dog(self, ctx):

    async with aiohttp.ClientSession() as s:

      async with s.get("https://api.ksoft.si/images/random-image", params = {"tag": "dog"}, headers = {"Authorization": f"Bearer {ksoft_token}"}) as resp:

        data = await resp.json()

    embed = discord.Embed()

    embed.set_image(url = data["url"])

    embed.description = "Here's some cute dog owo"

    await ctx.send(file=discord.File(Painter.urltoimage(url = data["url"]), 'ea.png'))

  @commands.command()
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def cat(self, ctx):

    async with aiohttp.ClientSession() as s:

      async with s.get("https://api.ksoft.si/images/random-image", params = {"tag": "cat"}, headers = {"Authorization": f"Bearer {ksoft_token}"}) as resp:

        data = await resp.json()

    embed = discord.Embed()

    embed.description = "Here's some cute cat owo"

    embed.set_image(url = data["url"])

    await ctx.send(file=discord.File(Painter.urltoimage(url = data["url"]), 'bapakmugans.png'))

  @commands.command(name = "locate-ip")
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def locateip(self, ctx, *, place = None, args):
    if len(args)==0:
      await ctx.send("Please input the IP!")

    if place == None:

      embed = discord.Embed()

      embed.title = "Hmm Invalid argument"

      embed.description = "**Try with ```Todo.locate-ip [ip address]```**"

      embed.color = discord.Color.red()

      return await ctx.send(embed = embed)

    async with aiohttp.ClientSession() as s:

      async with s.get("https://api.ksoft.si/kumo/geoip", params = {"ip": place}, headers = {"Authorization": f"Bearer {ksoft_token}"}) as resp:

        data = await resp.json()

    embed = discord.Embed()

    embed.title = place

    embed.add_field(name = "City", value = data["data"]["city"], inline = False)

    embed.add_field(name = "Continent", value = data["data"]["continent_name"], inline = False)

    embed.add_field(name = "Country", value = data["data"]["country_name"], inline = False)

    embed.add_field(name = "Time-zone", value = data["data"]["time_zone"], inline = False)

    embed.add_field(name = "Postal Code", value = data["data"]["postal_code"], inline = False)

    embed.add_field(name = "Longitude", value = data["data"]["longitude"], inline = False)

    embed.add_field(name = "Latitude", value = data["data"]["latitude"], inline = False)

    embed.timestamp = ctx.message.created_at

    await ctx.send(embed = embed)

  @commands.command()
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def locate(self, ctx, *, place = None):

    if place == None:

      embed = discord.Embed()

      embed.title = " Invalid argument"

      embed.description = "**Todo.locate [place]**"

      embed.color = discord.Color.red()

      return await ctx.send(embed = embed)

    async with aiohttp.ClientSession() as session:

      async with session.get("https://api.ksoft.si/kumo/gis", params = {"q": place, "include_map": "true"}, headers = {"Authorization": f"Bearer {ksoft_token}"}) as resp:

        data = await resp.json()

    embed = discord.Embed()

    embed.title = data["data"]["address"]

    embed.url = data["data"]["map"]

    embed.set_image(url = data["data"]["map"])

    embed.add_field(name = "Latitude", value = data["data"]["lat"])

    embed.add_field(name = "Longitude", value = data["data"]["lon"])

    await ctx.send(embed = embed)

  @commands.command(name = "nsfw-gif")
  @commands.cooldown(1, 6, commands.BucketType.user)
  @commands.is_nsfw()
  async def nsfwgif(self, ctx):

    async with aiohttp.ClientSession() as session:

      async with session.get("https://api.ksoft.si/images/random-nsfw", params = {"gifs": "true"}, headers = {"Authorization": f"Bearer {ksoft_token}"}) as resp:

        data = await resp.json()

    embed = discord.Embed()

    embed.description = "[{}]({})".format(data["title"], data["image_url"])

    embed.set_image(url = data["image_url"])

    await ctx.send(file=discord.File(Painter.urltoimage(url = data["image_url"]), 'dosabego.png'))

  @commands.command()
  @commands.cooldown(1, 6, commands.BucketType.user)
  @commands.is_nsfw()
  async def nsfw(self, ctx):

    async with aiohttp.ClientSession() as session:

      async with session.get("https://api.ksoft.si/images/random-nsfw", headers = {"Authorization": f"Bearer {ksoft_token}"}) as resp:

        data = await resp.json()

    embed = discord.Embed()

    embed.description = "[{}]({})".format(data["title"], data["image_url"])

    embed.set_image(url = data["image_url"])

    await ctx.send(file=discord.File(Painter.urltoimage(url = data["image_url"]), 'dosatolol.png'))
  
  @commands.command()
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def topsecretloli(self, ctx):

    async with aiohttp.ClientSession() as session:

      async with session.get("https://api.ksoft.si/images/rand-reddit/lolirefugees", params = {"remove_nsfw": "true", "span": "week"}, headers = {"Authorization": f"Bearer {ksoft_token}"}) as resp:

        data = await resp.json()

    await ctx.send("Note: r/lolirefugees' posts are SFW.")

    embed = discord.Embed()

    embed.description = "[{}]({})".format(data["title"], data["image_url"])

    embed.set_image(url = data["image_url"])

    await ctx.send(file=discord.File(Painter.urltoimage(url = data["image_url"]), 'lolisayang.png'))
  @commands.command(aliases=["findly"])
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def findlyrics(self, ctx, *, arg = None):

    x = "😕"

    if arg == None:

      embed = discord.Embed()

      embed.title = "{} Invalid argument".format(x)

      embed.description = "**Todo.findlyrics [song name]**"

      embed.color = discord.Color.red()

      return await ctx.send(embed = embed)

    async with aiohttp.ClientSession() as session:

      async with session.get("https://api.ksoft.si/lyrics/search", params = {"q": arg, "limit": 1}, headers = {"Authorization": f"Bearer {ksoft_token}"}) as resp:

        data = await resp.json()

    for datas in data["data"]:

      full = len(datas["lyrics"])

      try:

        return await ctx.send(datas["lyrics"])

      except discord.HTTPException:

        msg = "```"

        msg += "{}".format(datas["lyrics"][:1999])

        msg += "```"

        await ctx.author.send(datas["lyrics"][2000:full])

        return await ctx.send(f"```**{msg}**```")
  
  @commands.command()
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def lolicon(self, ctx):

    async with aiohttp.ClientSession() as s:

      async with s.get("https://api.ksoft.si/images/random-image", params = {"tag": "loli"}, headers = {"Authorization": f"Bearer {ksoft_token}"}) as resp:

        data = await resp.json()

    embed = discord.Embed()

    embed.description = "Here's some loli owo"

    embed.set_image(url = data["url"])

    await ctx.send(embed = embed)
  
  @commands.command()
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def neko(self, ctx):
    
    if ctx.channel.is_nsfw() == True:
    
      async with aiohttp.ClientSession() as session:
      
        async with session.get('https://api.ksoft.si/images/random-image', params = {"tag": "neko", "nsfw": "true"}, headers={"Authorization": f"Bearer {ksoft_token}"}) as resp:
        
          data = await resp.json()
    
      embed = discord.Embed()
    
      embed.set_image(url = data["url"])
    
      embed.description = "Tag: [{}]({})".format(data["tag"], data["url"])
    
      await ctx.send(embed = embed)
      
    else:
      
      async with aiohttp.ClientSession() as session:
      
        async with session.get('https://api.ksoft.si/images/random-image', params = {"tag": "neko", "nsfw": "false"}, headers={"Authorization": f"Bearer {ksoft_token}"}) as resp:
        
          data = await resp.json()

      if data["nsfw"] == True:

        return await ctx.send("The post was NSFW, please run the command again.")
    
      embed = discord.Embed()
    
      embed.set_image(url = data["url"])
    
      embed.description = "Tag: [{}]({})".format(data["tag"], data["url"])
    
      await ctx.send(embed = embed)
      
  @commands.command()
  @commands.cooldown(1, 6, commands.BucketType.user)
  @commands.is_nsfw()
  async def hentai(self, ctx):
    
    randomNSFW = "hentai_gif"
    
    async with aiohttp.ClientSession() as session:
      
      async with session.get('https://api.ksoft.si/images/random-image', params = {"tag": randomNSFW, "nsfw": "true"}, headers={"Authorization": f"Bearer {ksoft_token}"}) as resp:
        
        data = await resp.json()
        
    embed = discord.Embed()
    
    embed.set_image(url = data["url"])
    
    embed.description = "Tag: [{}]({})".format(data["tag"], data["url"])
    
    await ctx.send(embed = embed)
  
  @commands.command()
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def reddit(self, ctx, *, arg = None):
    
    x = "🙂"

    if arg == None:

      embed = discord.Embed()

      embed.title = "{} Invalid argument".format(x)

      embed.description = "**Todo.reddit [subreddit]**"

      embed.color = discord.Color.red()

      return await ctx.send(embed = embed)
    
    async with aiohttp.ClientSession() as session:
      
      async with session.get('https://api.ksoft.si/images/rand-reddit/{}'.format(arg), params = {"remove_nsfw": "false", "span": "week"}, headers={"Authorization": f"Bearer {ksoft_token}"}) as resp:
        
        data = await resp.json()

    try:

      if data["nsfw"] == True:

        if not ctx.channel.is_nsfw() == True:

          return await ctx.send("Seems like the post is NSFW related but the channel isn't, try running the command again in an NSFW channel.")
    
      embed = discord.Embed()
    
      embed.description = "[{}]({})".format(data["title"], data["image_url"])
    
      embed.set_image(url = data["image_url"])
    
      embed.set_footer(text = "Author: {}".format(data["author"]))
    
      await ctx.send(embed = embed)

    except KeyError:

      await ctx.send("There's something wrong with the result, try again later.")
    
  @commands.command()
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def meme(self, ctx):
    
    async with aiohttp.ClientSession() as session:
      
      async with session.get('https://api.ksoft.si/images/random-meme', headers={"Authorization": f"Bearer {ksoft_token}"}) as resp:
        
        data = await resp.json()
        
    embed = discord.Embed()
    
    embed.set_image(url = data["image_url"])
    
    embed.description = "[{}]({})".format(data["title"], data["image_url"])
    
    embed.set_footer(text = "Author: {} | Subreddit: {}".format(data["author"], data["subreddit"]))
    
    await ctx.send(embed = embed)
    
def setup(bot):
  
  bot.add_cog(Ksoft(bot))