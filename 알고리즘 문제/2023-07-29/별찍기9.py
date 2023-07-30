N = int(input())
K = 2*N-1
for i in range(K):
    if i+1 <= N:
        print((i)*' ' + ((K-2*i)*'*'))
    else:
        print(((K-i-1)*' ') + (2*(i-N+1)+1) *'*')