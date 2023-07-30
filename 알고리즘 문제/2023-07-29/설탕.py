import sys
N = int(sys.stdin.readline())
K = N//5
C = 0
if (N==4)or(N==7):
    print(-1)
elif N%5 == 0 :
    print(K)
elif N%5 == 1:
    K -= 1
    C += 2
    print(K+C)
elif N%5 == 2:
    K -= 2
    C += 4
    print(K+C)
elif N%5 == 3:
    C += 1
    print(K+C) 
else:
    K -= 1
    C += 3
    print(K+C)
