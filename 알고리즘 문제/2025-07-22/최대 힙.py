import heapq
import sys
Number = int(sys.stdin.readline())
pq = []

for _ in range(Number):
    natural = int(sys.stdin.readline())
    if natural == 0:
        if pq:
            print(-heapq.heappop(pq))
        else:
            print(0)
    else:
        minus = -natural
        heapq.heappush(pq, minus)