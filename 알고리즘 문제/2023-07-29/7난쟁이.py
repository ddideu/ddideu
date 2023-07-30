A = []
for i in range(9):
    A.append(int(input()))

A.sort()
for i in A:
    subprice = sum(A) - i
    for j in A:
        price = subprice - j
        if price == 100:
            A.remove(i)
            A.remove(j)
            for k in A:
                print(k)