# pairsum.py
N = int(input())
for i in range(N):
    pair = int(input())
    A = []
    B = []
    if pair =< 3:
        if pair == 3:
            print(f'Pairs for {pair}: 1 2')
        if pair < 3:
            print(f'Pairs for {pair}: ') 
    else:
        for i in range(0, pair//2):
            A.append(i)
        for i in range(2, pair):
            B.append(i)
    # (A + B = pair) and A<B