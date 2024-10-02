vote = str(input())
count_u = 0
count_d = 0
for i in vote:
    if i == 'U' or i == 'C':
        count_u += 1
    else:
        count_d += 1
if count_u > count_d // 2 + count_d % 2:
    print('U', end="")
if count_d:
    print('DP')