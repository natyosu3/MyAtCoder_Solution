# Placing Marbles

S = list(map(int, input()))
ct = 0


for s in S:
    if s == 1:
        ct += 1

print(ct)