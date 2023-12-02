N, S, M, L = map(int, input().split())


dp = [float('inf')] * (N + 13)
dp[0] = 0

for pack_size, pack_cost in [(6, S), (8, M), (12, L)]:
    for i in range(pack_size, N + 13):
        dp[i] = min(dp[i], dp[i - pack_size] + pack_cost)


print(min(dp[N:]))