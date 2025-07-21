while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
    else:
        f1 = 1
        f2 = 2
        cnt = 0
        if a <= f1 <= b:
            cnt += 1
        if a <= f2 <= b:
            cnt += 1
        while f2 < b:
            ins = f1 + f2
            f1 = f2
            f2 = ins
            if a <= f2 <= b:
                cnt += 1
        print(cnt)

