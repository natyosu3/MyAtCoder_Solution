# 011 - Print Prime Numbers

def prime_detect(N):
    for i in range(2, N+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
    print()

N = int(input())
prime_detect(N)