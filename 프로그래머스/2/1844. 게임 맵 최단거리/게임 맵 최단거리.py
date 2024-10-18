from collections import deque
def solution(maps):
    delta = [[0,1], [-1,0], [0,-1], [1,0]]
    answer = 0
    N = 0
    M = 0
    flag = 1
    visited = []
    queue = deque()
    for map in maps:
        N +=1
        if flag:
            M = len(map)
        tmp = [0] * M
        visited.append(tmp)
    visited[0][0] = 1
    visited[N-1][M-1] = -1
    queue.append([0,0])
    while queue:
        now_row, now_col = queue.popleft()
        for dy, dx in delta:
            next_row = now_row + dx
            next_col = now_col + dy
            if 0 <= next_row < N and 0 <= next_col < M:
                if visited[next_row][next_col] <= 0 and maps[next_row][next_col] == 1:
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    queue.append([next_row, next_col])
    answer = visited[N-1][M-1]
    
    return answer