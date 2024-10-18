## 에라토스테네스의 체는 다음과 같은 방식으로!
N = int(input())
arr = list(map(int, input().split()))
set_arr = set(arr)
max_num = max(set_arr)
score = [0 for _ in range(max_num + 1)]
for i in arr:
    if i == max_num:
        continue
    for j in range(i*2, max_num+1, i):
        if j in set_arr:
            score[i] += 1
            score[j] -= 1

for idx in arr:
    print(score[idx], end=' ')