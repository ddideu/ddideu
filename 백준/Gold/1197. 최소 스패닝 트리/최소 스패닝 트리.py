import sys
sys.setrecursionlimit(10**9)
N, M = map(int,input().split())
parents = [i for i in range(N+1)]

edges = []
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

for _ in range(M):
    A, B, cost = map(int, input().split())
    edges.append([cost, A, B])

edges.sort()

for node in range(M):
    cost, start, finish = edges[node]
    if find_parents(parents, start) != find_parents(parents, finish):
        union_find(parents, start, finish)
        total_cost += cost

print(total_cost)