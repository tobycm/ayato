"""
Economy cog file for bot.
"""

from discord.ext.commands import Context, Cog, command

from models.bot_model import CustomBot
from modules.database_utils import get_money, set_money

class Economy(Cog):
    """
    Economy cog
    """

    def __init__(self, bot: CustomBot):
        self.bot = bot

    @command(description='Bắt đầu game :v')
    async def start(self, ctx: Context):
        """
        Init user with money
        """

        check = await get_money(self.bot.redis_ins, ctx.author.id)

        if check is not None:
            return await ctx.reply('Bạn đã tạo tài khoản rồi!')
        await set_money(self.bot.redis_ins, ctx.author.id, 10)
        await ctx.reply('Tạo tài khoản thành công!')

    @command(description='Kiểm tra tiền của bạn')
    async def cash(self, ctx: Context):
        """
        Check money balance
        """

        money = await get_money(self.bot.redis_ins, ctx.author.id)

        if money is None:
            return await ctx.reply('Bạn chưa tạo tài khoản!')
        return await ctx.reply(f"Bạn có ${money}")

async def setup(bot: CustomBot):
    """
    Run at setup
    """

    await bot.add_cog(Economy(bot))
