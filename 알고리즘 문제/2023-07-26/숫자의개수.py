A = int(input())
B = int(input())
C = int(input())
sum = A*B*C
ABC = str(sum)
for i in range(0,10):
    print(ABC.count(str(i)))
