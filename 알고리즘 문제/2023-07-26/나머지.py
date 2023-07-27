i = 1
N = []
while i<11:
    A = int(input())
    K = A % 42
    N.append(K)
    i +=1
A = set(N)
print(len(A))
