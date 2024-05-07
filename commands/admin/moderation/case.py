import discord
from discord.ext import commands, pages
from discord.commands import Option
from discord.ext.pages import Paginator, Page
import asyncio

from views.case.buttons.getWarnProof import getWarnProof

warns = []
mods = []
users = []
warnIds = []

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
        self.bot.settings.set(f"Cases.Latest", user.name)

        if self.bot.settings.get(f"Cases.{user.name}.Warns") != None:
            for i in range(wAmount+1):
                if i == 0:
                    pass
                else:
                    warns.append(self.bot.settings.get(f'Cases.{user.name}.Warns.{i}'))
                    mods.append(self.bot.settings.get(f'Cases.{user.name}.WarnedBy.{i}'))
                    users.append(user.mention)
                    warnIds.append(f"#{i}")
        

        if user.id == 779442220104417280:
            avatarUrl = "https://cdn.discordapp.com/attachments/1231780683966582885/1236591328201015366/image.png?ex=663890eb&is=66373f6b&hm=538541765b9cd580515a7beccc6aab63798b12efc3e3e33b06196723261dfe7d&"
            description = "As you can see on the thumbnail, omairr **clearly** stated that he likes men which ultimately mean that he's gay."
            image1Url = "https://cdn.discordapp.com/attachments/1231780683966582885/1236591328201015366/image.png?ex=663890eb&is=66373f6b&hm=538541765b9cd580515a7beccc6aab63798b12efc3e3e33b06196723261dfe7d&"
            image2Url = "https://cdn.discordapp.com/attachments/1111425481238134784/1236695301591531520/image.png?ex=6638f1c0&is=6637a040&hm=8d20d609dd9ff1352c65a55a15afb29f970e4366898c1d9085f078ff0dc2135a&"
        else:
            avatarUrl = user.avatar.url
            description = ""
            image1Url = None
            image2Url = None

        joinedWarns = "\n".join(warns)
        joinedMods = "\n".join(mods)
        joinedUsers = "\n".join(users)
        joinedIds = "\n".join(warnIds)

        print(len(warns))
        if len(warns) == 1 or 0:
            s = ""
        else:
            s = "s"
        self.pages = [
            Page(
                embeds=[
                    discord.Embed(title=f"{user.name}'s Current Warn{s}", description=f"{description}", color=discord.Color.yellow()).set_thumbnail(url=avatarUrl).set_image(url=image1Url).add_field(name="User", value=joinedUsers).add_field(name="Moderator", value=joinedMods).add_field(name="Reason", value=joinedWarns).add_field(name=f"ID{s}", value=joinedIds),
                ],
            ),
            Page(
                embeds=[
                    discord.Embed(title=f"{user.name}'s Current Mute{s}", description=f"{description}", color=discord.Color.yellow()).set_thumbnail(url=avatarUrl).set_image(url=image2Url)
                ]
            )
        ]
        paginator = pages.Paginator(pages=self.get_pages(), custom_view=getWarnProof(bot=self.bot))

        await paginator.respond(ctx.interaction, ephemeral=True)
        warns.clear()
        mods.clear()
        users.clear()
        warnIds.clear()


def setup(bot: commands.Bot):
    bot.add_cog(Case(bot))