N = int(input())
count = 1
nums = 1
move = 0
while nums < N:
    move += 1
    nums += move*6
    count += 1
print(count)