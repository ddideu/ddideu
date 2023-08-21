import sys
A, B = map(int, sys.stdin.readline().split())
Max_split = 1
for i in range(1,(min(A, B)+1)):
    if A % i == 0 and B % i == 0:
        Max_split = i
print(Max_split)
C = A // Max_split
D = B // Max_split
print(C*D*Max_split)