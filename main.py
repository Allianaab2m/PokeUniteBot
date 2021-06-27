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
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return

    role_id = config.ROLE_DICT[payload.emoji.name]

client.run(TOKEN)