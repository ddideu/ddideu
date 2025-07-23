day = int(input())
for _ in range(day):
    year, month = map(int, input().split())
    if month == 3:
        if year % 4 or year == 2100:
            print(year, month-1, 28)
        else:
            print(year, month-1, 29)
    else:
        if month == 1:
            print(year-1, 12, 31)
        else:
            if month not in [3, 5, 7, 8, 10, 12]:
                print(year, month-1, 31)
            else:
                if month == 8:
                    print(year, month - 1, 31)
                else:
                    print(year, month-1, 30)
