import sys

def finds(n):
    if gates[n] == n:
        return n
    parents = finds(gates[n])
    gates[n] = parents
    return parents
    

gate = int(sys.stdin.readline())
planes = int(sys.stdin.readline())
gates = [i for i in range(gate+1)]
cnt = 0
for i in range(planes):
    plane = int(sys.stdin.readline())
    fin = finds(plane)
    if fin == 0:
        break
    cnt += 1
    gates[fin] = gates[fin] - 1
print(cnt)
