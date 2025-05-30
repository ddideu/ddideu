def contiune_game(total_game, win):
    percent = int(win * 100/ total_game)
    ans = 1000000001
    next_game = 0
    end_game = 1000000001
    while next_game < end_game:
        play_game = (next_game + end_game) // 2
        now_percent = int(((win + play_game)* 100)/(total_game + play_game))
        if now_percent > percent:
            end_game = play_game
            ans = play_game
        else:
            next_game = play_game + 1
    return ans



# 여기서 X는 현재 까지 한 게임 수 Y는 이긴 횟수
X, Y = map(float,input().split())
ans = contiune_game(X, Y)
if ans != 1000000001:
    print(ans)
else:
    print(-1)

