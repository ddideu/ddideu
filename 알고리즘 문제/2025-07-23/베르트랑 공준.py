import sys
from math import sqrt

def prime_num(num, Arr):
    if Arr[num] != 0:
        return Arr[num]
    my_prime = int(sqrt(num)) + 1
    flag = 1
    for idx in range(2, my_prime):
        if num % idx == 0:
            return Arr[num - 1]
    return Arr[num-1] + 1

arr = [0] * (123456 * 2 + 1)
arr[2] = 1
arr[3] = 2
while True:
    N = int(sys.stdin.readline())
    if N:
        N2 = N*2
        cnt = 0
        for i in range(2, N2+1):
            arr[i] = prime_num(i, arr)
        print(arr[N2] - arr[N])
    else:
        break