# TLE
N = int(input())
A = list(map(int, input().split()))

ans = [0]*N

for i in range(N):
    tmp = 0
    for j in range(N):
        if i == j:
            continue

        if A[i] < A[j]:
            tmp += A[j]
    
    ans[i] = (tmp)

print(*ans)