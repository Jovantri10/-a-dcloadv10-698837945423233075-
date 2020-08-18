import discord
from discord.ext import commands

import json

class Warn(commands.Cog):

  def __init__(self, bot):

    self.bot = bot

  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def clearwarn(self, ctx, user: discord.Member = None):

    x = ""

    if user == None:

      embed = discord.Embed()

      embed.description = "**Py!clearwarn <@user>**"

      embed.title = "{} Invalid argument".format(x)

      embed.color = discord.Color.red()

      return await ctx.send(embed = embed)

    file = open("warns.json", "r")

    warn = json.load(file)

    if not str(ctx.guild.id) in warn:

      return await ctx.send("There are no warnings in this server.")

    if not str(user.id) in warn[str(ctx.guild.id)]:

      return await ctx.send("User doesn't have any warnings.")

    warnings = warn[str(ctx.guild.id)][str(user.id)]["warns"]

    warn[str(ctx.guild.id)].pop(str(user.id))

    dumps = open("warns.json", "w")

    json.dump(warn, dumps, indent = 4)

    embed = discord.Embed()

    embed.description = "⏩Cleared {} warnings for {}.".format(len(warnings), user.mention)

    embed.color = discord.Color.green()

    await ctx.send(embed = embed)

  @commands.command(aliases = ["warnings"])
  @commands.has_permissions(manage_messages = True)
  async def warns(self, ctx, user: discord.Member = None):

    file = open("warns.json", "r")

    warn = json.load(file)

    if not str(ctx.guild.id) in warn:

      return await ctx.send("There are no warnings in this server.")

    if user == None:

      msg = "```"

      msg += "Warning(s) for: {}".format(ctx.guild.name)

      for user in warn[str(ctx.guild.id)]:

        fetched_user = await self.bot.fetch_user(user)

        warns = warn[str(ctx.guild.id)][str(fetched_user.id)]["warns"]

        msg += "\n\n{}\n\n- ".format(fetched_user)
        
        msg += "\n- ".join([warn for warn in warns])

      msg += "```"

      await ctx.send(msg)

    else:

      fetched_user = await self.bot.fetch_user(user.id)

      if not str(fetched_user.id) in warn[str(ctx.guild.id)]:

        return await ctx.send("User doesn't have any warnings.")

      msg = "```"

      msg += "Warning(s) for: {}\n\n- ".format(fetched_user)

      msg += "\n- ".join([warns for warns in warn[str(ctx.guild.id)][str(fetched_user.id)]["warns"]])

      msg += "```"

      await ctx.send(msg)

  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def warn(self, ctx, user: discord.Member = None, *, reason = None):

    x = ""

    embed = discord.Embed()

    embed.title = "{} Invalid argument".format(x)

    embed.description = "**Py!warn <@user> <reason>**"

    embed.color = discord.Color.red()

    channel = discord.utils.get(ctx.guild.channels, name = "mod-logs-python")

    if channel == None:

      return await ctx.send("Please make new channel with name `mod-logs-python`.")

    if user == None:

      return await ctx.send(embed = embed)

    if reason == None:

      return await ctx.send(embed = embed)

    file = open("warns.json", "r")

    warn = json.load(file)

    if not str(ctx.guild.id) in warn:

      warn[str(ctx.guild.id)] = {}

    if not str(user.id) in warn[str(ctx.guild.id)]:

      warn[str(ctx.guild.id)][str(user.id)] = {}

      warn[str(ctx.guild.id)][str(user.id)]["warns"] = []

    warn[str(ctx.guild.id)][str(user.id)]["warns"].append(reason)

    dumps = open("warns.json", "w")

    json.dump(warn, dumps, indent = 4)

    done = discord.Embed()

    done.description = "✔ Warned {}.".format(user.mention)

    done.color = discord.Color.green()

    log = discord.Embed()

    log.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

    log.description = "Used `warn` command in {}\nPy!warn {} {}".format(ctx.channel.mention, user.mention, reason)

    log.color = discord.Color.blue()

    log.timestamp = ctx.message.created_at

    await ctx.send(embed = done)

    await channel.send(embed = log)

    await ctx.message.delete()

def setup(bot):

  bot.add_cog(Warn(bot))