import discord
import traceback
from discord.interactions import Interaction
import discord.guild
from discord.ui import View, Button
import os

class getWarnProofID(discord.ui.Modal):
    def __init__(self, bot, title="Get ", *args, **kwargs):
        self.bot = bot
        super().__init__(
            discord.ui.InputText(
                label="Id",
                placeholder="69 (Don't put the #.)",
                max_length=2,
                style=discord.InputTextStyle.short
            ),
            title=title,
            *args,
            **kwargs
        )

    async def callback(self, interaction: discord.Interaction):
        latestUserName = self.bot.settings.get(f"Cases.Latest")
        with open(f"images/proofs/warns/{latestUserName}_warn{self.children[0].value}".filename, "wb") as f:
            await f"images/proofs/warns/{latestUserName}_warn{self.children[0].value}".save(f)
        file_to_send = discord.File(f)


        try:
            await interaction.response.send_message(file=file_to_send, ephemeral=True)
        except:
            embed = discord.Embed(title="Error!", description=f"No warns have been found with the #{self.children[0].value} id.\n Try again.", color=discord.Color.red())
            await interaction.response.send_message(embed=embed, ephemeral=True)
            