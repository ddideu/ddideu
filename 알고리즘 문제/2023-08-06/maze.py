row, col = map(int, input().split())
arr = [list(map(int, input())) for _ in range(row)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
x, y = 0, 0
direction = 0
count = 1
while x < row-1 or y < col-1:
    nx = x + dx[direction]
    ny = y + dy[direction]
    print(ny, nx)
    if 0 <= nx < col and 0 <= ny < row and arr[ny][nx] == 1:
        arr[y][x] = 0
        direction = 0
        count += 1
        x, y = nx, ny
        if x == col - 1 and y == row - 1:
            print(count)
            break
    else:
        direction = (direction + 1) % 4

        # 101111
        # 101010
        # 101011
        # 111011

        # 4 6
        # 110110
        # 110110
        # 111111
        # 111101