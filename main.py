import discord, os, config
from discord.ext import commands

token = config.token
prefix = ['a.', 'A.']
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), help_command=None)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="prefix is a. or A."))
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

bot.run(token)