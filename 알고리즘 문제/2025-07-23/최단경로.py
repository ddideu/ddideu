import heapq, sys
node, line = map(int, sys.stdin.readline().split())
arrs = [[] for _ in range(node + 1)]
start_point = int(sys.stdin.readline())
distance = [1e9] * (node + 1)

for _ in range(line):
    S, E, W = map(int, sys.stdin.readline().split())
    arrs[S].append([E, W])

for arr in arrs:
    arr.sort(key=lambda x: x[1])

pq = []
heapq.heappush(pq, [0, start_point])
distance[start_point] = 0
while pq:
    dist, now = heapq.heappop(pq)
    if distance[now] < dist:
        continue
    for n in arrs[now]:
        next_node = n[0]
        cost = n[1]

        new_cost = cost + dist

        if distance[next_node] <= new_cost:
            continue

        distance[next_node] = new_cost
        heapq.heappush(pq, [new_cost, next_node])

for idx in distance[1:]:
    if idx == 1e9:
        print('INF')
    else:
        print(idx)


