c,d,e,f,g,a,b,C = map(int,input().split())
A_list = [c,d,e,f,g,a,b,C]
B_list = A_list[:]
B_list.sort()
C_list = B_list[::-1]
if A_list == B_list:
    print('ascending')
elif A_list == C_list:
    print('descending')
else:
    print('mixed')