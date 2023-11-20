N = int(input())
A = list(map(int, input().split()))

cnt = 0
table = {}

# O(n^2)
# for i in range(N):
#     for j in range(i + 1, N):
#         if A[i] + A[j] == 100000: cnt += 1

# O(n)
for i in range(N):
    comp = 100000 - A[i]
    if comp in table:
        cnt += 1
    table[A[i]] = True

print(cnt)