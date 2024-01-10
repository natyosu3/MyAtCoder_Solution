import math

def find_divisors(N):
    sqrt_N = int(math.sqrt(N))
    
    for i in range(1, sqrt_N + 1):
        if N % i == 0:
            print(i)
            if i != N // i:
                print(N // i)

N = int(input())
divisors = find_divisors(N)
