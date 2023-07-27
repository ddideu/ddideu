N = int(input())
fac = 1
count = 0
for i in range(1, N+1):
    fac *= i

for i in reversed(range(len(str(fac)))):
    if str(fac)[i] == '0':
        count += 1
    else :
        break
print(count)
