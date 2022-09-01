from aioredis import Redis

from discord.ext import commands

import config

db = Redis(
    host=config.host,
    port=config.port, 
    username=config.username,
    password=config.password
)

async def check_user(ctx, user):
    check = db.get(user.id)

    if check is None:
        await ctx.reply('Bạn chưa có tài khoản!\nNhập `a.start` để tạo tài khoản ;)')

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description = 'Bắt đầu game :v')
    async def start(self, ctx):
        author = ctx.author

        check = db.get(author.id)

        if check is None:
            db.set(author.id, 10)
            await ctx.reply('Tạo tài khoản thành công!')
        else:
            await ctx.reply('Bạn đã tạo tài khoản rồi!')
        

    @commands.command(description = 'Kiểm tra tiền của bạn')
    async def cash(self, ctx):
        author = ctx.author

        user = db.get(author.id)

        await check_user(ctx, author)

        await ctx.reply(f'Bạn có {user.decode()}$')

    @commands.command(description = "Owner only")
    async def delete_eco(self, ctx):
        author = ctx.author

        if author.id == 972383714166321232:
            db.delete(972383714166321232)
            await ctx.reply("done")

    # @commands.command()
    # async def coinflip(self, ctx, *, coin = None):


async def setup(bot):
    await bot.add_cog(Economy(bot))
