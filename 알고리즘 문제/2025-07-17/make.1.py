def make_one(MAX):
    for i in range(2, MAX+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i],dp[i//2]+1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)



N = int(input())
dp = [0] * (N+1)
dp[0] = 0
dp[1] = 0
if N >= 2:
    dp[2] = 1
if N >= 3:
    dp[3] = 1

make_one(N)
print(dp[-1])