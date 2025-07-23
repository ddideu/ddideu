# 공청기 위쪽의 흐름
def air_Flow_A(ROW, COL, ARR):
    flag = 2
    delta_1 = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    delta_2 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(ROW):
        if ARR[i][0] == -1:
            now = 0
            ny, nx = i, 0
            point = 0
            while True:
                ny += delta_1[point][0]
                nx += delta_1[point][1]
                if 0 <= nx < COL and 0 <= ny <= i and ARR[ny][nx] != -1:
                    next_time = ARR[ny][nx]
                    ARR[ny][nx] = now
                    now = next_time
                else:
                    if point == 3:
                        break
                    else:
                        ny -= delta_1[point][0]
                        nx -= delta_2[point][1]
                        point += 1
            break
    return ARR, i+1
# 공청기 아래의 흐름
def air_Flow_B(ROW, COL, NEXT, ARR):
    delta_2 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    now = 0
    ny, nx = NEXT, 0
    point = 0
    while True:
        ny += delta_2[point][0]
        nx += delta_2[point][1]
        if 0 <= nx < COL and NEXT <= ny < ROW and ARR[ny][nx] != -1:
            next_time = ARR[ny][nx]
            ARR[ny][nx] = now
            now = next_time
        else:
            if point == 3:
                break
            else:
                ny -= delta_2[point][0]
                nx -= delta_2[point][1]
                point += 1
    return ARR

# 먼지의 이동
def air_Blow(ROW, COL, ARR):
    fact = [[0 for _ in range(C)] for _ in range(R)]
    delta = [[0,1],[-1,0],[0,-1],[1,0]]
    for nowRow in range(ROW):
        for nowCol in range(COL):
            # 델타 이동통해서 -1위치는 공청기 그리고 4이하면 유지
            if ARR[nowRow][nowCol] == -1:
                fact[nowRow][nowCol] = -1
            elif ARR[nowRow][nowCol] < 5:
                fact[nowRow][nowCol] += ARR[nowRow][nowCol]
            # 5이상이면 먼지의 이동
            else:
                blow_num = 0
                for dy, dx in delta:
                    ny = nowRow + dy
                    nx = nowCol + dx
                    if 0 <= ny < ROW and 0 <= nx < COL and ARR[ny][nx] != -1:
                        fact[ny][nx] += ARR[nowRow][nowCol] // 5
                        blow_num += 1
                fact[nowRow][nowCol] += ARR[nowRow][nowCol] - (ARR[nowRow][nowCol] // 5) * blow_num
    # 이동이 완료된 먼지 상태
    ARR = fact
    return ARR

# 초기 설정, 행 열, 시간, 처음 먼지 상태
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# 몇번 반복할것인지
start = 0
total_dust = 0
while start < T:
    arr = air_Blow(R,C,arr)
    arr, next_row = air_Flow_A(R,C,arr)
    arr = air_Flow_B(R,C,next_row,arr)
    start += 1

for checks in arr:
    for check in checks:
        if check != -1:
            total_dust += check
print(total_dust)
