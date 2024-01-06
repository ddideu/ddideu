def BFS(STACK):
    global cnt
    while STACK:
        x1, y1 = STACK.popleft()
        for dx1, dy1 in delta:
            nx1 = x1 + dx1
            ny1 = y1 + dy1
            if 0 <= nx1 < M and 0 <= ny1 < N:
                if arr[ny1][nx1] == 0 and visited[ny1][nx1] == 0:
                    visited[ny1][nx1] = cnt
                    STACK.append([nx1, ny1])


from collections import deque
N, M = map(int, input().split())
delta = [[1, 0], [0, -1], [-1, 0], [0, 1]]
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 1
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
queue = deque()
queue.append([0, 0])
BFS(queue)


while True:
    my_queue = deque()
    for row in range(N):
        for col in range(M):
            if visited[row][col] == 0:
                count = 0
                for dx, dy in delta:
                    nx = col + dx
                    ny = row + dy
                    if visited[ny][nx] != 0:
                        count += 1
                    if count == 2:
                        my_queue.append([col, row])
                        break
    if my_queue:
        for x, y in my_queue:
            visited[y][x] = cnt
            arr[y][x] = 0
        BFS(my_queue)
        cnt += 1
    else:
        break

print(cnt - 1)