T = int(input())

for i in range (T):
    P = int(input())
    P_N = [1,1,1,2,2]
    for i in range (P):
        if i<=4:
            continue
        else :
            S =  P_N[i-5]+P_N[i-1]
            P_N.append(S)
    
    print(P_N[-1])
