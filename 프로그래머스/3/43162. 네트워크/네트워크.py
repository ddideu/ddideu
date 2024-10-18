from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0] * (n)
    queue = deque()
    for i in range(n):
        if visited[i] == 0:
            queue.append(i)
            answer += 1
            while queue:
                start = queue.popleft()
                visited[start] = 1
                for idx in range(n):
                    if visited[idx] == 0 and computers[start][idx] == 1:
                        queue.append(idx)
    return answer