import discord, os, sys, asyncio
from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send('hi')

async def setup(bot):
    await bot.add_cog(Owner(bot))
