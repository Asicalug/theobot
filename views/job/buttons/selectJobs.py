import asyncio
import discord
from discord.interactions import Interaction
from discord.ui import Button, View

from views.case.modals.getWarnProofID import getWarnProofID

class SelectJob(discord.ui.View):
    def __init__(self, bot: discord.Bot) -> None:
        super().__init__(timeout=None)
        self.bot = bot
    
    @discord.ui.button(label="Starbucks", style=discord.ButtonStyle.primary, custom_id="get_starbucksJob", emoji=discord.PartialEmoji(name="starbucks", id=1238425796717318154))
    async def get_proof_callback(
        self,
        button, 
        interaction: discord.Interaction
    ):
        try:
            self.bot.settings.set(f'Jobs.{interaction.user.name}.Current', "starbucks")
        except Exception as e:
            embed = discord.Embed(title="Error!", description=f"Report this to <@1080643375960707092> and send a screenshot.\n`{e}`")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        embed = discord.Embed(title="Hired!", description="You're now a `starbucks employee`.")
        await interaction.response.send_message(embed=embed, ephemeral=True)