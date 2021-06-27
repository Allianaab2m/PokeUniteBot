from discord import message
from discord import client
from discord.ext.commands.cog import Cog
import pokelist
import config
from discord.ext import commands

PPL_roleID = config.PURPLE_ROLE_ID
ORN_roleID = config.ORANGE_ROLE_ID
game_active = False
PPL_react = '🟣'
ORN_react = '🟠'

class cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong.')

    @commands.command()
    async def pokemon(self, ctx, pokemon: str):
            if pokemon in pokelist.pokelist:
                await ctx.send(pokemon)
            else:
                await ctx.send("Invalid Value")

    @commands.group()
    async def game(self, ctx):
       if ctx.invoked_subcommand is None:
           await ctx.send("サブコマンドが要るで。pu.game startでゲーム開始するで。")
           await ctx.send(game_active)

    @game.command()
    async def start(self, ctx):
        start_msg = await ctx.send("始まるで～")
        await start_msg.add_reaction(PPL_react)
        await start_msg.add_reaction(ORN_react)
        game_active = True
        await ctx.send(game_active)
        return game_active

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            return
        
        if payload.emoji.name == PPL_react:
            await payload.member.add_roles(payload.member.guild.get_role(PPL_roleID))
        
        elif payload.emoji.name == ORN_react:
            await payload.member.add_roles(payload.member.guild.get_role(ORN_roleID))
                    
def setup(bot):
    # bot.add_cog(cogs(bot))
    print("Cog Loaded!")
    bot.load_extension('cogs')
