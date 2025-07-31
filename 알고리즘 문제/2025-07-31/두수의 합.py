N = int(input())
arr = sorted(map(int,input().split()))
target = int(input())
r_p = N-1
l_p = 0
cnt = 0
while l_p < N-1:
    if arr[l_p] + arr[r_p] > target:
        r_p -= 1
    elif arr[l_p] + arr[r_p] < target or l_p >= r_p:
        l_p += 1
        r_p = N-1
    else:
        cnt += 1
        l_p += 1
        r_p = N-1
print(cnt)