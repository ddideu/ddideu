
arr = list(map(str, input()))
stack = []

for i in arr:
    if i == '*':
        A = stack.pop()
        B = stack.pop()
        C = int(A) * int(B)
        stack.append(C)
    elif i == '/':
        A = stack.pop()
        B = stack.pop()
        C = int(B) // int(A)
        stack.append(C)
    elif i == '-':
        A = stack.pop()
        B = stack.pop()
        C = int(B) - int(A)
        stack.append(C)
    elif i == '+':
        A = stack.pop()
        B = stack.pop()
        C = int(B) + int(A)
        stack.append(C)
    else:
        stack.append(i)
print(*stack)