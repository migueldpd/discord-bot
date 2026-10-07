import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix='!',
    intents=intents
)

async def main():
    await bot.load_extension('cogs.events')
    await bot.load_extension('cogs.commands')
    await bot.load_extension('cogs.gamble')
    await bot.start(token)

asyncio.run(main())