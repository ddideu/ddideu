test = int(input())
for tc in range(test):
    prime_num = list(map(int, input().split()))
    num = prime_num[0]
    prime = prime_num[1:]
    checks = []
    for i in range(2, num+1):
        ad = []
        start = 0
        while start + i <= num:
            ad.append(sum(prime[start:start+i]))
            start += 1
        checks.append(ad)

    min_length = 2
    for check in checks:
        flag = 1
        for sub_sum in check:
            flag_1 = 1
            idx = int(sub_sum ** (1/2)) + 1
            for i in range(2, idx):
                if sub_sum % i == 0:
                    flag_1 = 0
                    break
            if flag_1:
                ans = prime[check.index(sub_sum):check.index(sub_sum) + min_length]
                print(f'Shortest primed subsequence is length {min_length}:', end=' ')
                print(*ans)
                flag = 0
                break
        if flag:
            min_length += 1
        else:
            break
    else:
        print('This sequence is anti-primed.')


