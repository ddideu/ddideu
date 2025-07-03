from collections import deque
student = int(input()) # 학생수 홀수 보장
students = deque() # 학생 정보 저장
for _ in range(student): # 학생 정보 저장 과정
    initial, num = map(str, input(). split())
    students.append([initial, int(num)])

while True:
    now_initial, myNumber = students.popleft()
    if students: # 남아있는 학생이 있다면
        myNumber -= 1
        while myNumber:
            partner, partnerNumber= students.popleft()
            students.append([partner, partnerNumber])
            myNumber -= 1
        partner, partnerNumber = students.popleft()
    else: # 없으면 한양이와 팀원이다. 축하한다.
        print(now_initial)
        break
