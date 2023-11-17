def count(s):
    n = len(s)
    counts = [0] * n

    for i in range(1, n):
        if s[i] == s[i - 1]:
            counts[i] = counts[i - 1] + 1
        else:
            counts[i] = counts[i - 1]

    return counts

def answer(s, queries):
    counts = count(s)
    results = []

    for query in queries:
        l, r = query
        result = counts[r - 1] - counts[l - 1]
        results.append(result)

    return results

N, Q = map(int, input().split())
S = input()
queries = [list(map(int, input().split())) for _ in range(Q)]

results = answer(S, queries)

for result in results:
    print(result)