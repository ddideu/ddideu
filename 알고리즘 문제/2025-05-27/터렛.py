import math

N = int(input())

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # sqrt => 루트!
    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if dis == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) == dis or r1 + r2 == dis:
        print(1)
    elif abs(r1-r2) < dis < abs(r1+r2):
        print(2)
    else:
        print(0)