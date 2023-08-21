import sys

number_1 = int(sys.stdin.readline())
A_list = list(map(int,sys.stdin.readline().split()))
number_2 = int(sys.stdin.readline())
B_list = list(map(int,sys.stdin.readline().split()))
A_list.sort()
for i in B_list:
    start = 0
    end = max(A_list)
    flag = 0
    while start <= end:
        middle = (start+end)//2
        if middle == i:
            flag = 1
            break
        elif middle > i:
            end = middle - 1
        else :
            start = middle + 1
    print(flag)