import asyncio
import discord
from discord.interactions import Interaction
from discord.ui import Button, View

from utils.settings import Settings

settings = Settings()

user = settings.get("Cases.Latest")

class selWarn(discord.ui.View):
    @discord.ui.select(
        placeholder = "Select a Warn!", 
        min_values = 1, 
        max_values = 1, 
        options = [
            discord.SelectOption(
                label=f"1 by {settings.get(f'Cases.{user}.WarnedBy.1')}",
                description=f"{settings.get(f'Cases.{user}.Warns.1')}"
            ),
            discord.SelectOption(
                label=f"2 by {settings.get(f'Cases.{user}.WarnedBy.2')}",
                description=f"{settings.get(f'Cases.{user}.Warns.2')}"
            ),
            discord.SelectOption(
                label=f"3 by {settings.get(f'Cases.{user}.WarnedBy.3')}",
                description=f"{settings.get(f'Cases.{user}.Warns.3')}"
            ),
            discord.SelectOption(
                label=f"4 by {settings.get(f'Cases.{user}.WarnedBy.4')}",
                description=f"{settings.get(f'Cases.{user}.Warns.4')}"
            ),
            discord.SelectOption(
                label=f"5 by {settings.get(f'Cases.{user}.WarnedBy.5')}",
                description=f"{settings.get(f'Cases.{user}.Warns.5')}"
            ),
            discord.SelectOption(
                label=f"6 by {settings.get(f'Cases.{user}.WarnedBy.6')}",
                description=f"{settings.get(f'Cases.{user}.Warns.6')}"
            ),
            discord.SelectOption(
                label=f"7 by {settings.get(f'Cases.{user}.WarnedBy.7')}",
                description=f"{settings.get(f'Cases.{user}.Warns.7')}"
            ),
            discord.SelectOption(
                label=f"8 by {settings.get(f'Cases.{user}.WarnedBy.8')}",
                description=f"{settings.get(f'Cases.{user}.Warns.8')}"
            ),
            discord.SelectOption(
                label=f"9 by {settings.get(f'Cases.{user}.WarnedBy.9')}",
                description=f"{settings.get(f'Cases.{user}.Warns.9')}"
            ),
            discord.SelectOption(
                label=f"10 by {settings.get(f'Cases.{user}.WarnedBy.10')}",
                description=f"{settings.get(f'Cases.{user}.Warns.10')}"
            ),
            discord.SelectOption(
                label=f"11 by {settings.get(f'Cases.{user}.WarnedBy.11')}",
                description=f"{settings.get(f'Cases.{user}.Warns.11')}"
            ),
            discord.SelectOption(
                label=f"12 by {settings.get(f'Cases.{user}.WarnedBy.12')}",
                description=f"{settings.get(f'Cases.{user}.Warns.12')}"
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        print("Hello World!")