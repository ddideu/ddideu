A = list(map(int,input().split()))
B = list(map(int,input().split()))
if sum(A) >= sum(B):
    print(sum(A))
else:
    print(sum(B))