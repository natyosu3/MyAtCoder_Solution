def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def func(n):
    digit_sum_value = digit_sum(n)
    return n % digit_sum_value == 0

N = int(input())
count = 0

for i in range(1, N+1):
    if func(i):
        count += 1

print(count)
