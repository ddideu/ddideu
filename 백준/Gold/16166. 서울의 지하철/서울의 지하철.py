from collections import deque
def BFS (Q,NUM):
    next_Q = deque()
    while Q:
        start_point = Q.popleft()
        if start_point == final_station:
            return NUM
        for next_time in arr[start_point]:
            if next_time not in visited:
                visited.append(next_time)
                next_Q.append(next_time)
    if next_Q:
        return BFS(next_Q, NUM+1)
    else:
        return -1


start = int(input())
visited = []
subways = []
finish_station = 0
for line in range(start):
    hosun = list(map(int, input().split()))
    stations = hosun[1:]
    my_station = deque()
    for station in range(len(stations)):
        for next_stations in range(station, len(stations)):
            my_station.append([stations[station], stations[next_stations]])
        if stations[station] > finish_station:
            finish_station = stations[station]
    subways.append(my_station)

final_station = int(input())

arr = {}

for subway in range(len(subways)):
    for next_station in subways[subway]:
        a, b = next_station[0], next_station[1]
        if a in arr and b not in arr[a]:
            arr[a].extend([b])
        else:
            if a not in arr:
                arr[a] = [b]
        if b in arr and a not in arr[b]:
            arr[b].extend([a])
        else:
            if b not in arr:
                arr[b] = [a]
queue = deque()
for my in arr[0]:
    queue.append(my)
cnt = BFS(queue, 0)
print(cnt)