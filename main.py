import config
import discord
from discord.ext import commands

import traceback
TOKEN = config.TOKEN

INITIAL_EXTENSIONS = [
        'cogs'
        ]

class PUBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        print(self.user.name)
        print(self.user.id)

if __name__ == '__init__':
    bot = PUBot(command_prefix='pu.')
    bot.run(TOKEN)
