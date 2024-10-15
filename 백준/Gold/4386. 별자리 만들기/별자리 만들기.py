N = int(input())
node = []
edge = []
parents = [i for i in range(N+1)]
total_cost = 0
def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]


def union_find(parents, a, b):
    A = find_parents(parents, a)
    B = find_parents(parents, b)
    if A < B:
        parents[B] = A
    else:
        parents[A] = B

for _ in range(N):
    x, y = map(float, input().split())
    node.append([x, y])

for start in range(N):
    for end_point in range(start, N):
        if end_point == start:
            continue
        cost = (abs(node[end_point][0] - node[start][0])**2 + abs(node[end_point][1] - node[start][1])**2)**(1/2)
        edge.append([cost, start, end_point])
edge.sort()
for now_cost, start_point, finish_point in edge:
    if find_parents(parents, start_point) != find_parents(parents, finish_point):
        union_find(parents, start_point, finish_point)
        total_cost += now_cost
print(total_cost)