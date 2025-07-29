Dp = [True] * 10001
Dp[0] = False
Dp[1] = False
for idx in range(2, 10001):
    if Dp[idx] == True :
        for next_idx in range(idx*2, 10001, idx):
            Dp[next_idx] = False

N = int(input())
for tc in range(N):
    gold = int(input())
    my_minus = 10000
    min_gold = 0
    max_gold = 0
    for i in range(2, gold):
        if Dp[i]:
            ins_gold = gold - i
            if Dp[ins_gold] and ins_gold >= i:
                min_gold = i
                max_gold = ins_gold
    print(min_gold, max_gold)
