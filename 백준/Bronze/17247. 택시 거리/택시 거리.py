N, M = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(N)]
node_dot = []
flag = 2
for row in range(N):
    for col in range(M): 
        if my_map[row][col] == 1:
            node_dot.append([row, col])
            flag -= 1
    if flag == 0:
        break 
print(abs(node_dot[0][0] - node_dot[1][0]) + abs(node_dot[0][1] - node_dot[1][1]))
