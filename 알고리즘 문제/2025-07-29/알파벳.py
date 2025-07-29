from collections import deque
import sys
def find_max_cnt():
    queue = deque()
    queue.append([0, 0, arr[0][0]])
    cnt = 1
    while queue:
        now_row, now_col, my_word = queue.popleft()
        if len(my_word) > cnt:
            cnt = len(my_word)
        for dy, dx in delta:
            next_col = dx + now_col
            next_row = dy + now_row
            if 0 <= next_col < M and 0 <= next_row < N:
                if arr[next_row][next_col] not in my_word:
                    my_visited = my_word[:]
                    my_visited += arr[next_row][next_col]
                    queue.append([next_row, next_col, my_visited])
    return cnt

input = sys.stdin.readline
N, M = map(int,input().split())
arr = [list(map(str,input().rstrip())) for _ in range(N)]
delta = [[0, 1], [-1, 0], [0, -1], [1, 0]]
cnt = find_max_cnt()
print(cnt)