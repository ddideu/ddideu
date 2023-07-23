list = []

for i in range(9):
    i = int(input())
    list.append(i) # list.append() =>리스트에다가 추가 하겠다.

print(max(list))
print(list.index(max(list))+1) 
#리스트에서 max 값에 해당하는 index 를 찾고 거기에 1을 더한다.          s