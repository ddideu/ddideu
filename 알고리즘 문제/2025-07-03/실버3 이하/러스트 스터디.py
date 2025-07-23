day = int(input())
studyPlan = list(map(int,input().split()))
realStudy = list(map(int,input().split()))
cnt = 0
for i in range(day):
    if realStudy[i] >= studyPlan[i]:
        cnt += 1
print(cnt)