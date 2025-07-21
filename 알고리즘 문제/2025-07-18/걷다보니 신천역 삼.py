N = int(input())
cnt = 0
if N > 1:
    cnt = 2
if N > 2:
    cnt = cnt * 3 **(N-2) % 1000000009
print(cnt)