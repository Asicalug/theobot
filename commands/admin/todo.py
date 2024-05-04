import discord
from discord.ext import commands
from discord.commands import Option


class Todo(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    @commands.slash_command(name="todo", description="Prints out the todo list")
    @commands.has_permissions(administrator=True)
    async def todo(
        self,
        ctx: discord.ApplicationContext
    ):
        embed = discord.Embed(
            title='Todo List',
            description=
            """
Warning system with proof - and 3 warnings = 1h timeout -> 6 warnings = 1d timeout -> 12 Warnings = Ban 🟡
Economy system - Work, Daily, Weekly, Beg, Slots, etc 🔴
Steal emojis command 🔴
Ban Command with Proof 🟡
Unban 🔴
Unwarn 🔴
dead chat ping 🔴
Case Info - Information about warn cases, ban cases, etc 🟡
Punishment History 🔴
            """,
            color=discord.Color.orange()
        )
        user = self.bot.get_user(self.bot.settings.get('Cases.Latest'))
        await ctx.respond(user.avatar.url, embed=embed, ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Todo(bot))