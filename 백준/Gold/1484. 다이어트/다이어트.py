G = int(input())
flag = 1

for now in range(1, G):
    for past in range(now, 0, -1):
        if (now-past)*(now+past) == G:
            print(now)
            flag = 0
            break
        elif (now-past)*(now+past) > G:
            break
        else:
            continue

if flag == 1:
    print(-1)