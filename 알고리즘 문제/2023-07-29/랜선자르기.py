import sys
K, N = map(int,sys.stdin.readline().split())
M = []
for i in range(K):
    M.append(int(sys.stdin.readline()))
    
for i in range(1,(max(M)+1)):
    S = 0
    for j in range(len(M)):
        S += M[j] // i
    if S < N:
        print(i-1)
        break
         


