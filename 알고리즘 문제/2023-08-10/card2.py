import sys

def card(N):

    stack = list(range(N,0,-1))

    while len(stack) != 1:
        stack.pop()
        temp = stack.pop()
        stack.insert(0, temp)
    return stack


Number = int(sys.stdin.readline())
print(*card(Number))