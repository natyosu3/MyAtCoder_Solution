N = int(input())
A = list(map(int, input().split()))

next_person = [0] * N

for i in range(N):
    if A[i] != -1:
        next_person[A[i] - 1] = i + 1

head = A.index(-1) + 1
result = [head]

while next_person[head - 1] != 0:
    head = next_person[head - 1]
    result.append(head)

print(' '.join(map(str, result)))