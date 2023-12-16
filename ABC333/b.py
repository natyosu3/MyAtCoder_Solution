stmp = input()
S1, S2 = stmp[0], stmp[1]
ttmp = input() 
T1, T2 = ttmp[0], ttmp[1]

points = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
S_distance = abs(points[S1] - points[S2])
T_distance = abs(points[T1] - points[T2])
S_distance = min(S_distance, 5 - S_distance)
T_distance = min(T_distance, 5 - T_distance)
if S_distance == T_distance:
   print('Yes')
else:
    print('No')