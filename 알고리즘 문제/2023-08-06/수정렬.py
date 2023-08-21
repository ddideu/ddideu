import sys

number_1 = int(sys.stdin.readline())
A_list = list(map(int,sys.stdin.readline().split()))
number_2 = int(sys.stdin.readline())
B_list = list(map(int,sys.stdin.readline().split()))

for k in range(len(A_list)):
    i = 0
    while i<len(B_li