from collections import Counter

s = input()

counter = Counter(s)
max_count = max(counter.values())
most_common_chars = [char for char, count in counter.items() if count == max_count]
print(min(most_common_chars))
