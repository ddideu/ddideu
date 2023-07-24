i = 1
while True:
    N = int(input())
    if N != 0:
        N *= 3
        if N % 2 == 0 :
            N /= 2
            N *= 3
            N //= 9
            print(f'{i}. even {int(N)}')
            i += 1
        else :
            N = (N+1)/2
            N *= 3 
            N //= 9
            print(f'{i}. odd {int(N)}')
            i += 1
    else :
        break