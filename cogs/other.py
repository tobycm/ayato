"""
Misc
"""

from discord import Embed, User, Color
from discord.ext.commands import Cog, command, Context

from models.bot_model import CustomBot

class Other(Cog):
    """
    Bot other commands cog
    """

    def __init__(self, bot: CustomBot):
        self.bot = bot

    @command(description='Xem độ trễ của bot')
    async def ping(self, ctx: Context):
        """
        Check bot ping
        """
        await ctx.send(f'\U0001f3d3 Pong! `{round(self.bot.latency * 1000)}ms`')

    @command(aliases=['av', 'avt'], description='Xem avatar của 1 user nào đó')
    async def avatar(self, ctx: Context, user: User = None):
        """
        Get user avatar
        """

        if user is None:
            user = ctx.author
        embed = Embed(
            title=f"{user}'s avatar",
            colour=Color.random()
        ).set_image(
            url=user.display_avatar.url
        )
        await ctx.send(embed=embed)

    # @avatar.error
    # async def avatar_e(self, ctx: Context, error):
    #     if isinstance(error, UserNotFound):
    #         return await ctx.reply('Không tìm thấy user này')
    #     raise error


async def setup(bot: CustomBot):
    """
    Run at setup
    """

    await bot.add_cog(Other(bot))
