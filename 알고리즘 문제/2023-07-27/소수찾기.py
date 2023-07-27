N = int(input())
A = list(map(int,input().split()))
B = list(set(A))
B.sort()
numbers = 0

for B_in in B:
    corret = 0
    for nums in range(2,1001):
        if nums >= B_in :  
            break 
        else :
            if B_in/nums - B_in//nums > 0:
                corret = 1
            else:
                corret = 0
                break
    if corret == 1:
        numbers += 1
    
print(numbers)
