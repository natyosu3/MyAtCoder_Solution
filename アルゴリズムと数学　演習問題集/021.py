from math import factorial

n, r = map(int, input().split())

ans = factorial(n) // (factorial(n-r) * factorial(r))
print(ans)