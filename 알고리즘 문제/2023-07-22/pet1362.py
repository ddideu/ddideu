res = []

while True:
    Adequate_weight, real_weight = map(int,input().split())
    life_count = 1 #진짜 너때문에 참 고생 많이 했다... 야발.
    if Adequate_weight != 0 and real_weight != 0:
        while True:
            action, num = map(str,input().split())
            if action == 'E':
                real_weight -= int(num)
                if real_weight <= 0:
                    res.append("RIP")
                    life_count = 0 
                    continue
                     #이것때문에 한참을 고민했다. 문제에서는 이후 과정을 무시를 해야했는데 나는 바로 끝나버리는 break를 썻고.
                    # 이후 바로 continue로 바꾸기는 했지만 해당 상태가 바뀐다는 점때문에 어떻게 처리해야하는지 고민을 많이 했다.
            if action == '#' and num == '0':
                if life_count == 0 : #체중의 상태가 변하더라도 답을 찾아 냈다. 아싸.
                    break
                elif Adequate_weight/2 < real_weight < Adequate_weight*2 :
                    res.append(':-)')
                    break
                else:
                    res.append(':-(') # 바로 출력 되는 형식으로 프린트문을 썻는데 그래서는 안됐기에 append함수를 이용하였다.
                    break
            if action == 'F':
                real_weight += int(num)
    else:
        break
         
# for i, v in enumerate(res): 
#     # enumerate라는 함수가 인덱스와 리스트 안의 요소를 담아주는 튜플의 형식으로 묶어 준다는 것을 알게 됐다
#     # 이거 찾으려고 한참을 생각하다가 구글링 해서 바로 알아 냈을때는...  
#     print(i+1, v)

K = 1
for i in res:
    print(K, i)
    K += 1
