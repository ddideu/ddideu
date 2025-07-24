import sys
def prime_num(Number, prime):
    for i in range(2, Number):
        if prime % i == 0:
            return 0
    return 1

target = int(sys.stdin.readline())
arr = []
cnt = 0
for prime_chcek in range(2, target+1):
    my_num = int(prime_chcek ** (1/2)) + 1
    check = prime_num(my_num, prime_chcek)
    if check:
        arr.append(prime_chcek)
dp = [0] * (len(arr) + 1)
for idx in range(len(arr)):
    dp[idx+1] = dp[idx] + arr[idx]
end_point = len(dp)
l_p = 0
r_p = 0
while r_p < end_point:
    if dp[r_p] - dp[l_p] > target:
        l_p += 1
    elif dp[r_p] - dp[l_p] < target:
        r_p += 1
    else:
        r_p += 1
        cnt += 1
print(cnt)
