def DP_1(N, K):
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            kg = backpack[i][0]
            value = backpack[i][1]
            if j < kg:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(value + dp[i - 1][j-kg], dp[i-1][j])
    return dp[N][K]


N, K = map(int, input().split())
backpack = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())
    backpack.append([W, V])
ans = DP_1(N, K)
print(ans)