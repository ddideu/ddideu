test = int(input())

for tc in range(test):
    mine_map = []
    max_mine = 0
    N = int(input())
    number = list(map(int, input()))
    mine_list = list(map(str, input()))
    mine_map.append(number)
    mine_map.append(mine_list)
    for find in range(N):
        if mine_map[1][find] == '*':
            mine_map[0][find] -= 1
            max_mine += 1
            if find < N-1:
                mine_map[0][find+1] -= 1
            if find > 0 :
                mine_map[0][find-1] -= 1
    if mine_map[1][0] == '#' and mine_map[0][0] != 0 and mine_map[0][1] != 0:
        max_mine += 1
        mine_map[0][0] -= 1
        mine_map[0][1] -= 1
    for mine_find in range(1,N-1):
        if mine_map[1][mine_find] == '#':
            if mine_map[0][mine_find-1] != 0 and mine_map[0][mine_find] != 0 and mine_map[0][mine_find+1] != 0:
                max_mine += 1
                mine_map[0][mine_find - 1] -= 1
                mine_map[0][mine_find] -= 1
                mine_map[0][mine_find + 1] -= 1
    if mine_map[1][N-1] == '#' and mine_map[0][N-1] != 0 and mine_map[0][N-2] != 0:
        max_mine += 1
        mine_map[0][0] -= 1
        mine_map[0][1] -= 1
    print(max_mine)