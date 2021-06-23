import config
import discord

TOKEN = config.TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('Login.')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/ping':
        await message.channel.send('Pong!')

client.run(TOKEN)
