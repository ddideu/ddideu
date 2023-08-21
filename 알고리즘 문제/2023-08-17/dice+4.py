test = int(input())
total = 0
for tc in range(test):
    dice = list(map(int, input().split()))
    stage = 0
    double_count_number = []
    snake_eye = []
    double_count = 0
    for i in range(1,7):
        if 4 == dice.count(i):
            stage = 50000 + (i * 5000)
            break
        elif 3 == dice.count(i):
            stage = 10000 + (i * 1000)
            break
        elif 2 == dice.count(i):
            double_count += 1
            double_count_number.append(i)
            if double_count == 2:
                break
        elif 1 == dice.count(i):
            snake_eye.append(i)

    if double_count == 2:
        stage = 2000 + int(double_count_number[0]) * 500 + int(double_count_number[1]) * 500
    elif double_count == 1:
        stage = 1000 + int(double_count_number[0]) * 100

    if len(snake_eye) == 4:
       stage = max(snake_eye) * 100

    if stage > total:
        total = stage
print(total)
