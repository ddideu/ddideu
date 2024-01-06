from collections import deque

go = [1, -1, 2]
A, B = map(int, input().split())
if A > B:
    print(A-B)
else:
    visited = [-1 for _ in range(B*2)]
    queue = deque()
    queue.append(A)
    visited[A] = 0
    while queue:
        now = queue.popleft()
        for i in go:
            if i == 2 and now < B:
                next_place = now * 2
                if visited[next_place] == -1:
                    visited[next_place] = visited[now]
                    queue.append(next_place)
                else:
                    com_a = visited[now]
                    com_b = visited[next_place]
                    if visited[now] < visited[next_place]:
                        visited[next_place] = visited[now]
                        queue.append(next_place)
            elif i != 2:
                next_place = now + i
                if 0 <= next_place < B*2:
                    if visited[next_place] == -1:
                        visited[next_place] = visited[now] + 1
                        queue.append(next_place)
                    else:
                        if visited[now] + 1 < visited[next_place]:
                            visited[next_place] = visited[now] + 1
                            queue.append(next_place)
    print(visited[B])