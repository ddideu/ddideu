N = int(input())
tang_furu = list(map(int, input().split()))
l_p = 0
r_p = 0
cnt = 0
fruit_count = {}
while r_p < N:
    if tang_furu[r_p] in fruit_count:
        fruit_count[tang_furu[r_p]] += 1
        r_p += 1
    else:
        fruit_count[tang_furu[r_p]] = 1
        while len(fruit_count) > 2:
            fruit_count[tang_furu[l_p]] -= 1
            if fruit_count[tang_furu[l_p]] == 0:
                del fruit_count[tang_furu[l_p]]
            l_p += 1
    cnt = max(cnt, r_p-l_p)
print(cnt)