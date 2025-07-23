from collections import deque
import sys
N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
parents = [i for i in range(N+1)]
visited = [1 for _ in range(N+1)]
for _ in range(N-1):
    S, E = map(int, sys.stdin.readline().split())
    arr[S].append(E)
    arr[E].append(S)

queue = deque()
queue.append(1)
visited[1] = 0
while queue:
    start = queue.popleft()
    for idx in arr[start]:
        if visited[idx]:
            visited[idx] = 0
            parents[idx] = start
            queue.append(idx)
for parent in parents[2:]:
    print(parent)

