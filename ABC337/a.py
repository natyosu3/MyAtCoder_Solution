N = int(input())

takahashi_score = 0
aoki_score = 0

for _ in range(N):
    X_i, Y_i = map(int, input().split())
    
    takahashi_score += X_i
    aoki_score += Y_i

if takahashi_score > aoki_score:
    print("Takahashi")
elif takahashi_score < aoki_score:
    print("Aoki")
else:
    print("Draw")
