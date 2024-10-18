import sys
delta = [[1, 0], [0, -1], [-1, 0], [0, 1]]

def BFS(ROW, COL, IDX):
    total_move = 1
    stack = []
    stack.append([ROW, COL])
    while stack:
        now_row, now_col = stack.pop()
        for d_row, d_col in delta:
            n_row = now_row + d_row
            n_col = now_col + d_col
            if 0 <= n_row < N and 0 <= n_col < M:
                if arr[n_row][n_col] == 0:
                    total_move += 1
                    arr[n_row][n_col] = IDX
                    stack.append([n_row, n_col])
    return total_move

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
my_map = [[0] * M for _ in range(N)]
group = [0, 0]
idx = 2
for row_idx in range(N):
    for col_idx in range(M):
        if arr[row_idx][col_idx] == 0:
            arr[row_idx][col_idx] = idx
            group.append(BFS(row_idx, col_idx, idx))
            idx += 1

for row_idx in range(N):
    for col_idx in range(M):
        if arr[row_idx][col_idx] == 1:
            visited = []
            my_map[row_idx][col_idx] += 1
            for d_row, d_col in delta:
                n_row = row_idx + d_row
                n_col = col_idx + d_col
                if 0 <= n_row < N and 0 <= n_col < M:
                    num = group[arr[n_row][n_col]]
                    num_idx = arr[n_row][n_col]
                    if num_idx not in visited:
                        visited.append(num_idx)
                        my_map[row_idx][col_idx] += num
            print(my_map[row_idx][col_idx] % 10,end='')
        else:
            print(0,end='')
    print()