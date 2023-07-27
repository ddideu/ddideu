A = str(input())
B = A.lower()
C = 'abcdefghijklmnopqrstuvwxyz'
D = -1
E = " "
for i in C:
    if B.count(i) > D:
        D = B.count(i)
        E = i
    elif B.count(i) == D:
        E = "?"
F = E.upper()
print(F)

