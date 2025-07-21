from collections import deque
target, targetNum = map(int,input().split()) # 초기 타겟수, 타겟 제거수(추가 타겟)
nowX,nowY = 0, 0 # 초기 위치
now_target = [] # 초기 타겟 위치
next_target = deque() #다음 타겟 위치
totalScore = 0 # 총 점수
for _ in range(target):
    now_target.append(list(map(int, input().split())))
for _ in range(targetNum):
    next_target.append(list(map(int, input().split())))

for _ in range(targetNum):
    myScore = 0
    now_idx = 0
    for i in range(target):
        if myScore < (abs(now_target[i][0] - nowX) ** 2 + abs(now_target[i][1]- nowY) ** 2):
            now_idx = i
            myScore = (abs(now_target[i][0] - nowX) ** 2 + abs(now_target[i][1]- nowY) ** 2)
    totalScore += myScore
    nowX, nowY= now_target.pop(now_idx)
    now_target.append(next_target.popleft())
print(totalScore)
