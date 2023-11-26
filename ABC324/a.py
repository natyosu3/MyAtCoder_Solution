N = int(input())
A = list(map(int, input().split()))

ans = set()


for i in A:
    ans.add(i)

if len(ans) == 1:
    print("Yes")
else:
    print("No")