K = int(input())
L = list(map(int,input().split()))
L.sort()
M = L[0]*L[K-1]
print(M)