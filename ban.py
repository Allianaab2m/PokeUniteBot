import collections
# import discord
ban_purple = ['ピカチュウ','ピカチュウ','ピカチュウ','ピカチュウ']
ban_orange = ['カビゴン','カビゴン','リザードン','リザードン'] # Test List
Character = ['ピカチュウ','ゲッコウガ','カビゴン','ワタシラガ','リザードン','ルカリオ','ファイアロー']

while len(ban_purple) + len(ban_orange) < 11: # purple orangeの配列要素数合計が11未満の時ずっと実行
    if len(ban_purple) < 5 or len(ban_orange) < 5: # どちらかが満タンかどうか検知
        TeamColor = input("Please select your team color:Purple or Orange ") # チーム名の入力を求める →リアクションで検知に変更

        if TeamColor == ('Purple'): # 紫チームの処理
            if len(ban_purple) == 5: # ちなみにさっきから出てるlenは配列に何個値が入ってるか調べてくれる関数です これが5であれば既に5人入ってることになる
                print("This team is full. Try another one.")
                continue # ループの先頭に戻る

            else: # 5人じゃなかった場合の処理
                BanCharacter = input("Please select your ban character:") # banしたいキャラクターの入力を求める →コマンドで入力に変更
                if BanCharacter in Character: # さっき入力された値がCharacter配列に存在するか調べる　
                    ban_purple.append(BanCharacter) # 入力された値を紫チームのban配列に追加
                    print("Selected ban character:" + BanCharacter)
                else: # 入ってなかった時
                    print("Such character does not exist. Try again.")
                    continue

        elif TeamColor == ('Orange'): # オレンジチームの処理 全部一緒
            if len(ban_orange) == 5:
                print("This team is full. Try another one.")
                continue

            else:
                BanCharacter = input("Please select your ban character:")
                if BanCharacter in Character:
                    ban_orange.append(BanCharacter)
                    print("Selected ban character: " + BanCharacter)
                else:
                    print("Such character does not exist. Try again.")
                    continue
        else: # PurpleかOrangeが入力されなかった時
            print("Such team does not exist. Try again.")
            continue

    else: # いっぱいになった時
        print("Game is full.")
        print(ban_purple)
        print(ban_orange)
        break # ループが暴れたので途中で終了させる

banned_purple = collections.Counter(ban_purple).most_common()[0][0] # 配列内の最頻値をbanned変数に入れる
banned_orange = collections.Counter(ban_orange).most_common()[0][0]
print(banned_purple)
print(banned_orange)
