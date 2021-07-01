# Guild
│

└ \# purple_banpick(config.PURPLE_CHANNEL_ID)
- 役職設定
    - Purple Team : 読み書き可
    - Orange Team : 見れない
    - everyone : 見れない
- ここに投稿されたキャラクター名を事前に送信しておいたEmbedに入れる
   

└ 🔊 purple_vc(config.PURPLE_VC_ID)
- 役職設定
    - everyone : 接続可
- 接続時にPurple Teamというロールが付与される(config.PURPLE_ROLE_ID)

└ \# orange_banpick(config.ORANGE_CHANNEL_ID)
- 役職設定
    - Purple Team : 見れない
    - Orange Team : 読み書き可
    - everyone : 見れない
- ここに投稿されたキャラクター名を事前に送信しておいたEmbedに入れる
   

└ 🔊 orange_vc(config.ORANGE_VC_ID)
- 役職設定
    - everyone : 接続可
- 接続時にOrange Teamというロールが付与される(config.ORANGE_ROLE_ID)

└ \# embed(config.BAN_CHANNEL_ID)
- Ban_channelとして取ってるやつ
- Embedを送信するだけのチャンネル
