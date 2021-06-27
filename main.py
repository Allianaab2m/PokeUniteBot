from discord import client, guild, member
from discord.ext.commands.core import bot_has_any_role, command
from discord.flags import Intents
import config
import discord
from discord.ext import commands
import pokelist
import traceback

TOKEN = config.TOKEN

client = discord.Client()
discord_intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix="pu.",
    intents = discord_intents
)

INITIAL_EXTENSIONS = [
        'cogs'
        ]

class PUBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix, intents)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

        async def on_ready(self):
            print(self.user.name)
            print(self.user.id)

if __name__ == '__main__':
    bot.run(TOKEN)
