import discord, ast, sys
from discord.ext.commands import command, Cog
from discord import Embed, Colour
from discord.ext import commands

def insert_returns(body):
		
		if isinstance(body[-1], ast.Expr):
			body[-1] = ast.Return(body[-1].value)
			ast.fix_missing_locations(body[-1])
			
		if isinstance(body[-1], ast.If):
			insert_returns(body[-1].body)
			insert_returns(body[-1].orelse)
			
		if isinstance(body[-1], ast.With):
			insert_returns(body[-1].body)

class Owner(Cog):
	
	def __init__(self, bot):
		
		self.bot = bot
		
	@Cog.listener()
	async def on_ready(self):
		
		print("Owner command loaded.")
		
	@command(name = 'cog', hidden = True)
	async def command_manage(self, ctx, type = None, *, commands = None):
		
		if ctx.author.id != self.bot.owner_id:
			
			return await ctx.send('{} Fak, you are not owner'.format(ctx.author.mention))
			
		if type == 'load':
			
			self.bot.load_extension(f'sourcenyaqaqa.{commands}')
			await ctx.send("Uwu")
			#await ctx.message.add_reaction('👍')
			
		elif type == 'unload':
			
			self.bot.unload_extension(f'sourcenyaqaqa.{commands}')
			await ctx.send("Uwu")
			#await ctx.message.add_reaction('👍')
			
		elif type == 'reload':
			
			self.bot.reload_extension(f'sourcenyaqaqa.{commands}')
			await ctx.send("Uwu")
			#await ctx.message.add_reaction('👍')
			
	@command(name = 'eval', hidden = True, aliases = ['e'])
	@commands.is_owner()
	async def eval_fn(self, ctx, *, command):
		fn_name = "_eval_expr"
		
		cmd = command.strip("` ")
		
		cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
		
		body = f"async def {fn_name}():\n{cmd}"
		
		parsed = ast.parse(body)
		
		body = parsed.body[0].body
		
		insert_returns(body)
		
		env = {
			'bot': ctx.bot,
			'discord': discord,
			'commands': commands,
			'ctx': ctx,
			'send': ctx.send,
			'author': ctx.author,
			'guild': ctx.guild,
			'get': discord.utils.get,
			'__import__': __import__
		}
		
		exec(compile(parsed, filename="<ast>", mode="exec"), env)
		
		result = (await eval(f"{fn_name}()", env))
		
		embed = Embed(
		  colour = Colour.from_rgb(255, 255, 0)
			)
		#f = [
			#("Code Blok", f"```{command}```", False),
		#	("Console Log", f"*```{result} ```*", False)
		#	]
			
	#	for name, value, inline in f:
			
		#	embed.set_author(icon_url=self.bot.user.avatar_url, name="S u c c e s")
		#	embed.add_field(name=name, value=value, inline=inline)
			
		await ctx.send(f"***OUTPUT***\n***```{result}```***\n⏳ {self.bot.latency} s")
		await ctx.message.add_reaction("<a:alpaisonlen:744891229137010750>")
		
	@eval_fn.error
	async def eval_fn_error(self, ctx, error):
		
		if isinstance(error, commands.CommandInvokeError):
			
			#embed = Embed(colour = Colour.red())
			#f = [
				#("Output", f"```{error}```", False)
				#]
			#for name, value, inline in f:
				
				#embed.set_author(icon_url=self.bot.user.avatar_url, name=self.bot.user.name)
				#embed.add_field(name=name, value=value, inline=inline)
		  o = discord.Embed(title="There is error!", description=f"***```{error}```***", color=0x2f3136)
		  await ctx.send(embed=o)
		  await ctx.message.add_reaction("<a:alpaiswarning:744891281397776454>")
		elif isinstance(error, commands.NotOwner):
		  await ctx.send("{} Nonono bish, pls leave, dont try it again".format(ctx.author.mention))
	  #else: return
		
def setup(bot):
	
	bot.add_cog(Owner(bot))