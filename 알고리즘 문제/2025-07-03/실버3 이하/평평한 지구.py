testCase = int(input())
for tc in range(testCase):
    area, moveTime = map(int,input().split())
    if moveTime < area:
        myArea = (area*2) * (area+1) - ((area - moveTime - 1) * 2) * (area - moveTime)
    else:
        myArea = (area * 2) * (area + 1)
    print(myArea)
