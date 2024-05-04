import os
import discord
import inspect
import importlib
from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} is ready")
        await self.bot.change_presence(activity=discord.Streaming(name="MissingBuilder's Community", url='https://twitch.tv/missingbuilder', game="Discord"))
#        for filename in os.listdir("./views/buttons"):
#            if filename.endswith(".py"):
#                classes = [obj for name, obj in inspect.getmembers(importlib.import_module(f"views.buttons.{filename[:-3]}")) if inspect.isclass(obj) and issubclass(obj, discord.ui.View)]
#                for view in classes:
#                    print(f"Loaded {view.__name__}")

def setup(bot: commands.Bot):
    bot.add_cog(Ready(bot))