import sys
N = int(sys.stdin.readline())
card_stack = []
card_duplication = {}
for i in range(N):
    New_card = int(sys.stdin.readline())
    card_stack.append(New_card)

for i in card_stack:
    if i in card_duplication:
        card_duplication[i] += 1 #해당하는 카드가 있다면 생성된 값에 +1
    else :
        card_duplication[i] = 1 #해당하는 카드가 없다면 새로 생성

duplication_value = list(card_duplication.values()) #해당 인덱스에 해당하는 카드가 몇번 나왔는지 해당하는 변수
duplication_key = list(card_duplication.keys()) #해당 인덱스에 해당하는 카드의 숫자.
top_card = 2**62
top_card_N = 0
for i in range(0,(len(duplication_value))):
    if duplication_value[i] > top_card_N:
        top_card_N = duplication_value[i]
        top_card = duplication_key[i]
    if duplication_value[i] == top_card_N:
        if duplication_key[i] > top_card:
            continue
        else:
            top_card_N = duplication_value[i]
            top_card = duplication_key[i]
    
print(top_card)

# for i in range(len(duplication_value)):
#     for j in range(len(duplication_value)):
#         if duplication_value[i] > duplication_value[j]:
#             if j>i:
#                 top_card = duplication_key[i]
#                 print(top_card)
#             else:
#                 continue
#         if duplication_value[i] == duplication_value[j]:
#             if i == j :
#                 continue
#             else:
#                 top_card > duplication_key[j]
#                 top_card = duplication_key[i]
#                 print


            


        

# for i in card_duplication:

# duplication_number = list(card_duplication.values())
# duplication_num = list(card_duplication.keys())
# max = duplication_number[0]
# for K in duplication_number:
#     if max >= duplication_number[K]:
#         max = max
#     else :
#         max = duplication_number[K]

 
