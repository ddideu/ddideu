N = int(input())
l_p = 0
r_p = N-1
arr = sorted(list(map(int, input().split())))
two_liquid = []
mix_liquid = 2000000001
while l_p < r_p:
    if abs(mix_liquid) >= abs(arr[r_p] + arr[l_p]):
        two_liquid = [arr[l_p], arr[r_p]]
        mix_liquid = arr[r_p] + arr[l_p]
    if arr[r_p] + arr[l_p] < 0:
        l_p += 1
    elif arr[r_p] + arr[l_p] > 0:
        r_p -= 1
    else:
        break
print(*two_liquid)