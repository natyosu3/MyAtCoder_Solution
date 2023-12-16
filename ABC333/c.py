N = int(input().strip())

repunits = [int('1' * i) for i in range(1, N*3+1)]

sums = set()
for i in range(N*3):
    for j in range(i, N*3):
        for k in range(j, N*3):
            sums.add(repunits[i] + repunits[j] + repunits[k])


sums = sorted(list(sums))

print(sums[N-1])