N, M = map(int, input().split())
S = input()
T = input()

T_head = T[:N]
T_tail = T[-N:]

if S == T_head and S == T_tail:
    print(0)
elif S == T_head:
    print(1)
elif S == T_tail:
    print(2)
else:
    print(3)