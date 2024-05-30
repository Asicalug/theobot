import discord
from discord.ext import commands
from discord.commands import Option


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    @commands.slash_command(name="kick", description="Kicks a specified user")
    @commands.has_permissions(kick_members=True)
    async def kick(
        self,
        ctx: discord.ApplicationContext,
        user: Option(discord.Member, description='The member to kick'), # type: ignore
        reason: Option(str, description="The reason why a user has been kicked for", required=False) # type: ignore
    ):
        if int(ctx.user.id) == int(user.id):
            embed = discord.Embed(title="Error!", description="`You can't kick yourself`", color=discord.Color.red())
            await ctx.response.send_message(embed=embed, ephemeral=True)
            return

        try:
            embed = discord.Embed(title=f"You've been kicked from the {ctx.guild.name} discord server.", color=discord.Color.yellow())
            embed.add_field(name="Reason", value=reason)
            await user.send(embed=embed)
        except Exception as error:
            global e
            e = error
        
        try: 
            await user.kick(reason=reason)
        except Exception as error: 
            embed = discord.Embed(title="Couldn't Kick.", description=f"I couldn't kick {user.mention}.", color=discord.Color.red())
            embed.add_field(name=f"Error Kicking {user.display_name}", value=f'`{error}`')
            await ctx.response.send_message(embed=embed, ephemeral=True)
            return
        
        embed = discord.Embed(title="Kicked !", description=f"You've kicked {user.mention}.", color=discord.Color.green())
        if e:
            embed.add_field(name=f"Error sending message to {user.display_name}", value=f"`{e}`")
        else: pass
        embed.add_field(name="Reason", value=reason)
        await ctx.response.send_message(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Kick(bot))