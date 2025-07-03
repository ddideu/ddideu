subjects, myPoint = map(int,input().split()) # 내가 수강할 과목, 내 포인트
minPoint = [] #듣기 위한 최소 점수
mySubjects = 0 # 내가 이번학기 수강 과목
for _ in range(subjects): # 과목수만큼
    Person, subjectPerson = map(int, input().split()) # 현재 수강인원, 수강정원
    subjectPoint = list(map(int, input().split())) # 몇점씩 배팅?
    if Person < subjectPerson: # 수강인원이 수강정원보다 적다
        minPoint.append(1) # 1포인트만 배팅
    else: # 아니면
        subjectPoint.sort(reverse=True) # 높은순으로 정렬
        minPoint.append(subjectPoint[subjectPerson-1]) # 수강정원 순위번수에 있는 애만큼 배팅)
minPoint.sort() # 낮은순 정렬
for consumptionPoint in minPoint:
    if myPoint >= consumptionPoint:
        mySubjects += 1
        myPoint -= consumptionPoint
    else:
        break
print(mySubjects)