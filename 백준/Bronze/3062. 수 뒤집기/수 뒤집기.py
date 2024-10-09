test = int(input())
for tc in range(test):
    num = str(input())
    reverse_num = ''
    flag = 1
    for i in num:
        reverse_num = i + reverse_num
    sum_num = str(int(num) + int(reverse_num))
    for j in range(len(sum_num)//2):
        if sum_num[j] != sum_num[len(sum_num)-1-j]:
            flag = 0
            break
    if flag:
        print('YES')
    else:
        print('NO')