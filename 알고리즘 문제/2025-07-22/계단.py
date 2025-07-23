# 포도 문제와 비슷하지만 문제는 포도의 경우는 마지막은 안마셔도 되지만 이는 마셔야 한다. 주의할것.
# 그러면. 반대로 내려가는 식으로 해보자. 어짜피 마지막은 0이니까 괜찮지 않아?
N = int(input())
arr = []
dp = [0] * (N+1)
for _ in range(N):
    arr.append(int(input()))
dp[1] = arr[0]
if N >= 2:
    dp[2] = dp[1] + arr[1]
    # 2계단 전에서 2칸 올라온거. 3계단 전에서 2칸 뛰고 1칸 더 올라온거 값
if N >= 3:
    dp[3] = max(dp[1] + arr[2], dp[0] + arr[1] + arr[2])
for idx in range(3, N):
    # 경우의 수 1. 한칸만 올라갈 경우 2. 한번에 2칸 오르고 2칸을 한번씩 올라갈때
    dp[idx + 1] = max(dp[idx-1] + arr[idx], dp[idx-2] + arr[idx-1] + arr[idx])
print(dp[-1])