import sys
def three(N):
    num = 0
    for i in str(N):
        num += int(i)
    return num


Number = int(sys.stdin.readline())
count = 0
while Number // 10 != 0:
    Number = three(Number)
    count += 1

if Number % 3 == 0:
    print(count)
    print('YES')
else:
    print(count)
    print('NO')