row_line, col_line = map(int, input().split())
tile = [list(map(str, input()))for _ in range(row_line)]
row_tile = 0
col_tile = 0
for row in range(row_line):
    r_tile = 0
    stack = []
    for col in range(col_line):
        if tile[row][col] == '-' and col == 0 :
            r_tile += 1
            stack.append(tile[row][col])
        elif tile[row][col] == '|' and col == 0:
            r_tile = 0
            stack.append(tile[row][col])
        S = stack.pop()
        if S == tile[row][col] and tile[row][col] == '-':
            stack.append(S)
            stack.append(tile[row][col])
        else:
            if S == tile[row][col]:
                stack.append(S)
                stack.append(tile[row][col])
            elif S == '-' and tile[row][col] == '|':
                stack.append(S)
                stack.append(tile[row][col])
            else:
                stack.append(S)
                stack.append((tile[row][col]))
                r_tile += 1
    row_tile += r_tile

for row in range(col_line):
    c_tile = 0
    stack = []
    for col in range(row_line):
        if tile[col][row] == '|' and col == 0 :
            c_tile += 1
            stack.append(tile[col][row])
        elif tile[col][row] == '-' and col == 0:
            c_tile = 0
            stack.append(tile[col][row])
        S = stack.pop()
        if S == tile[col][row] and tile[col][row] == '|':
            stack.append(S)
            stack.append(tile[col][row])
        else:
            if S == tile[col][row]:
                stack.append(S)
                stack.append(tile[col][row])
            elif S == '|' and tile[col][row] == '-':
                stack.append(S)
                stack.append(tile[col][row])
            else:
                stack.append(S)
                stack.append((tile[col][row]))
                c_tile += 1
    col_tile += c_tile
print(row_tile+col_tile)
