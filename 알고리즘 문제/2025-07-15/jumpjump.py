def My_Right_Jump(loc, roads, Jump):
    total_jump = 1
    flag = 1
    while loc < total_block - 1:
        if roads[loc] <= Jump:
            total_jump += 1
            loc += 1
        else:
            if flag:
                flag = 0
                total_jump += 1
                loc += 1
            else:
                break
    return total_jump

def My_Left_Jump(loc, roads, Jump):
    total_jump = 1
    flag = 1
    while loc > -1:
        if roads[loc] <= Jump:
            total_jump += 1
            loc -= 1
        else:
            if flag:
                flag = 0
                total_jump += 1
                loc -= 1
            else:
                break
    return total_jump

total_block, my_jump = map(int,input().split())
roads = list(map(int,input().split()))
jumps = 0
for i in range(total_block):
    my_right = My_Right_Jump(i,roads,my_jump)
    my_left = My_Left_Jump(total_block-2-i,roads,my_jump)
    jumps = max(jumps, my_left, my_right)
    if jumps == total_block:
        break
print(jumps)