
s = input()
i = 0
while i < len(s) and s[i] == 'A':
    i += 1
s_a = s[:i]

j = i
while j < len(s) and s[j] == 'B':
    j += 1
s_b = s[i:j]

k = j
while k < len(s) and s[k] == 'C':
    k += 1
s_c = s[j:k]

remaining = s[k:]

if len(remaining) == 0:
    print("Yes")
else:
    print("No")
