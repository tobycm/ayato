"""
Help command cog for bot.
"""

from discord import Embed, Color
from discord.ext.commands import MinimalHelpCommand, Cog, Command

from models.bot_model import CustomBot


class CustomHelp(MinimalHelpCommand):
    """
    Help command for bot.
    """

    def get_command_signature(self, command: Command):  # pylint: disable=arguments-differ
        return f"{self.context.clean_prefix}{command.qualified_name} {command.signature}"

    async def send_bot_help(self, mapping) -> None:  # pylint: disable=arguments-differ
        embed = Embed(
            title="Bot Help",
            color=Color.random()
        )

        for cog, commands in mapping.items():
            commands = await self.filter_commands(commands, sort=True)
            command_signatures = [
                self.get_command_signature(c) for c in commands
            ]
            if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(
                    command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)


class MyCog(Cog):
    """
    Cog responsible for CustomHelp
    """

    def __init__(self, bot: CustomBot):
        self._original_help_command = bot.help_command
        self.bot = bot
        bot.help_command = CustomHelp()
        bot.help_command.cog = self

    async def cog_unload(self):
        self.bot.help_command = self._original_help_command
