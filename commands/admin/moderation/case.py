import discord
from discord.ext import commands, pages
from discord.commands import Option
from discord.ext.pages import Paginator, Page
import asyncio

from bot import reloadcog

warns = []

class Case(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def get_pages(self):
        return self.pages
        #print(f"{self.__class__.__name__} loaded")

    @commands.slash_command(name="case", description='Gets the case of the user')
    @commands.has_permissions(moderate_members=True)
    async def case(
        self,
        ctx: discord.ApplicationContext,
        user: Option(discord.User, description="The user that you want to get the case info from") # type: ignore
    ): 
        wAmount = self.bot.settings.get(f"Cases.{user.name}.WarnAmount")

        if self.bot.settings.get(f"Cases.{user.name}.Warns") != None:
            for i in range(wAmount+1):
                if i == 0:
                    pass
                else:
                    warns.append(self.bot.settings.get(f'Cases.{user.name}.Warns.{i}'))
        

        if user.id == 779442220104417280:
            avatarUrl = "https://cdn.discordapp.com/attachments/1231780670146088970/1235661318569197590/image.png?ex=6637d1c7&is=66368047&hm=e96f59ee4df743e2cd9b60cc3d24142da8d52bf229c595a92d817b56f673d4be&"
        else:
            avatarUrl = user.avatar.url

        self.pages = [
            Page(
                embeds=[
                    discord.Embed(title="Current Warns", description=f"Test\n {warns}").set_thumbnail(url=avatarUrl),
                ],
            ),
        ]
        paginator = pages.Paginator(pages=self.get_pages())

        await paginator.respond(ctx.interaction, ephemeral=True)
        warns.clear()


def setup(bot: commands.Bot):
    bot.add_cog(Case(bot))