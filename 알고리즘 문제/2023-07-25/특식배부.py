N = int(input())
A, B, C = map(int,input().split())
sum = 0

if N >= A:
    sum += A
else:
    sum += N
if N >= B:
    sum += B
else:
    sum += N
if N >= C:
    sum += C
else:
    sum += N

print(sum)
