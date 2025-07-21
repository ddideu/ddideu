import sys
N, target = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
visited = [0] * (N+1)
for i in range(1, N+1):
    visited[i] = visited[i-1] + arr[i-1]
print(visited)
cnt = 100001
l_p = 0
r_p = N
while l_p < r_p:
    cumulative_sum = visited[r_p] - visited[l_p]
    cumulative_num = r_p - l_p
    if cumulative_sum >= target:
        cnt = min(cumulative_num, cnt)
        r_p -= 1
    else:
        l_p += 1
        r_p = N

if cnt == -1:
    print(0)
else:
    print(cnt)