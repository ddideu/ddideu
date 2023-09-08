N = int(input())
arr = [[] for _ in range (201)]
for i in range(N):
    age_name = list(map(str,input().split()))
    arr[int(age_name[0])].append(age_name[1])
for i in arr:
    if len(i) != 0:
        for j in i:
            print(f'{arr.index(i)} {j}')