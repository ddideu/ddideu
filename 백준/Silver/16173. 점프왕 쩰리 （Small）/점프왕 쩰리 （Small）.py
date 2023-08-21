def JUMP_KING(s_r,s_c):
    dx = [0, 1]
    dy = [1, 0]
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append((s_r,s_c))
    visited[s_r][s_r] = 1
    while queue:
        row, col = queue.pop(0)
        if jump_map[row][col] == -1:
            return 'HaruHaru'
            break
        jump_size = jump_map[row][col]
        for k in range(2):  # 아니라면 for 문을 돌리면서
            ncol = (dx[k]*jump_size) + col   # 인접 행렬로 이동해서
            nrow = (dy[k]*jump_size) + row
            if 0 <= ncol < N and 0 <= nrow < N:  # 해당 조건 들
                if jump_map[nrow][ncol] >= -1 and visited[nrow][ncol] == 0:  # 만족했을때만
                    queue.append((nrow, ncol))   # 큐에 집어 넣은후
                    visited[nrow][ncol] = visited[nrow][ncol] + 1
    return 'Hing'


N = int(input())
jump_map = [list(map(int,input().split())) for _ in range(N)]
start_row_point, start_col_point = 0, 0
ans = JUMP_KING(start_row_point,start_col_point)
print(ans)