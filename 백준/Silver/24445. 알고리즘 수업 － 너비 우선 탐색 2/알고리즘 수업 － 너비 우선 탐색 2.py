from collections import deque
import sys

def bFS(start):
    point = 2
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        for k in arr[now]:
            if visited[k] == 0:
                visited[k] = point
                point += 1
                queue.append(k)


N, M, R = map(int, sys.stdin.readline() .split())
arr = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    S, E = map(int, sys.stdin.readline() .split())
    arr[S].append(E)
    arr[E].append(S)

for i in arr:
    i.sort(reverse=True)

visited[R] = 1
bFS(R)
for j in range(1, N+1):
    print(visited[j])