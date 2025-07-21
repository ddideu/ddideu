import heapq

pq = []
n = int(input())

for _ in range(n):
    numbers = map(int,input().split())
    for number in numbers:
        if len(pq) < n:
            heapq.heappush(pq, number)
        else:
            if pq[0] < number:# 힙큐에서 0 제일 앞의 값은 무조건 힙큐중 가장 작은 수이다.
                                # 즉 이문제는 너 최소힙 구현할줄 알아? 이문제와 같은거였다.
                                # 최소힙 관련 CS 정리 해야겠다.
                heapq.heappop(pq)
                heapq.heappush(pq, number)
print(pq[0])