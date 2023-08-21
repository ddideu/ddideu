import sys
test = int(sys.stdin.readline())
stack = []
for tc in range(test):
    input_word = list(map(str, sys.stdin.readline().split()))
    if input_word[0] == 'push':
        stack.append(input_word[1])
    elif input_word[0] == 'top':
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)
    elif input_word[0] == 'size':
        s = len(stack)
        print(s)
    elif input_word[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif input_word[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
