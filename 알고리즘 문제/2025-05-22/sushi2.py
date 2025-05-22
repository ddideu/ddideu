from collections import deque
people, total_sushi = map(int,input().split())
eat_sushi = [[] for _ in range(200001)]
people_eat = [0] * people

for people_order in range(people):
    my_order = list(map(int,input().split()))
    for order in my_order[1:]:
        eat_sushi[order].append(people_order)

menus = list(map(int, input().split()))
for menu in menus:
    if eat_sushi[menu]:
        who = eat_sushi[menu][0]
        people_eat[who] += 1
print(*people_eat)