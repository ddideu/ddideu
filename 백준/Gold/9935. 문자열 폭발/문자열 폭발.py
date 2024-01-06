word = list(map(str, input()))
boom = str(input())
stack = []
for check in word:
    stack.append(check)
    if len(stack) >= len(boom) and check == boom[len(boom)-1]:
        flag = 1
        for j in range(len(boom)):
            if stack[len(stack)-1-j] != boom[len(boom)-j-1]:
                flag = 0
                break
        if flag == 1:
            for _ in range(len(boom)):
                stack.pop()


if stack:
    print(''.join(stack))
else:
    print('FRULA')