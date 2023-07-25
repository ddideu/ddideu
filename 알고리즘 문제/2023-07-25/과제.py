A_list = []
for i in range(28):
    A = int(input())
    A_list.append(A)

for i in range(30):
    B = i + 1
    Count = A_list.count(B)
    if Count == 0:
        print(B) 
