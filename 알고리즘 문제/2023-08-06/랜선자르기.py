import sys

K, N = map(int, sys.stdin.readline().split())
M = [(int(sys.stdin.readline())) for _ in range(K)]

start = 1
end = max(M)
while start <= end:
    cnt = 0
    middle = (start+end)//2

    for i in M:
        cnt += i//middle

    if cnt < N:
        end = middle - 1

    if cnt >= N:
        start = middle + 1

print(end)

