N = int(input())
card_stack = []
card_duplication = {}
for i in range(N):
    New_card = int(input())
    card_stack.append(New_card)
for i in card_stack:
    if i in card_duplication:
        card_duplication[i] += 1
    else :
        card_duplication[i] = 1
# for i in card_duplication:

# duplication_number = list(card_duplication.values())
# duplication_num = list(card_duplication.keys())
# max = duplication_number[0]
# for K in duplication_number:
#     if max >= duplication_number[K]:
#         max = max
#     else :
#         max = duplication_number[K]

 
