def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

N = int(input())
print(factorial(N))