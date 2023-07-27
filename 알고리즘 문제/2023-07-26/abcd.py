import sys
n = int(sys.stdin.readline())
card_dict = {}
for i in range(n):
    card =int(sys.stdin.readline())
    if card in card_dict:
       card_dict[card] += 1
    else:
        card_dict[card] = 1
# print(card_dict)
result ={}
#value값기준 key 값 정렬
result = sorted(card_dict.items(), key = lambda x:x[1], reverse=True) # 음수 2개가 동시 출연 하는 순간 반례가 나와버린다.
# print(result)
print(result[0][0])