count = 0

N, S = map(int,input().split())


for i in range(1, N+1):
    for j in range(1, N+1):
        if i+j <= S:
            count += 1

print(count)