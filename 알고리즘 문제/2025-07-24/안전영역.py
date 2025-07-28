from collections import deque
delta = [[0, 1], [-1, 0], [0, -1], [1, 0]]


def BFS(ROW, COL):
    queue = deque()
    queue.append([row, col])
    visited[row][col] = water_flow + 1
    while queue:
        now_row, now_col = queue.popleft()
        for dy, dx in delta:
            n_r = now_row + dy
            n_c = now_col + dx
            if 0 <= n_r < N and 0 <= n_c < N and arr[n_r][n_c] > water_flow:
                if visited[n_r][n_c] <= water_flow:
                    visited[n_r][n_c] = water_flow + 1
                    queue.append([n_r, n_c])


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1]*N for _ in range(N)]
cnt = 0
water_flow = -1
while True:
    ins = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] > water_flow:
                if visited[row][col] <= water_flow:
                    BFS(row,col)
                    ins += 1
    cnt = max(cnt, ins)
    water_flow += 1
    if ins == 0:
        break
print(cnt)
