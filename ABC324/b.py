import sys
N = int(input())


for i in range(60):
    for j in range(40):
        if N == (2 ** i) * (3 ** j):
            print("Yes")
            sys.exit()

print("No")