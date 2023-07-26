K = int(input())
for i in range(K):
    P, M = map(int,input().split())
    B = []
    C_count = 0
    for j in range(P):
        A = int(input())
        B.append(A)
    
    for k in range(1, M+1):
        if B.count(k) >= 2:
            C_count += B.count(k) - 1
    
    print(C_count)
    