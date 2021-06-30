from os import name
import discord
import config
import pokelist

TOKEN = config.TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)
# game_status = False
ban_embed = discord.Embed(
                    title="Ban Pick System", 
                    description="Ban Pick System on Discord.",
                    )
ban_embed.add_field(name="Purple Team",value="Not Selcted")
ban_embed.add_field(name="Orange Team",value="Not Selcted")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='v.1.0.0'))

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == 'pu.repository':
        await message.channel.send("https://github.com/Allianaab2m/PokeUniteBot")

    if message.content == 'pu.list':
        await message.channel.send(pokelist.pokelist)
    
    channel_ppl = client.get_channel(config.PURPLE_CHANNEL_ID)
    channel_orn = client.get_channel(config.ORANGE_CHANNEL_ID)
    channel_ban = client.get_channel(config.BAN_CHANNEL_ID)

    if message.channel.id == config.PURPLE_CHANNEL_ID:
        if message.content in pokelist.pokelist:

            global ppl_ban 
            ppl_ban = message.content
            await channel_ppl.send("あなたのチームのBanポケモン:" + ppl_ban)
            ban_embed.set_field_at(0, name="Purple Team", value=ppl_ban)
            msg = await channel_ban.fetch_message(send_embed_id)
            await msg.edit(embed = ban_embed)
            print(ppl_ban)
            return ppl_ban
           
        else:
            await channel_ppl.send("Invalid value")

    if message.channel.id == config.ORANGE_CHANNEL_ID:
        if message.content in pokelist.pokelist:
            orn_ban = message.content
            await channel_orn.send("あなたのチームのBanポケモン:" + orn_ban)
            ban_embed.set_field_at(1, name="Orange Team", value=orn_ban)
            msg = await channel_ban.fetch_message(send_embed_id)
            await msg.edit(embed = ban_embed)
            print(orn_ban)
            return orn_ban

        else:
            await channel_orn.send("Invalid value")

@client.event
async def on_voice_state_update(member, before, after):
    global send_embed_id
    global send_embed
    if before.channel is None and after.channel is not None:
        if after.channel.id == config.PURPLE_VC_ID:
            role = member.guild.get_role(config.PURPLE_ROLE_ID)
            await member.add_roles(role)
            if len(after.channel.members) == 1 and len(client.get_channel(config.ORANGE_VC_ID).members) == 0:
                send_embed = await client.get_channel(config.BAN_CHANNEL_ID).send(embed = ban_embed)
                send_embed_id = send_embed.id

        if after.channel.id == config.ORANGE_VC_ID:
            role = member.guild.get_role(config.ORANGE_ROLE_ID)
            await member.add_roles(role)
            if len(after.channel.members) == 1 and len(client.get_channel(config.PURPLE_VC_ID).members) == 0:
                send_embed = await client.get_channel(config.BAN_CHANNEL_ID).send(embed = ban_embed)
                send_embed_id = send_embed.id

    elif before.channel is not None and after.channel is None:
        if before.channel.id == config.PURPLE_VC_ID:
            role = member.guild.get_role(config.PURPLE_ROLE_ID)
            await member.remove_roles(role)

        if before.channel.id == config.ORANGE_VC_ID:
            role = member.guild.get_role(config.ORANGE_ROLE_ID)
            await member.remove_roles(role)
    

    
    
client.run(TOKEN)