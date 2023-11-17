def dates_dunc(N, D):
    count = 0
    for i in range(1, N + 1):
        for j in range(1, D[i - 1] + 1):
            i_str = str(i)
            j_str = str(j)
            if len(set(i_str + j_str)) == 1:
                count += 1
    return count

N = int(input().strip())
D = list(map(int, input().strip().split()))

result = dates_dunc(N, D)
print(result)