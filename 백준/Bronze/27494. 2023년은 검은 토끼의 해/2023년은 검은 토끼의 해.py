N = int(input())
cnt = 0
find_num = '2023'
if N < 2023:
    print(0)
else:
    for number in range(2023, N+1):
        idx = 0
        check = str(number)
        if '2' not in check or '0' not in check or '3' not in check:
            continue
        else:
            for find in check:
                if find == find_num[idx]:
                    idx += 1
                    if idx == 4:
                        cnt += 1
                        break
    print(cnt)
