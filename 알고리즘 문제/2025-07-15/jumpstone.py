from collections import deque
N = int(input())
roads = list(map(int,input().split()))
visited = [1 for _ in range(N)]
my_loc = int(input()) - 1
queue = deque()
queue.append(my_loc)
ans = 0
while queue:
    now_loc = queue.popleft()
    visited[now_loc] = 0
    ans += 1
    if now_loc - roads[now_loc] >= 0 and visited[now_loc - roads[now_loc]]:
        visited[now_loc - roads[now_loc]] = 0
        queue.append(now_loc - roads[now_loc])
    if now_loc + roads[now_loc] < N and visited[now_loc + roads[now_loc]]:
        visited[now_loc + roads[now_loc]] = 0
        queue.append(now_loc + roads[now_loc])
print(ans)

