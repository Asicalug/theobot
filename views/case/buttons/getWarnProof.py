import asyncio
import discord
from discord.interactions import Interaction
from discord.ui import Button, View

from views.case.modals.getWarnProofID import getWarnProofID

class getWarnProof(discord.ui.View):
    def __init__(self, bot) -> None:
        super().__init__(timeout=None)
        self.bot = bot
    
    @discord.ui.button(label="Get Proof", style=discord.ButtonStyle.primary, custom_id="get_proof", emoji="🔍")
    async def get_proof_callback(
        self,
        button, 
        interaction: discord.Interaction
    ):
        await interaction.response.send_modal(getWarnProofID(bot=self.bot))