import discord
import config
import pokelist

TOKEN = config.TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)
# game_status = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == config.PURPLE_VC_ID:
            role = member.guild.get_role(config.PURPLE_ROLE_ID)
            await member.add_roles(role)
        if after.channel.id == config.ORANGE_VC_ID:
            role = member.guild.get_role(config.ORANGE_ROLE_ID)
            await member.add_roles(role)

    elif before.channel is not None and after.channel is None:
        if before.channel.id == config.PURPLE_VC_ID:
            role = member.guild.get_role(config.PURPLE_ROLE_ID)
            await member.remove_roles(role)
        if before.channel.id == config.ORANGE_VC_ID:
            role = member.guild.get_role(config.ORANGE_ROLE_ID)
            await member.remove_roles(role)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    channel_ppl = client.get_channel(config.PURPLE_CHANNEL_ID)
    channel_orn = client.get_channel(config.ORANGE_CHANNEL_ID)

    if message.channel.id == config.PURPLE_CHANNEL_ID:
        if message.content in pokelist.pokelist:
            # channel = config.PURPLE_CHANNEL_ID
            ppl_ban = message.content
            await channel_ppl.send("あなたのチームのBanポケモン:" + ppl_ban)
        else:
            await channel_ppl.send("Invalid value")

    if message.channel.id == config.ORANGE_CHANNEL_ID:
        if message.content in pokelist.pokelist:
            await channel_orn.send(message.content)
        else:
            await channel_orn.send("Invalid value")

    else:
        print("Event Handled")
        print(type(message.content))
        print(message.content)
        print(message.channel.id)
        print(channel_ppl, channel_orn)

client.run(TOKEN)