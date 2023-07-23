import sys

N = int(input())
list = []
K = 1
for i in range(N):
    S = int(sys.stdin.readline())
    list.append(S)

frontstick = list[-1]

for i in reversed(range(N)):
    if list[i] > frontstick:
        K += 1
        frontstick = list[i]

print(K)
        # elif int(list[y]) > int(list[y+1]):
        # print(K)
# for j in range(N):
#     if list[j] >= list[j+1:]:
#         K += 1
#     else :
#         continue
# print(K)