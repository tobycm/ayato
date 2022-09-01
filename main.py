import os

from discord import Intents, Game
from discord.ext import commands

import config

token = config.token
prefix = ['a.', 'A.']
bot = commands.Bot(command_prefix=prefix, intents=Intents.all())


@bot.event
async def on_ready():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension("cogs." + file[:-3])
            print(f'Loaded cog {file}')
    print('Bot is ready!')

@bot.event
async def on_message(message):
    if message.content == f'<@{bot.user.id}>':
        await message.reply(f'**Prefix của bot là: `{prefix[0]}` or `{prefix[1]}`\nVà `{prefix[0]}help` để xem các lệnh của bot :)**')
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

async def startup_tasks():
    """
    Run after bot is ready
    """

    await bot.wait_until_ready()

    await bot.change_presence(activity=Game(name="prefix is a. or A."))

bot.loop.create_task(startup_tasks())

bot.run(token)
