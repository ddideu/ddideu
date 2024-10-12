test = int(input())
for tc in range(test):
    line, leaf = map(int,input().split())
    if (line*3) <= leaf <= (line*4):
        print(0)
    else:
        line_count = 0
        leaf_count = 0
        while ((line+line_count)*3) > (leaf+leaf_count) or ((line+line_count)*4) < (leaf+leaf_count):
            if ((line+line_count)*3) > (leaf+leaf_count):
                leaf_count += 1
            elif ((line+line_count)*4) < (leaf+leaf_count):
                line_count += 1
        print(line_count+leaf_count)


