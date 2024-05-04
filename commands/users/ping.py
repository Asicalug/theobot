import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")
	
    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="Pong!", description=f'My current latency is at {round(self.bot.latency * 1000, 2)}ms', color=discord.Color.blurple())
        output = await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Ping(bot))