N = int(input())
X_1 = []
Y_1 = []
for i in range(N):
    X, Y = map(int,input().split())
    X_1.append(X)
    Y_1.append(Y)
    
A = list(zip(X_1,Y_1))
A.sort()
for i in range(N):
    print(*(A[i]))