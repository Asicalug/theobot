import os
import discord
import inspect
import importlib
from discord.ext import commands

from views.tickets.selector import Selector
from views.tickets.manageTicket import manageTicket
from views.tickets.ticketDeleteCheck import uSure

class Ready(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} is ready")
        await self.bot.change_presence(activity=discord.Streaming(name="with no-delays.", url='https://twitch.tv/missingbuilder', game="Discord"))
        self.bot.add_view(Selector(bot=self.bot))
        self.bot.add_view(manageTicket(bot=self.bot))
        self.bot.add_view(uSure(bot=self.bot))




def setup(bot: commands.Bot):
    bot.add_cog(Ready(bot))
