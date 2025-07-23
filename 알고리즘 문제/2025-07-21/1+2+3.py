test = int(input())
for _ in range(test):
    number = int(input())
    dp = [0] * (number + 1)
    if number >= 1:
        dp[1] = 1
    if number >= 2:
        dp[2] = 2
    if number >= 3:
        dp[3] = 4
    for i in range(4, number+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[-1])