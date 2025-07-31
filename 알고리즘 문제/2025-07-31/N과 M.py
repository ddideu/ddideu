import sys
input = sys.stdin.readline

def check(Stack):
    if len(Stack) == M:
        print(*Stack)
        return
    for idx in range(N):
        if max(Stack) < arr[idx]:
            Stack.append(arr[idx])
            check(Stack)
            Stack.pop()
    return
N, M = map(int,input().split())
arr = sorted(map(int,input().split()))
for i in range(N):
    stack = [arr[i]]
    check(stack)