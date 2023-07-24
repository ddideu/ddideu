import sys
A, B = sorted(map(int,sys.stdin.readline().split()))
if A == B:
    print(0)
    print(" ")
else:
    print((B-A-1))
    for i in range(abs(B-A-1)):
        print(A+i+1, end=" ")
