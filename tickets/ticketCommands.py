import discord
from discord.ext import commands
from discord.commands import Option, SlashCommandGroup

from views.tickets.selector import Selector

class TicketCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    ticket = SlashCommandGroup(name="ticket", description="Various Ticket Commands")

    @ticket.command(
        name='setup',
        description='sets up the ticket system'
    )
    @commands.has_permissions(administrator=True)
    async def setup_ticket(
        self,
        ctx: discord.ApplicationContext,
        panel: Option(discord.TextChannel, description='The panel where the users can create a ticket', required=False), # type: ignore
        tickets: Option(discord.CategoryChannel, description='The category where the tickets will be created', required=False), # type: ignore
        closed: Option(discord.CategoryChannel, 'The channel where you want the closed channels to be moved to.', required=False), # type: ignore
        role: Option(discord.Role, description='The role for the staff members that you want to have access to tickets', required=False) # type: ignore
    ):
        if panel is None:
            if self.bot.settings.get('Tickets.Panel') is not None:
                panel = self.bot.settings.get('Tickets.Panel')
            else:
                embed = discord.Embed(
                    title="Error!",
                    description="You need to setup the panel first.",
                    color=discord.Color.red()
                )
                await ctx.response.send_message(embed=embed, ephemeral=True)

        if tickets is None:
            if self.bot.settings.get('Tickets.Tickets') is not None:
                panel = self.bot.settings.get('Tickets.Tickets')
            else: 
                embed = discord.Embed(
                    title="Error!",
                    description="You need to setup the `tickets category` first.",
                    color=discord.Color.red()
                )
                await ctx.response.send_message(embed=embed, ephemeral=True)

        if closed is None:
            if self.bot.settings.get('Tickets.Closed') is not None:
                panel = self.bot.settings.get('Tickets.Closed')
            else: 
                embed = discord.Embed(
                    title="Error!",
                    description="You need to setup the `closed category` first.",
                    color=discord.Color.red()
                )
                await ctx.response.send_message(embed=embed, ephemeral=True)

        if role is None:
            if self.bot.settings.get('Tickets.Role') is not None:
                panel = self.bot.settings.get('Tickets.Role')
            else: 
                embed = discord.Embed(
                    title="Error!",
                    description="You need to setup the `role` first.",
                    color=discord.Color.red()
                )
                await ctx.response.send_message(embed=embed, ephemeral=True)

        elif panel != None and tickets != None and closed != None: 
            self.bot.settings.set('Tickets.Panel', panel.id)
            self.bot.settings.set('Tickets.Tickets', tickets.id)
            self.bot.settings.set('Tickets.Closed', closed.id)
            self.bot.settings.set('Tickets.Role', role.id)

        panel = self.bot.get_channel(self.bot.settings.get('Tickets.Panel'))
        tickets = self.bot.get_channel(self.bot.settings.get('Tickets.Tickets'))
        closed = self.bot.get_channel(self.bot.settings.get('Tickets.Closed'))
        role = ctx.guild.get_role(self.bot.settings.get('Tickets.Role'))
        embed = discord.Embed(
            title="Open a Ticket",
            description="Open a Ticket by clicking the button below.",
            color=discord.Color.blurple()
        )
        await panel.send(embed=embed, view=Selector(bot=self.bot))


        if (self.bot.settings.get('Log.Channel') is not None):
            log = self.bot.get_channel(self.bot.settings.get('Log.Channel'))
            embed = discord.Embed(
                title="Ticket System Setup",
                description=f"{ctx.user.mention} has setted up the ticket system",
                color=discord.Color.blurple()
            )
            embed.set_author(
                name=ctx.user.display_name,
                icon_url=ctx.user.avatar.url,
                url=ctx.user.jump_url
            )
            embed.add_field(
                name='Panel',
                value=panel.mention,
                inline=True
            )
            embed.add_field(
                name='Category',
                value=tickets.mention,
                inline=True
            )
            embed.add_field(
                name='Closed Category',
                value=closed.mention,
                inline=True
            )
            embed.add_field(
                name='Role',
                value=role.mention,
                inline=True
            )

            await log.send(embed=embed)


        embed = discord.Embed(
            title="Ticket System Setted Up!",
            description="The Ticket System Has Been Succesfully setted up",
            color=discord.Color.green()
        )
        embed.add_field(
            name='Panel',
            value=panel.mention,
            inline=True
        )
        embed.add_field(
            name='Category',
            value=tickets.mention,
            inline=True
        )
        embed.add_field(
            name='Closed Category',
            value=closed.mention,
            inline=True
        )
        embed.add_field(
            name='Role',
            value=role.mention,
            inline=True
        )

        await ctx.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(TicketCommands(bot))