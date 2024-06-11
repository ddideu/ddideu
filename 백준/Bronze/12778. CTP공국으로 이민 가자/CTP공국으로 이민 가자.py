alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
test = int(input())
for _ in range(test):
    number, select = map(str, input().split())
    if select == 'C':
        word = list(map(str, input(). split()))
        my_number = []
        for i in word:
            for j in range(len(alpha)):
                if i == alpha[j]:
                    my_number.append(j+1)
        print(*my_number)
    else:
        word = list(map(int, input().split()))
        my_alpha = []
        for i in word:
            my_alpha.append(alpha[i-1])
        print(*my_alpha)