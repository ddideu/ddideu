n = int(input())
my_combi = 1
if n%2:
    for i in range(n,0,-2):
        my_combi *= i
else:
    for i in range(n-1,0,-2):
        my_combi *= i
print(my_combi)

