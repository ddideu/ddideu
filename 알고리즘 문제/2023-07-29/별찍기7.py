N = int(input())
K = 2*N-1
for i in range(K):
    if i+1 <= N:
        print((N-1-i)*' '+ (2*i+1)*'*')
    else:
        print(((i-N+1)*' ') + ((2*(K-i)-1) * '*'))