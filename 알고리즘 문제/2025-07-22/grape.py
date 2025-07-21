N = int(input())
dp = [0] * (N+1)
arr = []
for _ in range(N):
    arr.append(int(input()))
dp[1] = arr[0]
if N >= 2:
    dp[2] = dp[1] + arr[1]
for idx in range(2, N):
    # 경우의 수 1. 나 이번턴 쉴래. 2. 나 바로 직전에 안마셨으니까 이번에 한잔 마실래, 3. 나 2턴전에 안마셨으니까. 이번턴에 2잔 마실래
    dp[idx + 1] = max(dp[idx], dp[idx-1] + arr[idx], dp[idx-2] + arr[idx-1] + arr[idx])
print(dp)
