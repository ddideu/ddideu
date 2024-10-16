from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    S = list(map(int, sys.stdin.readline().split()))
    if S[0] == 1:
        queue.appendleft(S[1])
    elif S[0] == 2:
        queue.append(S[1])
    elif S[0] == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif S[0] == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif S[0] == 5:
        print(len(queue))
    elif S[0] == 6:
        if queue:
            print(0)
        else:
            print(1)
    elif S[0] == 7:
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)