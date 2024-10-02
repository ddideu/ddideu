from collections import deque
N = int(input())
score = 0
subjects = []
queue = deque()
for _ in range(N):
    subjects.append(list(map(int, input().split())))

for idx in range(N):
    if subjects[idx][0]:
        subjects[idx][2] = subjects[idx][2] - 1
        if subjects[idx][2] == 0:
            score += subjects[idx][1]
        else:
            queue.append(idx)
    if queue and subjects[idx][0] == 0:
        now = queue.pop()
        subjects[now][2] = subjects[now][2] - 1
        if subjects[now][2] == 0:
            score += subjects[now][1]
        else:
            queue.append(now)
print(score)