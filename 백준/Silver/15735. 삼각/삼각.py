num = 0
N = int(input())
reverse_num = 0

for i in range(N, 0, -1):
    num += (i**2 + i) // 2

for i in range(N-1, 0, -2):
    reverse_num += (i**2 + i) // 2

print(num + reverse_num)