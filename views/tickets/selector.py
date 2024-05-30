import discord
from utils.calculate.calculateTicketNum import calcTicketNum

from views.tickets.manageTicket import manageTicket

class Selector(discord.ui.View):
    def __init__(self, bot: discord.Bot) -> None:
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        custom_id="ticket_selector",
        placeholder = "Ticket Category", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Staff",
                emoji="<:raccoonhuh:1243215937407160470>",
                description="The main staff team will help you"
            ),
            discord.SelectOption(
                label="Admin",
                emoji="<:raccoonthink:1243215971997450280>",
                description="The admin team will help you"
            ),
            discord.SelectOption(
                label="Management",
                emoji="<:raccoonsilly:1243215943841218611>",
                description="The management team will help you"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "Staff":
            embed = discord.Embed(
                title="Creating your ticket...",
                description="Please be patient as we are working to create your ticket.",
                color=discord.Color.yellow()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True),
                interaction.user: discord.PermissionOverwrite(view_channel=True), 
                interaction.guild.get_role(self.bot.settings.get('Tickets.Role')): discord.PermissionOverwrite(view_channel=True)
            }
            if self.bot.settings.get('Tickets.Count') is None:
                self.bot.settings.set('Tickets.Count', 0)


            current = self.bot.settings.get('Tickets.Count')
            ticketNum = calcTicketNum(current=current)

            category = discord.utils.get(
                interaction.guild.categories,
                id=self.bot.settings.get("Tickets.Tickets")
            )

            self.bot.settings.set("Tickets.Count", ticketNum)

            channel = await interaction.guild.create_text_channel(
                name=f"staff-{interaction.user.name}-{ticketNum}",
                category=category,
                overwrites=overwrites
            )

            embed = discord.Embed(
                title="Welcome!",
                description=
                f"""
                Welcome {interaction.user.mention}.\n
                Please describe the reason for the creation of this ticket below.\n
                Remember, do **NOT** ping any staff members in this ticket.
                """,
                color=discord.Color.blurple()
            )
            embed.set_footer(text="Sincerely, the CrackedNetwork team.")
            msg = await channel.send(
                content=interaction.user.mention,
                embed=embed,
                view=manageTicket(bot=self.bot)
            )
            await msg.pin(reason="First message in ticket")
            await channel.purge(limit=1, reason="ugly message")

            embed = discord.Embed(
                title="Ticket Created!",
                description=
                f"""
                Your ticket has been created.
                Please access it [here]({channel.jump_url}) ({channel.mention})
                """,
                color=discord.Color.green()
            )
            await interaction.edit_original_response(embed=embed)

            if (self.bot.settings.get('Log.Channel') is not None):
                log = self.bot.get_channel(self.bot.settings.get('Log.Channel'))
                embed = discord.Embed(
                    title=f"New Ticket",
                    description=f"{interaction.user.mention} created a [ticket]({channel.jump_url}) ({channel.mention})",
                    color=discord.Color.blurple()
                )
                embed.set_author(
                    name=interaction.user.display_name,
                    icon_url=interaction.user.avatar.url,
                    url=interaction.user.jump_url
                )
                await log.send(embed=embed)
        if select.values[0] == "Admin":
            embed = discord.Embed(
                title="Creating your ticket...",
                description="Please be patient as we are working to create your ticket.",
                color=discord.Color.yellow()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True),
                interaction.user: discord.PermissionOverwrite(view_channel=True), 
                interaction.guild.get_role(self.bot.settings.get('Tickets.Role')): discord.PermissionOverwrite(view_channel=True)
            }
            if self.bot.settings.get('Tickets.Count') is None:
                self.bot.settings.set('Tickets.Count', 0)


            current = self.bot.settings.get('Tickets.Count')
            ticketNum = calcTicketNum(current=current)

            category = discord.utils.get(
                interaction.guild.categories,
                id=self.bot.settings.get("Tickets.Tickets")
            )

            self.bot.settings.set("Tickets.Count", ticketNum)

            channel = await interaction.guild.create_text_channel(
                name=f"Admin-{interaction.user.name}-{ticketNum}",
                category=category,
                overwrites=overwrites
            )

            embed = discord.Embed(
                title="Welcome!",
                description=
                f"""
                Welcome {interaction.user.mention}.\n
                Please describe the reason for the creation of this ticket below.\n
                Remember, do **NOT** ping any staff members in this ticket.
                """,
                color=discord.Color.blurple()
            )
            embed.set_footer(text="Sincerely, the CrackedNetwork team.")
            msg = await channel.send(
                content=interaction.user.mention,
                embed=embed,
                view=manageTicket(bot=self.bot)
            )
            await msg.pin(reason="First message in ticket")
            await channel.purge(limit=1, reason="ugly message")

            embed = discord.Embed(
                title="Ticket Created!",
                description=
                f"""
                Your ticket has been created.
                Please access it [here]({channel.jump_url}) ({channel.mention})
                """,
                color=discord.Color.green()
            )
            await interaction.edit_original_response(embed=embed)

            if (self.bot.settings.get('Log.Channel') is not None):
                log = self.bot.get_channel(self.bot.settings.get('Log.Channel'))
                embed = discord.Embed(
                    title=f"New Ticket",
                    description=f"{interaction.user.mention} created a [ticket]({channel.jump_url}) ({channel.mention})",
                    color=discord.Color.blurple()
                )
                embed.set_author(
                    name=interaction.user.display_name,
                    icon_url=interaction.user.avatar.url,
                    url=interaction.user.jump_url
                )
                await log.send(embed=embed)
        if select.values[0] == "Management":
            embed = discord.Embed(
                title="Creating your ticket...",
                description="Please be patient as we are working to create your ticket.",
                color=discord.Color.yellow()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True),
                interaction.user: discord.PermissionOverwrite(view_channel=True), 
                interaction.guild.get_role(self.bot.settings.get('Tickets.Role')): discord.PermissionOverwrite(view_channel=True)
            }
            if self.bot.settings.get('Tickets.Count') is None:
                self.bot.settings.set('Tickets.Count', 0)


            current = self.bot.settings.get('Tickets.Count')
            ticketNum = calcTicketNum(current=current)

            category = discord.utils.get(
                interaction.guild.categories,
                id=self.bot.settings.get("Tickets.Tickets")
            )

            self.bot.settings.set("Tickets.Count", ticketNum)

            channel = await interaction.guild.create_text_channel(
                name=f"mgmt-{interaction.user.name}-{ticketNum}",
                category=category,
                overwrites=overwrites
            )

            embed = discord.Embed(
                title="Welcome!",
                description=
                f"""
                Welcome {interaction.user.mention}.\n
                Please describe the reason for the creation of this ticket below.\n
                Remember, do **NOT** ping any staff members in this ticket.
                """,
                color=discord.Color.blurple()
            )
            embed.set_footer(text="Sincerely, the CrackedNetwork team.")
            msg = await channel.send(
                content=interaction.user.mention,
                embed=embed,
                view=manageTicket(bot=self.bot)
            )
            await msg.pin(reason="First message in ticket")
            await channel.purge(limit=1, reason="ugly message")

            embed = discord.Embed(
                title="Ticket Created!",
                description=
                f"""
                Your ticket has been created.
                Please access it [here]({channel.jump_url}) ({channel.mention})
                """,
                color=discord.Color.green()
            )
            await interaction.edit_original_response(embed=embed)

            if (self.bot.settings.get('Log.Channel') is not None):
                log = self.bot.get_channel(self.bot.settings.get('Log.Channel'))
                embed = discord.Embed(
                    title=f"New Ticket",
                    description=f"{interaction.user.mention} created a [ticket]({channel.jump_url}) ({channel.mention})",
                    color=discord.Color.blurple()
                )
                embed.set_author(
                    name=interaction.user.display_name,
                    icon_url=interaction.user.avatar.url,
                    url=interaction.user.jump_url
                )
                await log.send(embed=embed)