N = int(input())
L = list(map(int,input().split()))
M = max(L)
fake_grade = 0
for i in L:
    fake_grade += (i/M) * 100

print(round(fake_grade/len(L),3))