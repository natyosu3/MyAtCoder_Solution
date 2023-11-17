def calculate_total_score(scores, X):
    total = 0
    for score in scores:
        if score <= X:
            total += score
    return total


N, X = map(int, input().split())

scores = list(map(int, input().strip().split()))

result = calculate_total_score(scores, X)

print(result)