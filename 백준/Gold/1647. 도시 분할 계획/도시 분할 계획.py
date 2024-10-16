import sys
def find_parents(parents, X):
    if parents[X] != X:
        parents[X] = find_parents(parents, parents[X])
    return parents[X]

def union_find(parents, a, b):
    A = find_parents(parents, a)
    B = find_parents(parents, b)
    if A < B:
        parents[B] = A
    else:
        parents[A] = B


N, M = map(int, sys.stdin.readline().split())
parents = [i for i in range(N+1)]
dist = []
total_cost = 0
last_cost = 0


for _ in range(M):
    start, finish, cost = map(int, sys.stdin.readline().split())
    dist.append([cost, start, finish])

dist.sort()

## 최소 신장트리의 특성! 마지막 선을 자르게 된다면 두개의 신장트리가 된다!
## 이점을 잘 생각해둘것!
for now_cost, start_point, end_point in dist:
    if find_parents(parents,start_point) != find_parents(parents, end_point):
        union_find(parents, start_point, end_point)
        total_cost += now_cost
        last_cost = now_cost
print(total_cost - last_cost)