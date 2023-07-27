import sys
N, M = map(int,sys.stdin.readline().split())
K = list(map(int,sys.stdin.readline().split()))
K.sort()

count = 0

for h in K:
    for i in K:
        for j in K:
            if (h == i) or (h == j) or (i == j):
                continue
            else:
                if count < h+i+j < M:
                    count = h+i+j

print (count)
