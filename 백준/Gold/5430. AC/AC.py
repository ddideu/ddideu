from collections import deque
test = int(input())
for tc in range(test):
    P = str(input())
    N = int(input())
    X = input().strip('[]').split(',')
    arr = deque()
    R = False
    flag = True
    if N:
        for i in X:
            arr.append(int(i))

    for func in P:
        if func == 'R':
            R = not R
        else:
            if arr:
                if R:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                flag = not flag
                break
    if flag:
        if R:
            reverse_arr = reversed(arr)
            print('[', end='')
            print(*reverse_arr, sep=',', end=']')
            print()
        else:
            print('[', end='')
            print(*arr, sep=',', end=']')
            print()
    else:
        print('error')
