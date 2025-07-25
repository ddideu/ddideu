from collections import deque
import sys
delta = [[0, 1], [-1, 0], [0, -1], [1, 0]]
def BFS(Queue, my_zone, count):
    my_Queue = Queue.copy()
    visited = [[0] * M for _ in range(N)]
    now_zone = my_zone
    while my_Queue:
        if now_zone <= count:
            break
        now_row, now_col = my_Queue.popleft()
        for dy, dx in delta:
            next_r = now_row + dy
            next_c = now_col + dx
            if 0<= next_r < N and 0 <= next_c < M:
                if visited[next_r][next_c] == 0 and lab[next_r][next_c] == 0:
                    now_zone -= 1
                    visited[next_r][next_c] = 1
                    my_Queue.append([next_r, next_c])
    return now_zone




def wall_creator(Row, Col, number, Q, Zone):
    global cnt
    if number == 0:
        result = BFS(Q, Zone, cnt)
        cnt = max(result, cnt)
        return

    for n_r in range(N):
        for n_c in range(M):
            if lab[n_r][n_c] == 0:
                if n_r > Row or (n_r == Row and n_c > Col):
                    lab[n_r][n_c] = 1
                    wall_creator(n_r, n_c, number-1, Q, Zone)
                    lab[n_r][n_c] = 0

input = sys.stdin.readline
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
safe_area = N*M - 3
queue = deque()

for row in range(N):
    for col in range(M):
        if lab[row][col] == 2:
            queue.append([row, col])
            safe_area -= 1
        if lab[row][col] == 1:
            safe_area -= 1

for row in range(N):
    for col in range(M):
        if lab[row][col] == 0:
            lab[row][col] = 1
            wall_creator(row, col, 2, queue, safe_area)
            lab[row][col] = 0

print(cnt)
