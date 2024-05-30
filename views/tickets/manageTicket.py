import asyncio
import discord
from discord.interactions import Interaction
from discord.ui import Button, View

from views.tickets.ticketDeleteCheck import uSure

class manageTicket(discord.ui.View):
    def __init__(self, bot) -> None:
        super().__init__(timeout=None)
        self.bot = bot
    
    @discord.ui.button(label="Close", style=discord.ButtonStyle.primary, custom_id="close_ticket", emoji="🔒")
    async def close_ticket_callback(
        self,
        button, 
        interaction: discord.Interaction
    ):
        role = interaction.guild.get_role(self.bot.settings.get('Tickets.Role'))
        if (role not in interaction.user.roles):
            await interaction.response.send_message("*Missing Permissions* :warning:", ephemeral=True)
            embed = discord.Embed(
                title="Error!",
                description="You do not have the required permissions to close this ticket.",
                color=discord.Color.red()
            )
            await asyncio.sleep(1)
            await interaction.edit_original_response(content=None, embed=embed)
            return
        if "closed-" in interaction.channel.name:
            embed = discord.Embed(
                title="Error!",
                description="This ticket has already been closed.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)

        else:
            embed = discord.Embed(
                title='Closing...',
                description=f'{interaction.channel.mention} is being closed...',
                color=discord.Color.yellow()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


            embed = discord.Embed(
                title='Ticket Closing',
                description='This ticket is closing.',
                color=discord.Color.yellow()
            )
            embed.set_author(
                name=interaction.user.display_name,
                icon_url=interaction.user.avatar.url,
                url=interaction.user.jump_url
            )
            embed.set_footer(
                text=f'requested by {interaction.user.display_name}',
                icon_url=interaction.user.avatar.url
            )
            msg = await interaction.channel.send(embed=embed)
            category = interaction.guild.get_channel(self.bot.settings.get("Tickets.Closed"))
            await interaction.channel.edit(name=f"closed-{interaction.channel.name}", category=category, sync_permissions=True)

            embed = discord.Embed(
                title='Closed!',
                color=discord.Color.green()
            )
            await msg.delete()
            await interaction.channel.send(embed=embed)

            embed = discord.Embed(
                title='Successfully Closed!',
                description=f'{interaction.channel.mention} has been successfully closed.',
                color=discord.Color.green()
            )
            await interaction.edit_original_response(embed=embed)
            if (self.bot.settings.get('Log.Channel') is not None):
                log = self.bot.get_channel(self.bot.settings.get('Log.Channel'))
                embed = discord.Embed(
                    title=f"Closed Ticket",
                    description=f"{interaction.user.mention} closed the {interaction.channel.name} ticket",
                    color=discord.Color.blurple()
                )
                await log.send(embed=embed)


    @discord.ui.button(label="Delete", style=discord.ButtonStyle.primary, custom_id="del_ticket", emoji="🗑️")
    async def del_ticket_callback(
        self,
        button, 
        interaction: discord.Interaction
    ):
        role = interaction.guild.get_role(self.bot.settings.get('Tickets.Role'))
        if (role not in interaction.user.roles):
            await interaction.response.send_message("*Missing Permissions* :warning:", ephemeral=True)
            embed = discord.Embed(
                title="Error!",
                description="You do not have the required permissions to close this ticket.",
                color=discord.Color.red()
            )
            await asyncio.sleep(1)
            await interaction.edit_original_response(content=None, embed=embed)
            return
        else:
            if "closed-" in interaction.channel.name:
                embed = discord.Embed(
                    title="Are you sure?",
                    description=
                    f"""
                    Do you really want to delete [this ticket]({interaction.channel.jump_url}) ({interaction.channel.mention})\n
                    To cancel, ignore this\n
                    To proceed click on "Yes"
                    """,
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed, view=uSure(bot=self.bot), ephemeral=True)

            else:
                embed = discord.Embed(
                    title="Error!",
                    description="You need to close the ticket before being able to delete it.",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)