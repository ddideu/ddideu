import sys
N, target = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
visited = [0] * (N+1)
for i in range(N):
    visited[i+1] = visited[i] + arr[i]

cnt = 0
l_p = 0
r_p = N
if visited[-1] >= target:
    while r_p < N+1 and l_p < N:
        if visited[r_p] - visited[l_p] >= target:
            cnt = r_p - l_p
            r_p -= 1
        else:
            l_p += 1
            r_p = l_p + cnt
            if r_p > N:
                r_p = N
print(cnt)
