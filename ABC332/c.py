N, M = map(int, input().split())
S = input()


ans = 0
wearing_plain = M 
wearing_logo = 0

for i in range(N):
    if S[i] == "0":
        # すべて洗濯
        wearing_plain = M
        wearing_logo = ans
        pass
    elif S[i] == "1":
        # 食事に行く日
        if wearing_plain > 0:
            # 無地のTシャツがあればそれを着用
            wearing_plain -= 1
        elif wearing_logo > 0:
            # ロゴ入りTシャツがあればそれを着用
            wearing_logo -= 1
        else:
            # ロゴ入りTシャツを購入
            ans += 1

    elif S[i] == "2":
        # 競技プログラミングのイベントに行く日
        if wearing_logo > 0:
            # ロゴ入りTシャツがあればそれを着用
            wearing_logo -= 1
        else:
            # ロゴ入りTシャツがない場合はロゴ入りTシャツを購入
            ans += 1


print(ans)
