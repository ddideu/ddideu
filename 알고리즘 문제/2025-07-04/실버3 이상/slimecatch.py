def my_Lv(Start, Finish, Point): #이분 탐색
    while Start < Finish:
        middle = (Start + Finish) // 2
        exp_point = (middle**2) + middle # 짝수 합 (짝수 갯수의 제곱) + 짝수 갯수
        if Point >= exp_point:
            Start = middle + 1
        else:
            Finish = middle
    return Start

test = int(input())
for tc in range(test):
    slime = int(input())
    myExp = 0
    if slime != 1: # 모든 자연수의 합 공식  n *( n+1) // 2
        myExp = slime * (slime + 1) // 2
    else:
        myExp = 1
    print(my_Lv(1, slime, myExp))
