card = int(input())
cardSelect = list(map(str,input().split()))
drop_card = {}
flag = 1
for i in range(card): # 카드 수 만큼 반복
    if cardSelect[i] not in drop_card: # 이 버린 패가 처음 버린거라면
        drop_card[cardSelect[i]] = 1 # 딕셔너리에 추가
    else: # 아니면
        drop_card[cardSelect[i]] += 1 # 카드 추가
        if drop_card[cardSelect[i]] == 5: # 근데 5장 버린게 확인 되면
            print(i + 1) # 이면 출력
            flag = 0
            break
if flag: # 이면 검사 통과시
    print(0) # 0 출력