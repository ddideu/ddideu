from collections import deque
N = int(input())
arr = [[] for _ in range(N)]
my_map = [[0] * N for _ in range(N)]
nodes = [list(map(int, input().split())) for _ in range(N)]
for row in range(N):
    for col in range(N):
        if nodes[row][col] == 1:
            arr[row].append(col)

for i in range(N):
    queue = deque()
    for idx in arr[i]:
        queue.append(idx)
    while queue:
        start = queue.popleft()
        my_map[i][start] = 1
        for next_idx in arr[start]:
            if my_map[i][next_idx] == 0:
                my_map[i][next_idx] = 1
                queue.append(next_idx)
for check in my_map:
    print(*check)