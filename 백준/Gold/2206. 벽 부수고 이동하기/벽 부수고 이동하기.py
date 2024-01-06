from collections import deque
N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
heart = 1
visited_not_break = [[0] * M for _ in range(N)]
visited_not_break[0][0] = 1
visited_break = [[0] * M for _ in range(N)]
visited_break[0][0] = 1
delta = [[0, 1], [-1, 0], [0, -1], [1, 0]]
queue = deque()
queue.append([0, 0, heart])

while queue:
    y, x, life = queue.popleft()
    if y == N-1 and x == M-1:
        break
    else:
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            if 0 <= nx < M and 0 <= ny < N:
                if life == 1:
                    if arr[ny][nx] == '0':
                        if visited_not_break[ny][nx] == 0:
                            visited_not_break[ny][nx] = visited_not_break[y][x] + 1
                            visited_break[ny][nx] = visited_break[y][x] + 1
                            queue.append([ny, nx, 1])
                    else:
                        if visited_break[ny][nx] == 0:
                            visited_break[ny][nx] = visited_not_break[y][x] + 1
                            queue.append([ny, nx, 0])
                else:
                    if arr[ny][nx] == '0':
                        if visited_break[ny][nx] == 0:
                            visited_break[ny][nx] = visited_break[y][x] + 1
                            queue.append([ny, nx, 0])


if visited_break[N-1][M-1] != 0:
    print(visited_break[N-1][M-1])
else:
    print(-1)