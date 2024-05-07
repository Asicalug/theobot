import discord
from discord.ext import commands
from discord.commands import Option
import shutil
import requests
import uuid


class Warn(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    @commands.slash_command(name="warn")
    @commands.has_permissions(moderate_members=True)
    async def warn(
        self,
        ctx: discord.ApplicationContext,
        member: Option(discord.User, description='The member to warn'), # type: ignore
        reason: Option(str, description='The reason why you warned that member'), #type: ignore
        proof: Option(discord.Attachment, description='The proof for why you warned him') #type: ignore
    ):


        try:
            await proof.save(fp=f"{member.name}_warn{self.bot.settings.get(f'Cases.{member.name}.WarnAmount')+1}.png")
            shutil.move(f"{member.name}_warn{self.bot.settings.get(f'Cases.{member.name}.WarnAmount')+1}.png", "images/proofs/warns")
            self.bot.settings.set(f"Cases.{member.name}.Warns.{self.bot.settings.get(f'Cases.{member.name}.WarnAmount')+1}", reason)
            self.bot.settings.set(f"Cases.{member.name}.WarnedBy.{self.bot.settings.get(f'Cases.{member.name}.WarnAmount')+1}", ctx.user.name)
            self.bot.settings.set(f'Cases.{member.name}.WarnAmount', self.bot.settings.get(f'Cases.{member.name}.WarnAmount')+1)

        except:
            await proof.save(fp=f"{member.name}_warn1.png")
            shutil.move(f"{member.name}_warn1.png", "images/proofs/warns")
            self.bot.settings.set(f'Cases.{member.name}.WarnAmount', 1)
            self.bot.settings.set(f"Cases.{member.name}.Warns.1", reason)
            self.bot.settings.set(f"Cases.{member.name}.WarnedBy.1", ctx.user.name)

        embed = discord.Embed(
            title=f"{member.name} has been sucessfully warned",
            description=f"use /case {member.mention} to view their full case",
            color=discord.Color.green()
        )
        await ctx.interaction.respond(embed=embed, ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Warn(bot))