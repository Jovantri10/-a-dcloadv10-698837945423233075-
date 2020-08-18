import discord
from discord.ext import commands
import paginator
from disputils import BotEmbedPaginator
from discord import Embed
import random

lala = [0x1abc9c, 0x9b59b6, 0x99aab5, 0x7289da, 0xa84300, 0xf1c40f, 0xe91e63, 0x546e7a]

class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.bot.remove_command('help')
		
	@commands.command(aliases=["help"])
	@commands.is_owner()
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def yel(ctx, *commands : str):
	  bot = ctx.bot
    destination = ctx.message.author if bot.pm_help else ctx.message.channel

    def repl(obj):
        return _mentions_transforms.get(obj.group(0), '')

    # help by itself just lists our own commands.
    if len(commands) == 0:
        pages = bot.formatter.format_help_for(ctx, bot)
    elif len(commands) == 1:
        # try to see if it is a cog name
        name = _mention_pattern.sub(repl, commands[0])
        command = None
        if name in bot.cogs:
            command = bot.cogs[name]
        else:
            command = bot.commands.get(name)
            if command is None:
                yield from bot.send_message(destination, bot.command_not_found.format(name))
                return

        pages = bot.formatter.format_help_for(ctx, command)
    else:
        name = _mention_pattern.sub(repl, commands[0])
        command = bot.commands.get(name)
        if command is None:
            yield from bot.send_message(destination, bot.command_not_found.format(name))
            return

        for key in commands[1:]:
            try:
                key = _mention_pattern.sub(repl, key)
                command = command.commands.get(key)
                if command is None:
                    yield from bot.send_message(destination, bot.command_not_found.format(key))
                    return
            except AttributeError:
                yield from bot.send_message(destination, bot.command_has_no_subcommands.format(command, key))
                return

        pages = bot.formatter.format_help_for(ctx, command)

    if bot.pm_help is None:
        characters = sum(map(lambda l: len(l), pages))
        # modify destination based on length of pages.
        if characters > 1000:
            destination = ctx.message.author

    for page in pages:
        yield from bot.send_message(destination, page)


def setup(bot):
	bot.add_cog(Help(bot))