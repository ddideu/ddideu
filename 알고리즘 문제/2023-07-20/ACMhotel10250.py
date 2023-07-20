T = int(input())
for i in range(T):
    H, W, A = map(int,input().split())
    X = 1
    Y = 0
    if A % H == 0:
        Y += H
    else :
        Y = A % H
    while A > H :
         A -= H
         X += 1
    if X <= 9:
        print(str(Y)+'0'+str(X))
    else :
        print(str(Y)+str(X))


