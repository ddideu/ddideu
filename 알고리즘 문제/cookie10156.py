K, N, M = map(int,input().split())
Multi = K * N
if M < Multi:
    print(Multi-M)
else:
    print(0)