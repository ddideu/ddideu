while True:
    N = str(input())
    R_N = " "
    if N == '0':
        break
    else :
        for i in N:
            R_N = i + R_N
    if int(R_N) == int(N):
        print('yes')
    else :
        print('no')
