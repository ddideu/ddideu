import heapq


def MIN_RUPEE(NOW):
    pq = []
    heapq.heappush(pq, (NOW, 0, 0))

    while pq:
        real, row, col = heapq.heappop(pq)

        if visited[row][col] < real:
            continue

        for dy, dx in delta:
            nx = col + dx
            ny = row + dy
            if 0 <= nx < N and 0 <= ny < N:
                cost = arr[ny][nx]
                new_cost = real + cost
                if visited[ny][nx] <= new_cost:
                    continue

                visited[ny][nx] = new_cost
                heapq.heappush(pq, (new_cost, ny, nx))



test = 1
delta = [[0, 1], [-1, 0], [0, -1], [1, 0]]
while True:
    N = int(input())
    min_rupee = 10 * (N * N)
    if N != 0:
        arr = [list(map(int, input().split())) for _ in range(N)]
        INF = int(1e9)
        visited = [[INF]*N for _ in range(N)]
        now = arr[0][0]
        MIN_RUPEE(now)
        print(f'Problem {test}: {visited[N-1][N-1]}')
        test += 1
    else:
        break