from collections import deque
delta = [[0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]]
clear = [[-1, 1], [-1, 0], [-1, -1], [0, -1]]
N, M = map(int, input().split())
arr = []
visited = []
people = 0

for i in range(N):
    arr.append(list(map(int, input().split())))

for j in range(N):
    visit_row = []
    for k in range(M):
        visit_row.append(1)
    visited.append(visit_row)

for row in range(N):
    for col in range(M):
        if visited[row][col] == 1:
            flag = 1
            mounted = deque()
            checked = [[row, col]]
            mounted.append([row, col])
            visited[row][col] = 0
            while mounted:
                x, y = mounted.popleft()
                for dx, dy in delta:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if flag == 1 and arr[nx][ny] > arr[x][y]:
                            flag = 0
                            continue
                        elif arr[nx][ny] == arr[x][y] and [nx, ny] not in checked:
                            visited[nx][ny] = 0
                            mounted.append([nx, ny])
                            checked.append([nx, ny])
            if flag == 1:
                people += 1

print(people)