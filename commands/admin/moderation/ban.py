import discord
from discord.ext import commands
from discord.commands import Option


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    @commands.slash_command(name="ban", description="Bans a specified user")
    @commands.has_permissions(ban_members=True)
    async def ban(
        self,
        ctx: discord.ApplicationContext,
        user: Option(discord.User, description='The member to ban'), # type: ignore
        reason: Option(str, description="The reason why a user has been banned for", required=False) # type: ignore
    ):
        if int(ctx.user.id) == int(user.id):
            embed = discord.Embed(title="Error!", description="`You can't ban yourself`", color=discord.Color.red())
            await ctx.response.send_message(embed=embed, ephemeral=True)
            return

        try:
            embed = discord.Embed(title=f"You've been banned from the {ctx.guild.name} discord server.", color=discord.Color.yellow())
            embed.add_field(name="Reason", value=reason)
            await user.send(embed=embed)
        except Exception as error:
            global e
            e = error
        
        try: 
            await user.ban(reason=reason)
        except Exception as error: 
            embed = discord.Embed(title="Couldn't ban.", description=f"I couldn't ban {user.mention}.", color=discord.Color.red())
            embed.add_field(name=f"Error baning {user.display_name}", value=f'`{error}`')
            await ctx.response.send_message(embed=embed, ephemeral=True)
            return
        
        embed = discord.Embed(title="banned !", description=f"You've banned {user.mention}.", color=discord.Color.green())
        if e:
            embed.add_field(name=f"Error sending message to {user.display_name}", value=f"`{e}`")
        embed.add_field(name="Reason", value=reason)
        await ctx.response.send_message(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Ban(bot))