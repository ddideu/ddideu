chanel = int(input())
ans = abs(100 - chanel)
number = int(input())
if number:
    broke_number = set(input().split())
else:
    broke_number = set()

for num in range(1000001):
    for N in str(num):
        if N in broke_number:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - chanel))

print(ans)