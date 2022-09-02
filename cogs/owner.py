"""
Owner commands (nhưng nó hơi bủh)
"""

from discord.ext.commands import command, Context, Cog

from models.bot_model import CustomBot


class Owner(Cog):
    """
    Owner commands cog
    """

    def __init__(self, bot: CustomBot):
        self.bot = bot

    @command
    async def test(self, ctx: Context):
        """
        Test command
        """

        await ctx.send('hi')


async def setup(bot: CustomBot):
    """
    Run at setup
    """

    await bot.add_cog(Owner(bot))
