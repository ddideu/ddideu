import heapq
people, total_sushi = map(int,input().split())
eat_sushi = [[] for _ in range(200001)]
people_eat = [0 for _ in range(people)]

for people_order in range(people):
    k, *my_order = list(map(int,input().split()))
    for order in my_order:
        heapq.heappush(eat_sushi[order], people_order)

menus = list(map(int, input().split()))
print(eat_sushi)
for menu in menus:
    if eat_sushi[menu]:
        people_eat[heapq.heappop(eat_sushi[menu])] += 1
print(*people_eat, sep=' ')



