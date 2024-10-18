#다익스트라 연습
import heapq
N, M = map(int, input().split())
distance = [1e9] * (N+1)
edge = [[] for _ in range(N+1)]
for _ in range(M):
    start, finish, cost = map(int,input().split())
    edge[start].append([finish, cost])
    edge[finish].append([start, cost])

pq = []
# pq, (비용, 출발점)
heapq.heappush(pq, (0, 1))
while pq:
    now_cost, start = heapq.heappop(pq)

    if distance[start] < now_cost:
        continue

    for next_point, cost in edge[start]:
        new_cost = cost + now_cost

        if distance[next_point] <= new_cost:
            continue

        distance[next_point] = new_cost
        heapq.heappush(pq, (new_cost, next_point))
print(distance[N])