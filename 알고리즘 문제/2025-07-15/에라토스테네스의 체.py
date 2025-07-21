import sys

while True:
    N = int(sys.stdin.readline())
    if N != 0:
        for i in range(3, N//2 + 1):
            b = N - i
            end = int(b ** (1/2))
            print(b)
            print(end)
            flag = 1
            for j in range(2, end):
                if b % j == 0:
                    flag = 0
                    break
            if flag:
                print(f'{N} = {i} + {b}')
                break
        else:
            print("Goldbach's conjecture is wrong.")
    else:
        break