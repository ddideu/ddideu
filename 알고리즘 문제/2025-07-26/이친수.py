num = int(input())
dp = [0] * (num + 1)
dp[1] = 1
if num >= 2:
    for idx in range(1,num):
        dp[idx+1] = dp[idx] + dp[idx-1]
print(dp[-1])