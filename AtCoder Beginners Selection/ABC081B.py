# Shift only

N = input()
A = list(map(int, input().split()))
ct = 0

while all(x % 2 == 0 for x in A):
    A = [x / 2 for x in A]
    ct += 1

print(ct)