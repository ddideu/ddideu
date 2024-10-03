import math
K, N = map(int, input().split())
arr = list(map(int, input().split()))
print(math.lcm(*arr)-K)