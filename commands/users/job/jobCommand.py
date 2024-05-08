import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup

from views.job.selector.selectJob import SelectJob

class Job(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    job = SlashCommandGroup(name="job", description="Multiple commands that will make the job system work")

    @job.command(name="select", description="Select the job that you want to do")
    async def jobSelect(
        self,
        ctx: discord.ApplicationContext
    ):
        try:
            currentJob = f"working as a `{self.bot.settings.get(f'Jobs.{ctx.user.name}.Current')}`"
        except:
            currentJob = "`Unemployed`"

        embed = discord.Embed(title="Get a Job", description=f"You're currently {currentJob}", color=discord.Color.blurple())
        await ctx.response.send_message(embed=embed, view=SelectJob(bot=self.bot), ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Job(bot))
        