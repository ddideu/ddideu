from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
line = [0] * (N+1)
for _ in range(M):
    first, second = map(int, sys.stdin.readline().split())
    arr[first].append(second)
    line[second] += 1

queue = deque()

for i in range(1,N+1):
    if line[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    print(now, end=' ')
    for next_time in arr[now]:
        line[next_time] -= 1
        if line[next_time] == 0:
            queue.append(next_time)

