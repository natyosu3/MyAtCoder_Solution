def move(direction, ans):



N, Q = map(int, input().split())

ans_direction = [(int, int)] * N

for i in range(1, N + 1):
    ans_direction[i-1] = ((i, 0))


for i in range(Q):
    query = input().split()

    if query[0] == '1':
        if query[1] == 'L':
            # 竜の頭を左に動かす
            pass
        elif query[1] == 'R':
            # 竜の頭を右に動かす
            pass
        elif query[1] == 'U':
            # 竜の頭を上に動かす
            pass
        elif query[1] == 'D':
            # 竜の頭を下に動かす
            pass

    elif query[0] == '2':
        print(ans_direction[int(query[1]) - 1])

print(ans_direction)