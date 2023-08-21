N = int(input())
K_2 = 0
K_5 = 0
if N%5 == 1:
    if N == 1:
        print(-1)
    else:
        K_2 = 3
        K_5 = (N-6) // 5
        print(K_2+K_5)
elif N%5 == 2:
    K_2 = 1
    K_5 = N // 5
    print(K_2+K_5)
elif N%5 == 3:
    if N == 3:
        print(-1)
    else:
        K_2 = 4
        K_5 = (N - 8) // 5
        print(K_2 + K_5)
elif N%5 == 4:
    K_2 = 2
    K_5 = N // 5
    print(K_2+K_5)
else:
    print(N//5)