import discord
from discord.ext import commands


class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Xem độ trễ của bot')
    async def ping(self, ctx):
        await ctx.send(':ping_pong: Pong! `{}ms`'.format(round(self.bot.latency * 1000)))

    @commands.command(description='Xem tất cả lệnh và thông tin')
    async def help(self, ctx, cmd=None):
        if not cmd:
            embed = discord.Embed(
                title=f"Tất cả lệnh của {self.bot.user.name}",
                colour=discord.Color.random()
            )
            for cogs in self.bot.cogs:
                cog = self.bot.get_cog(cogs)
                if len([cog.walk_commands()]):
                    embed.add_field(
                        name=cog.qualified_name + ' :',
                        value=''.join(
                            f"**`{i.name}`:** _**{i.description or 'Không có mô tả'}**_ _(Alias: `{i.aliases or 'Không có'}`_)\n" for i in cog.walk_commands()),
                        inline=False
                    )
            await ctx.send(embed=embed)
        #     ##################################
        # for cogs in self.bot.cogs:
        #     cog = self.bot.get_cog(cogs)
        #     if len([cog.walk_commands()]):
        #         for commands in cog.walk_commands():
        #             if cmd == commands.name or commands.aliases:
        #                 embed = discord.Embed(
        #                     title=f"Lệnh: {cmd}",
        #                     description=f"**- Tên lệnh: `{commands.name}`**\n**- Mô tả lệnh: `{commands.description}`**\n**- Lệnh tắt: `{commands.aliases}`**",
        #                     colour=discord.Color.random()
        #                 )
        #                 return await ctx.reply(embed=embed)

    @commands.command(aliases=['av', 'avt'], description='Xem avatar của 1 user nào đó')
    async def avatar(self, ctx, member: discord.User = None):
        if not member:
            member = ctx.author
        embed = discord.Embed(
            title=f"{member}'s avatar",
            colour=discord.Color.random()
        )
        embed.set_image(url=member.display_avatar.url)
        await ctx.send(embed=embed)

    @avatar.error
    async def avatar_e(self, ctx, error):
        if isinstance(error, commands.UserNotFound):
            return await ctx.reply('Không tìm thấy user này')
        raise error


async def setup(bot):
    await bot.add_cog(Other(bot))
