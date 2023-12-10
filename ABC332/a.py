N, S, K = map(int, input().split())
PQ = [list(map(int, input().split())) for _ in range(N)]


total = 0
for P, Q in PQ:
    total += P * Q
if total < S:
    total += K

print(total)