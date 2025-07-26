from collections import deque
import sys
input = sys.stdin.readline

def knight_trip(Queue, End_R, End_C):
    knight_jump = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]
    while queue:
        now_row, now_col, now_count = queue.popleft()
        if now_row == end_row and now_col == end_col:
            return now_count
        for dy, dx in knight_jump:
            next_row = now_row + dy
            next_col = now_col + dx
            if 0 <= next_row < N and 0 <= next_col < N:
                if my_map[next_row][next_col]:
                    my_map[next_row][next_col] = False
                    queue.append([next_row,next_col, now_count + 1])


test = int(input())
for tc in range(test):
    N = int(input())
    my_map = [[True]*N for _ in range(N)]
    start_row, start_col = map(int, input().split())
    end_row, end_col = map(int, input().split())
    my_map[start_row][start_col] = False
    cnt = 0
    queue = deque()
    queue.append([start_row, start_col, cnt])
    if my_map[end_row][end_col] != 0:
        cnt = knight_trip(queue, end_row, end_col)
    print(cnt)