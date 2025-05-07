N, M = map(int,input().split())
eyfa_check = []
flag = 1
for _ in range(N):
    ins = str(input())
    now_eyfa = ""
    for word in ins:
        now_eyfa += word*2
    eyfa_check.append(now_eyfa)

for i in range(N):
    check = str(input())
    if eyfa_check[i] != check:
        flag = 0
        break

if flag:
    print('Eyfa')
else:
    print('Not Eyfa')