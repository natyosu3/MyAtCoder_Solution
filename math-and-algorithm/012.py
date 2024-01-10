def is_prime(N):
    if N <= 1:
        return False
    if N <= 3:
        return True

    if N % 2 == 0 or N % 3 == 0:
        return False

    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6

    return True

N = int(input())
result = is_prime(N)

if result:
    print("Yes")
else:
    print("No")
