N = int(input())
dp = [0] * (N+1)
cards = list(map(int,input().split()))
dp[1] = cards[0]
if N >= 2:
    for i in range(2, N+1):
        for idx in range(i-1, -1, -1):
            dp[i] = max(dp[i], dp[i-idx-1] + cards[idx])
print(dp[-1])