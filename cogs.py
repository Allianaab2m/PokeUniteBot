import discord
import pokelist
from discord.ext import commands

class cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong.')

    @commands.command()
    async def pokemon(self, ctx, pokemon):
        if pokemon in pokelist:
            await ctx.send(pokemon)
        else:
            await ctx.send("Invalid value")

def setup(bot):
    bot.add_cog(cogs(bot))
