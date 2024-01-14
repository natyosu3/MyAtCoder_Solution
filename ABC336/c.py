def func(num, base):
    return ((num == 0) and "0") or (func(num // base, base).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % base])

N = int(input())
N -= 1


N = func(N, 5)

N = ''.join(str(int(digit)*2) for digit in str(N))

print(N)