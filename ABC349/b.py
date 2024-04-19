S = input()

dict1 = {}

for s in S:
    if s in dict1:
        dict1[s] += 1
    else:
        dict1[s] = 1

number = {}

for k, v in dict1.items():
    if v in number:
        number[v] += 1
    else:
        number[v] = 1

if all(v == 2 or v == 0 for v in number.values()):
    print("Yes")
else:
    print("No")