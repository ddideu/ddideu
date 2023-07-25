A_list = []

for i in range(8):
    A = int(input())
    # 문제 점수 리스트 생성
    A_list.append(A)  

C_list = []
score = 0
for i in range(5):
    score += max(A_list)
    C_list.append(A_list.index(max(A_list))+1)
    A_list[A_list.index(max(A_list))] = -1
C_list.sort()
print(score)
print(*C_list)