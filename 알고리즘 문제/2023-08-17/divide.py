num = list(map(str,input()))
N_num = ''
for i in range(len(num)-2):
    N_num = N_num + num[i]
divine = int(input())

for i in range(9,-1,-1):
    S = N_num
    S = S + str(i)
    for j in range(9,-1,-1):
        T = S
        T = T + str(j)
        if int(T) % divine == 0:
            U = str(i)+str(j)

print(U)