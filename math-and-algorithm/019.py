N = int(input())
A = list(map(int, input().split()))

red, yellow, blue = 0, 0, 0

for a in A:
    if a == 1:
        red += 1
    elif a == 2:
        yellow += 1
    elif a == 3:
        blue += 1

ans = int(0.5 * (red * (red - 1) + yellow * (yellow - 1) + blue * (blue - 1)))
print(ans)