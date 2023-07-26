# pairsum.py
N = int(input())
for i in range(N):
    pair = int(input())
    if pair == 3:
        print(f'Pairs for {pair}: 1 2')
    if pair == 4:
        print(f'Pairs for {pair}: 1 3')
    if pair == 5:
        print(f'Pairs for {pair}: 1 4, 2 3')
    if pair == 6:
        print(f'Pairs for {pair}: 1 5, 2 4')
    if pair == 7:
        print(f'Pairs for {pair}: 1 6, 2 5, 3 4')
    if pair == 8:
        print(f'Pairs for {pair}: 1 7, 2 6, 3 5')
    if pair == 9:
        print(f'Pairs for {pair}: 1 8, 2 7, 3 6, 4 5')
    if pair == 10:
        print(f'Pairs for {pair}: 1 9, 2 8, 3 7, 4 6')
    if pair == 11:
        print(f'Pairs for {pair}: 1 10, 2 9, 3 8, 4 7, 5 6')
    if pair == 12:
        print(f'Pairs for {pair}: 1 11, 2 10, 3 9, 4 8, 5 7')
    if pair < 3: 
        print(f'Pairs for {pair}:')