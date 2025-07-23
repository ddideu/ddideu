fruit, myLength = map(int, input().split())
fruitHeight = sorted(map(int, input().split()))
for i in range(fruit):
    if fruitHeight[i] <= myLength:
        myLength += 1
    else:
        break
print(myLength)
