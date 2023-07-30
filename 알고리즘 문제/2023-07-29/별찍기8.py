N = int(input())
K = 2*N-1
for i in range(K):
    if i+1 <= N:
        print((1+i)*'*'+ (2*(N-i-1))*' '+(1+i)*'*')
    else:
        print(((K-i)*'*') + ((2*(i-N+1)) * ' ') + ((K-i)*'*'))