from collections import deque
def Knight_map(ROW,COL):
    queue = deque()
    queue.append([ROW, COL])
    while queue:
        n_row, n_col = queue.popleft()
        for dx, dy in knight_jump:
            nx = n_col + dx
            ny = n_row + dy
            if 0 <= nx < M and 0 <= ny < N:
                if arr[ny][nx] != '#' and visited[ny][nx] == 0:
                    queue.append([ny, nx])
                    if arr[ny][nx] == 'X':
                        return visited[n_row][n_col]
                    visited[ny][nx] = visited[n_row][n_col] + 1

    return -1


knight_jump = [[2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]
N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for row in range(N):
    for col in range(M):
        if arr[row][col] == 'K':
            visited[row][col] = 1
            total_jump = Knight_map(row, col)
            print(total_jump)