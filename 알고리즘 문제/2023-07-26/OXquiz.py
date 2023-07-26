import sys
N = int(sys.stdin.readline())
for i in range(N):
    A = str(sys.stdin.readline())
    count = 0
    count_sum = 0
    for J in A:
        if J == 'O':
            count += 1
            count_sum += count
        else:
            count = 0 
    print(count_sum)