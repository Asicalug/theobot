import discord
# Defines a custom Select containing colour options
# that the user can choose. The callback function
# of this class is called when the user changes their choice.
class SelectJob(discord.ui.Select):
    def __init__(self, bot):
        # For example, you can use self.bot to retrieve a user or perform other functions in the callback.
        # Alternatively you can use Interaction.client, so you don't need to pass the bot instance.
        self.bot = bot
        # Set the options that will be presented inside the dropdown:
        options=[
            discord.SelectOption(
                label="Starbucks Employee",
                description="Hires you as a starbucks employee"
            ),
            discord.SelectOption(
                label="McDonalds",
                description="Hires you as a McDonalds employee"
            ),
            discord.SelectOption(
                label="KFC",
                description="Hires you as a KFC employee"
            )
        ],        

        # The placeholder is what will be shown when no option is selected.
        # The min and max values indicate we can only pick one of the three options.
        # The options parameter, contents shown above, define the dropdown options.
        super().__init__(
            placeholder="Get a job...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        selected_job = self.get_item(selected_job).values[0]
        embed = discord.Embed(title="Success", description=f"You're now a {selected_job}\nUse `/job work` to work.")
        await interaction.response.send_message(embed=embed, ephemeral=True)
