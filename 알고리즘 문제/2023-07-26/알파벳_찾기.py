N = str(input())
A = 'abcdefghijklmnopqrstuvwxyz'
B = []
for i in A:
    B.append(N.find(str(i)))
print(*B)
    