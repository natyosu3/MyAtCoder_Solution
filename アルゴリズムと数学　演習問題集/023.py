N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

blue_e, red_e = 0, 0


for i in range(N):
    blue_e += B[i]
    red_e += R[i]

blue_e /= N
red_e /= N

print(blue_e + red_e)