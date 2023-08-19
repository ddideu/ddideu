from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque()
for i in range(N):
    arr = list(map(str, sys.stdin.readline().split()))
    if arr[0] == 'push':
        queue.append(int(arr[1]))
    elif arr[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(queue))
    elif arr[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif arr[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
