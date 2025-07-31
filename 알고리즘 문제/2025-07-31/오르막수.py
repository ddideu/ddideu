N = int(input())
dp = [[1]*10 for _ in range(N + 1)]

for idx in range(1, N+1):
    for num in range(8, -1, -1):
        dp[idx][num] = dp[idx-1][num] + dp[idx][num+1]
print(dp[-1][0])