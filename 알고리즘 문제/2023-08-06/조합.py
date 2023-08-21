Test = int(input())
arr = []
for tc in range(Test):
    left, right = map(int, input().split())
    total = 1
    for top in range(right, (right-left), -1):
        total *= top
    for bottom in range(1, left+1):
        total //= bottom
    arr.append(total)
for i in range(Test):
    print(int(arr[i]))