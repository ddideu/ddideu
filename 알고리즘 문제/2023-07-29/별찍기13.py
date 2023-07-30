N = int(input())
K = 2*N-1
for i in range(K):
    if i+1 <= N:
        print(+(1+i)*'*')
    else:
        print(((K-i)*'*'))