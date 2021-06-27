import discord
import config

TOKEN = config.TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)
game_status = False
PPL_react = '🟣'
ORN_react = '🟠'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('pu.start'):
        game_status = True
        msg = await message.channel.send('Start the custom game.')
        await msg.add_reaction(PPL_react)
        await msg.add_reaction(ORN_react)

@client.event
async def on_reaction_add(reaction ,user):

    if reaction.emoji == config.PPL_react:
        PPLRole = discord.utils.get(user.server.roles, name="Purple Team")
        await client.add.roles(user, PPLRole)

    if reaction.emoji == config.ORN_react:
        ORNRole = discord.utils.get(user.server.roles, name="Orange Team")
        await client.add.roles(user, ORNRole)


client.run(TOKEN)