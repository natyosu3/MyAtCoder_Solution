def ctz(N):
    count = 0
    while N % 2 == 0:
        N //= 2
        count += 1
    return count

N = int(input())

result = ctz(N)
print(result)
