N = int(input())
A_list = []
B_list = []
for i in range(N):
    A, B = map(str,input().split())
    A_list.append(A)
    B_list.append(int(B))
C_1 = 00000
C = 5
for i in range(N):
    if C > B_list[i]:
        C = B_list[i]
        C_1 = A_list[i]

print(C_1)

