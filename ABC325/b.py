N = int(input())
W = [0 for _ in range(N)]
X = [0 for _ in range(N)]
for i in range(N):
    W[i], X[i] = map(int,input().split())

ans = 0

for hour in range(24):
    temp = 0
    for i in range(N):
        # 全て含むため"-1"
        if 9 <= (hour + X[i]) % 24 <= 17:
            temp += W[i]
    
    ans = max(ans, temp)

print(ans)