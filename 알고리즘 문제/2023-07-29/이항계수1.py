N, K = map(int,input().split())
Sum_N = 1
Sum_K = 1
if K == 0:
    print(1)
else:
    for i in range(K):
        Sum_N *= N
        Sum_K *= K
        N -= 1
        K -= 1
    print(int(Sum_N/Sum_K))