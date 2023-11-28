N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans=[]
for i in A:
    ans.append(min(R ,max(i,L)))  # AiとLの大きい方とRの小さい方を比較して小さい方をansに追加する

print(*ans)