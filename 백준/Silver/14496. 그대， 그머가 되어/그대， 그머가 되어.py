from collections import deque

start, end = map(int, input().split())
N, M = map(int, input().split())
move_point = -1
arr = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)

queue = deque()
queue.append(start)
while queue:
    s_point = queue.popleft()
    if s_point == end:
        move_point = visited[s_point]
        break
    for next_point in arr[s_point]:
        if visited[next_point] == 0:
            visited[next_point] = visited[s_point] +1
            queue.append(next_point)

print(move_point)