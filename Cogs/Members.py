import discord
from discord.ext import commands


class MembersCog(commands.Cog, name='Members'):

    def __init__(self, bot):
        self.bot = bot
    
      
    @commands.command(name='joined')
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member = None):
        """Check when the mentioned member joined the server."""

        if member is None:
            member = ctx.author

        await ctx.send(f'{member.display_name} joined the {member.joined_at.strftime("%dth of %B %Y")}')
        
    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member = None):
        """Check the mentioned member's top role in this server."""

        if member is None:
            member = ctx.author

        await ctx.send(f'{member.display_name} top role is {member.top_role.name}')

def setup(bot):
    bot.add_cog(MembersCog(bot))