import heapq


N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
distance = [1e9] * (N+1)
for _ in range(M):
    S, E, V = map(int,input().split())
    arr[S].append((E, V))

for Y in arr:
    Y.sort(key=lambda x: x[1])

start, end = map(int,input().split())
if start == end:
    print(0)
else:
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for n in arr[now]:
            next_node = n[0]
            cost = n[1]

            new_cost = dist + cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

    print(distance[end])