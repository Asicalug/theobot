import discord
from discord.ext import commands, pages
from discord.ext.pages import Paginator, Page
from discord.commands import Option, SlashCommandGroup
import time

class StaffCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")
    
    def get_pages(self):
        return self.pages


    staff = SlashCommandGroup(name="staff", description="Various staff Commands")

    @staff.command(
        name='strike',
        description='Strikes a Staff member'
    )
    @commands.has_role("Strike Management")
    async def staff_strike(
        self,
        ctx: discord.ApplicationContext,
        user: Option(discord.Member, description="The staff member that you want to strike"), #type: ignore
        reason: Option(str, description="The reason why you striked this staff member") #type: ignore
    ):  
        
        role = discord.utils.find(lambda r: r.name == 'Staff Team', ctx.guild.roles)
        
        if role not in user.roles:
            embed = discord.Embed(title="Error!", description=f"{user.mention} is not a staff member", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)

        if role in user.roles:
            try:
                self.bot.settings.set(f"Staff.Striking.{user.name}.Strikes.{self.bot.settings.get(f'Staff.Striking.{user.name}.StrikeAmount')+1}", reason)
                self.bot.settings.set(f"Staff.Striking.{user.name}.StrikedBy.{self.bot.settings.get(f'Staff.Striking.{user.name}.StrikeAmount')+1}", ctx.user.name)
                self.bot.settings.set(f"Staff.Striking.{user.name}.StrikeTime.{self.bot.settings.get(f'Staff.Striking.{user.name}.StrikeAmount')+1}", int(time.time()))
                self.bot.settings.set(f'Staff.Striking.{user.name}.StrikeAmount', self.bot.settings.get(f'Staff.Striking.{user.name}.StrikeAmount')+1)
            except:
                self.bot.settings.set(f'Staff.Striking.{user.name}.StrikeAmount', 1)
                self.bot.settings.set(f"Staff.Striking.{user.name}.Strikes.1", reason)
                self.bot.settings.set(f"Staff.Striking.{user.name}.StrikeTime.1", int(time.time()))
                self.bot.settings.set(f"Staff.Striking.{user.name}.StrikedBy.1", ctx.user.name)


            try:
                embed = discord.Embed(title=f"You were striked in {ctx.guild.name}", description=f"<:raccoonsilly:1243215943841218611> Moderator: {ctx.user.name}\n<:raccoonhuh:1243215937407160470> Reason: {reason}", color=discord.Color.red())
                await user.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(
                    title=f"{user.name} has been sucessfully striked",
                    description=f"use /staff viewstrikes {user.mention} to view their strike list they have",
                    color=discord.Color.green()
                )
                embed.add_field(name="Error", value=f"Couldn't DM {user.name}\n`{e}`")
                await ctx.response.send_message(embed=embed)
                return

            embed = discord.Embed(
                title=f"{user.name} has been sucessfully striked",
                description=f"use /staff viewstrikes {user.mention} to view their strike list they have",
                color=discord.Color.green()
            )

            await ctx.response.send_message(embed=embed, ephemeral=True)


    @staff.command(
        name='viewstrikes',
        description='View strike list of a member'
    )
    @commands.has_role("Strike Management")
    async def staff_strike(
        self,
        ctx: discord.ApplicationContext,
        user: Option(discord.Member, description="The staff member that you want to view their strikes."), #type: ignore
    ):  
        
        self.pages = []

        for i in range(self.bot.settings.get(f'Staff.Striking.{user.name}.StrikeAmount')):
            i = i+1
            self.pages.append(
                Page(
                    embeds=[
                        discord.Embed(title=f"Strike {i}", description=f"> ⏰ Issued on: <t:{self.bot.settings.get(f'Staff.Striking.{user.name}.StrikeTime.{i}')}>\n> ⚒️ Moderator: {self.bot.settings.get(f'Staff.Striking.{user.name}.StrikedBy.{i}')}\n> 📝 Reason: {self.bot.settings.get(f'Staff.Striking.{user.name}.Strikes.{i}')}", color=discord.Color.yellow()).set_thumbnail(url=user.avatar.url)
                    ]
                )
            )
        paginator = pages.Paginator(pages=self.get_pages())
        await paginator.respond(ctx.interaction, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(StaffCommands(bot))