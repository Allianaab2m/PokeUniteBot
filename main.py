from os import name # ？
# システムの都合上Banという言葉が大量に出てきますが，DiscordサーバーからのBanではないです
import discord
import config # config.pyをインポート
import pokelist # pokelist.py(指定できるキャラが格納された配列)をインポート

TOKEN = config.TOKEN # configのTOKENを呼び出し

intents = discord.Intents.all() # Intents
client = discord.Client(intents=intents) # client
ban_embed = discord.Embed(
                    title="Ban Pick System", 
                    description="Ban Pick System on Discord.",
                    ) # 後で触るEmbedのテンプレート
ban_embed.add_field(name="Purple Team",value="Not Selcted")
ban_embed.add_field(name="Orange Team",value="Not Selcted") #ホントはテンプレートに入れたかった。nameが被ってるって怒られた。

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) # 起動したときにプリント .formatの意味実はあんまりわかってない
    await client.change_presence(activity=discord.Game(name='v.1.0.0')) # Presenceの設定

@client.event
async def on_message(message):
    if message.author.bot: # botなら弾く
        return

    if message.content == 'pu.repository': # repositoryコマンドなら
        await message.channel.send("https://github.com/Allianaab2m/PokeUniteBot") # レポジトリリンクを送る

    if message.content == 'pu.list': # listコマンド
        await message.channel.send(pokelist.pokelist) # [配列](pokelist.py)が返ってきます
    
    channel_ppl = client.get_channel(config.PURPLE_CHANNEL_ID) # チャンネルIDを設定
    channel_orn = client.get_channel(config.ORANGE_CHANNEL_ID)
    channel_ban = client.get_channel(config.BAN_CHANNEL_ID)

    if message.channel.id == config.PURPLE_CHANNEL_ID: # 送信されたチャンネルが紫のチャンネルなら
        if message.content in pokelist.pokelist: # そのメッセージの内容と一致するものがpokelist配列にあるか

            global ppl_ban # Embedに入れたいがためのグローバル変数宣言
            ppl_ban = message.content # message.contentをさっきの変数に格納
            await channel_ppl.send("あなたのチームのBanポケモン:" + ppl_ban) # 受け付けたら送信
            ban_embed.set_field_at(0, name="Purple Team", value=ppl_ban) # Embedテンプレートの値を編集
            msg = await channel_ban.fetch_message(send_embed_id)
            await msg.edit(embed = ban_embed)
            # print(ppl_ban)
            return ppl_ban
           
        else: # 配列になかったとき
            await channel_ppl.send("Invalid value")

    if message.channel.id == config.ORANGE_CHANNEL_ID: # 上のコピペ
        if message.content in pokelist.pokelist:
            orn_ban = message.content
            await channel_orn.send("あなたのチームのBanポケモン:" + orn_ban)
            ban_embed.set_field_at(1, name="Orange Team", value=orn_ban)
            msg = await channel_ban.fetch_message(send_embed_id)
            await msg.edit(embed = ban_embed)
            # print(orn_ban)
            return orn_ban

        else:
            await channel_orn.send("Invalid value")

@client.event
async def on_voice_state_update(member, before, after): # VC入ったときの動作
    global send_embed_id
    global send_embed
    if before.channel is None and after.channel is not None: # 入ったら
        if after.channel.id == config.PURPLE_VC_ID: # 紫チームのVCチャンネルなら
            role = member.guild.get_role(config.PURPLE_ROLE_ID)
            await member.add_roles(role) # 紫チームの役職を付与
            if len(after.channel.members) == 1 and len(client.get_channel(config.ORANGE_VC_ID).members) == 0: # 最初の紫VC参加者，かつオレンジVCに誰もいなかったら
                send_embed = await client.get_channel(config.BAN_CHANNEL_ID).send(embed = ban_embed) # Ban指定チャンネルにembedを送信
                send_embed_id = send_embed.id

        if after.channel.id == config.ORANGE_VC_ID: # オレンジチームのVCなら
            role = member.guild.get_role(config.ORANGE_ROLE_ID)
            await member.add_roles(role)
            if len(after.channel.members) == 1 and len(client.get_channel(config.PURPLE_VC_ID).members) == 0:
                send_embed = await client.get_channel(config.BAN_CHANNEL_ID).send(embed = ban_embed)
                send_embed_id = send_embed.id

    elif before.channel is not None and after.channel is None: # 抜けたとき
        if before.channel.id == config.PURPLE_VC_ID:
            role = member.guild.get_role(config.PURPLE_ROLE_ID)
            await member.remove_roles(role) # 役職剥奪

        if before.channel.id == config.ORANGE_VC_ID:
            role = member.guild.get_role(config.ORANGE_ROLE_ID)
            await member.remove_roles(role)
    

    
    
client.run(TOKEN)
