N = int(input())
target_boom = []
for idx in range(N):
    X, Y, V = map(int,input().split())
    total_dist = (X**2 + Y**2) ** (1/2)
    boom_time = total_dist / V
    target_boom.append([boom_time, idx+1])
target_boom.sort(key=lambda x: (x[0], x[1]))
for boom_time, idx in target_boom:
    print(idx)