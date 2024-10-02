def DELTA(STACK):
    for now_y, now_x in STACK:
        for dy, dx in delta_twin:
            ny = now_y + dy
            nx = now_x + dx
            if arr[ny][nx] == '#':
                arr[now_y][now_x] = '#'
                break


delta_twin = [[1, 0], [-1, 0], [0, 1], [0, -1]]
N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N*3)]
twin_stack = []
odd_stack = []
## 3*3 에서 때려 죽여도 .을 유지 해야하는 곳 1,3,7,9 제일 첫행,첫열,끝행, 끝열 하나만 일치하면 . 유지.
yes_count = 0

for row in range(1, N*3-1):
    for col in range(1, M*3-1):
        if (row//3 + col//3) % 2 == 1 and (row % 3 == 1 or col % 3 == 1):
            if (row + col) % 2:
                odd_stack.append([row, col])
            else:
                twin_stack.append([row, col])

DELTA(twin_stack)
DELTA(odd_stack)

for idx in arr:
    print(*idx, sep="")

# 행을 3으로 나눈 나머지가 1이 아니고, 열을 3으로 나눈 나머지가 1이 아니라면 바꿔 말하면 1,3,7,9번에 해당하는 칸.
# 그부분은 패스를 해야 한다. 구현해보자.