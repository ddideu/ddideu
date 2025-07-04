def split_candy(START, FINISH, SCORES, MONEY):
    real_score = 0
    while START < FINISH:
        middle = (START + FINISH) // 2
        my_candy = 0
        for score in SCORES:
            if score > middle:
                my_candy += score - middle
        if MONEY < my_candy:
            START = middle + 1
        else:
            FINISH = middle
    return START


people, money = map(int,input().split())
scores = list(map(int, input().split()))
mycandy = split_candy(0, max(scores), scores, money)
print(mycandy)