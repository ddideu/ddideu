stick = int(input())
count = 0
stick_1 = 1
while stick != 0:
    if stick > stick_1:
        stick_1 *= 2
    elif stick == stick_1:
        count += 1
        break
    else:
        stick = stick - (stick_1//2)
        count += 1
        stick_1 = 1

print(count)
