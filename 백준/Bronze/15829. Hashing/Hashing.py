import sys
alpha = 'abcdefghijklmnopqrstuvwxyz'
N = int(sys.stdin.readline())
A = list(map(str, sys.stdin.readline().strip()))
B = 0
C = 0
for i in A:
    C += (alpha.index(i)+1) * (31**B)
    B += 1
print(C)