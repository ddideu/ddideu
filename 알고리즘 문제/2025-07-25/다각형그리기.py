from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
sample = deque(map(int, input().split()))
reverse_sample = deque()
for idx in range(N-1, -1, -1):
    if sample[idx] == 1:
        reverse_sample.append(3)
    elif sample[idx] == 2:
        reverse_sample.append(4)
    elif sample[idx] == 3:
        reverse_sample.append(1)
    else:
        reverse_sample.append(2)

cnt = 0
results = []
test = int(input())
for _ in range(test):
    test_sample = deque(map(int, input().split()))
    ins = test_sample.copy()
    for _ in range(N) :
        if sample == ins or reverse_sample == ins:
            cnt += 1
            results.append(test_sample)
            break
        add = ins.popleft()
        ins.append(add)
print(cnt)
for result in results:
    print(*result)
