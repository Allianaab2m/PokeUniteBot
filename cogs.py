import discord
import pokelist
import config
from discord.ext import commands

PPL_roleID = config.PURPLE_ROLE_ID
ORN_roleID = config.ORANGE_ROLE_ID
game_active = False

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

    # @commands.group()
    # async def game(self, ctx):
    #    if ctx.invoked_subcommand is None:
    #        await ctx.send("サブコマンドが要るで。pu.game startでゲーム開始するで。")

    # @game.command()
    # async def start(self, ctx):
    #     start_msg = await ctx.send("Start Game.")
    #     start_msg_id = start_msg.id
    #     game_active = True
    #     return start_msg_id

    # @game.command()
    # async def join(self, ctx, start_msg_id):
    #     if game_active == False:
    #         await ctx.send("まだゲームが開始されてへんみたいやで。先にpu.game startしてや。")
    #     elif game_active == True:
    #         async def on_raw_reaction_add(self, payload):
    #             if payload.member.bot:
    #                 return
            


def setup(bot):
    bot.add_cog(cogs(bot))
