def convert_col(alpha):
    convert = 0
    if alpha == 'A':
        convert = 0
    elif alpha == 'B':
        convert = 1
    elif alpha == 'C':
        convert = 2
    elif alpha == 'D':
        convert = 3
    elif alpha == 'E':
        convert = 4
    else:
        convert = 5
    return convert

def convert_row(alpha):
    convert = 0
    if alpha == '1':
        convert = 5
    elif alpha == '2':
        convert = 4
    elif alpha == '3':
        convert = 3
    elif alpha == '4':
        convert = 2
    elif alpha == '5':
        convert = 1
    else:
        convert = 0
    return convert

visited = [[True] * 6 for _ in range(6)]
my_row = -1
my_col = -1
start_row = -1
start_col = -1
flag = 1
delta = [[1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1], [-2,1], [-1,2]]
for _ in range(36):
    now_col, now_row = map(str, input())
    now_col = convert_col(now_col)
    now_row = convert_row(now_row)
    if visited[now_row][now_col]:
        visited[now_row][now_col] = False
    else:
        flag = 0
        break
    if my_row != -1 and my_col != -1:
        delta_flag = 1
        for dy, dx in delta:
            next_row = my_row + dy
            next_col = my_col + dx
            if next_row == now_row and next_col == now_col:
                my_row = now_row
                my_col = now_col
                delta_flag = 0
                visited[now_row][now_col] = False
                break
        if delta_flag:
            flag = 0
            break
    else:
        my_row = now_row
        my_col = now_col
        start_row = now_row
        start_col = now_col


for dy, dx in delta:
    next_row = my_row + dy
    next_col = my_col + dx
    if next_row == start_row and next_col == start_col:
        break
else:
    flag = 0
if flag:
    print('Valid')
else:
    print('Invalid')