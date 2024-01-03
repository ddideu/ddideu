num = int(input())
arr = list(map(int, input().split()))
dp = [0] * (num + 1)
for i in range(num):
    now = arr[i]
    cnt = 1
    dp[i+1] = cnt
    for j in range(i+1):
        if arr[j] < now:
            dp[i+1] = max(dp[j+1] + cnt, dp[i+1])
print(max(dp))