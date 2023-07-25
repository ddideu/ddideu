import sys
N = int(sys.stdin.readline())
card_stack = []
card_duplication = {}
for i in range(N):
    New_card = int(sys.stdin.readline())
    card_stack.append(New_card)

for i in card_stack:
    card_duplication[i] = card_duplication.get(i, 0) + 1
    # if i in card_duplication:
    #     card_duplication[i] += 1 #해당하는 카드가 있다면 생성된 값에 +1
    # else :
    #     card_duplication[i] = 1 #해당하는 카드가 없다면 새로 생성

duplication_value = list(card_duplication.values()) #해당 인덱스에 해당하는 카드가 몇번 나왔는지 해당하는 변수
duplication_key = list(card_duplication.keys()) #해당 인덱스에 해당하는 카드의 숫자.
top_card = 2**62
top_card_N = 0
for i in range(0,(len(duplication_value))):
    if duplication_value[i] > top_card_N: #가장 많이 나온 횟수보다 많다면
        top_card_N = duplication_value[i] # 해당 카드로 가장 많이 나온 횟수 변화
        top_card = duplication_key[i] # 해당 카드 숫자로 변화
    if duplication_value[i] == top_card_N:
        if duplication_key[i] > top_card: # 해당카드가 탑카드보다 클시
            continue #무시하고 진행
        else: # 그 이외의 경우는
            top_card_N = duplication_value[i] # 해당 카드로 가장 많이 나온 횟수 변화
            top_card = duplication_key[i] # 해당 카드 숫자로 변화
    
print(top_card) 