total_pie, eat_pie = map(int, input().split())
pies = list(map(int, input().split()))
pies.extend(pies)
max_happy = 0
visited = [0] * (total_pie * 2 + 1)

for i in range(1, total_pie*2 + 1):
    visited[i] = visited[i-1] + pies[i-1]

for j in range(eat_pie, total_pie*2 + 1):
    max_happy = max(max_happy, visited[j] - visited[j-eat_pie])

print(max_happy)
