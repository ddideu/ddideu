from collections import deque
import sys
N, M = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
visited = [1 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int,sys.stdin.readline().split())
    arr[A].append(B)
    arr[B].append(A)
cnt = 0

for i in range(1, N+1):
    if visited[i]:
        queue = deque()
        queue.append(i)
        visited[i] = 0
        while queue:
            start = queue.popleft()
            for idx in arr[start]:
                if visited[idx]:
                    visited[idx] = 0
                    queue.append(idx)
        cnt += 1
print(cnt)