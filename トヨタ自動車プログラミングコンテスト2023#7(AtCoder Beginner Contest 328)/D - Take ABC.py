def func(s):
    stack = []

    for char in s:
        stack.append(char)

        if len(stack) >= 3 and stack[-3:] == list("ABC"):
            stack.pop()
            stack.pop()
            stack.pop()

    return ''.join(stack)

S = input()

print(func(S))