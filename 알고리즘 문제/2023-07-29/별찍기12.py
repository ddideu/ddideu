N = int(input())
K = 2*N-1
for i in range(K):
    if i+1 <= N:
        print(((N-i-1))*' '+(1+i)*'*')
    else:
        print((((i-N+1)) * ' ') + ((K-i)*'*'))