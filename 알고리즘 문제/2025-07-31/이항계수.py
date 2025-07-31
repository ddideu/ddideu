N, K = map(int,input().split())
dp = [[1] * (i+1) for i in range(N+1)]
if N > 1:
    for idx in range(2, N+1):
        for number in range(1,idx):
            dp[idx][number] = dp[idx-1][number-1] + dp[idx-1][number]
print(dp[-1][K] % 10007)
