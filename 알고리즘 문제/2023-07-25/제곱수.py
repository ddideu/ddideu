import sys
N = int(sys.stdin.readline())
i = 0
count = []
while True:
    if i**2 <= N:
        i += 1
    if i**2 > N:
        N -= (i-1)**2
        i = 0
        count.append(i-1**2) 
    if N == 0 and i == 0:
        break
print(len(count))
# if 2**2 > N:
#     count += N 

# if N == 0:
#     print(count) 


# while True:
#     i = 1
#     count = 0
#     if N == 0:
#         print(count)
#         break
#     else:
#         if i**2 < N:
#             i += 1
#         elif i**2 >= N:
#             N -= (i-1)**2
#             count += 1
#             i = 1 
#         if 2**2 > N:
#             count += N
