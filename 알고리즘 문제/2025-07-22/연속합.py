N = int(input())
sub_sums = list(map(int,input().split()))
dp = [0] * N
dp[0] = sub_sums[0]
for i in range(1, N):
    dp[i] = max(sub_sums[i], sub_sums[i] + dp[i-1]) #현재 배열의 숫자와, 이전 까지의 합과 현재 배열의 숫자중 더 큰게 뭐야? 
print(max(dp))