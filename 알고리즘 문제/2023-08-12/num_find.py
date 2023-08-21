import sys
number_1 = int(sys.stdin.readline())
A_list = sorted(map(int, sys.stdin.readline().split()))
number_2 = int(sys.stdin.readline())
B_list = list(map(int, sys.stdin.readline().split()))

def binary(i, N, start, end):
    if start > end:
        return 0
    middle = (start + end) // 2
    if N[middle] == i:
        return 1
    elif N[middle] > i:
        return  binary(1, N, start, middle-1)
    else:
        return binary(1, N, middle + 1, end)

for i in B_list:
    start = 0
    end = len(A_list)
    print(binary(i, A_list, start, end))