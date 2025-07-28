import heapq
import sys
N = int(sys.stdin.readline())
minus_pq = []
plus_pq = []
for _ in range(N):
    number = int(sys.stdin.readline())
    if number != 0:
        if number < 0:
            minus_number = -number
            heapq.heappush(minus_pq, minus_number)
        else:
            heapq.heappush(plus_pq, number)
    else:
        m_number = 0
        p_number = 0
        if minus_pq:
            m_number = heapq.heappop(minus_pq)
        if plus_pq:
            p_number = heapq.heappop(plus_pq)
        if m_number != 0 or p_number != 0:
            if m_number == 0:
                print(p_number)
            elif p_number == 0:
                print(-m_number)
            elif m_number > p_number:
                print(p_number)
                heapq.heappush(minus_pq, m_number)
            elif m_number < p_number:
                print(-m_number)
                heapq.heappush(plus_pq, p_number)
            else:
                print(-m_number)
                heapq.heappush(plus_pq, p_number)
        else:
            print(0)
