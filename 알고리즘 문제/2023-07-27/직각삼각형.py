while True:
    A, B, C = map(int,input().split())
    D = A**2+B**2-C**2
    E = A**2-B**2+C**2
    F = -A**2+B**2+C**2
    if A == 0 and B == 0 and C == 0 :
        break
    else:
        if D*E*F == 0:
            print('right')
        else:
            print('wrong')
