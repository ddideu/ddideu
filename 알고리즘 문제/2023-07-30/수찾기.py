import sys
input = sys.stdin.readline

A = int(input())
A_1 = list(map(int,input().split()))
A_1.sort()

B = int(input())
B_1 = list(map(int,input().split()))


C =[]
for i in A_1:
    B_1.find(i)
