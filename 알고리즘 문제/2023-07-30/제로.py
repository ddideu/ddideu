A = int(input())
A_1=[]
for i in range(A):
    B = int(input())
    if B != 0:
        A_1.append(B)
    else:
        A_1.pop()

print(sum(A_1))