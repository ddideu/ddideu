def divine(S, E, GAME, WIN, POINT):
    middle = (S+E)//2
    MY_POINT = int((WIN+middle)/ (GAME + middle) * 100)
    if MY_POINT == POINT:
        return divine(middle + 1, E, GAME, WIN, POINT)
    else:
        return divine(S, middle-1, GAME, WIN, POINT)


X, Y = map(int, input().split())
Z = int(Y / X * 100)
start = 0
finish = 1000000001
if finish:
    game = divine(start, finish, X, Y, Z)
else:
    print(0)
