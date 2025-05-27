from collections import deque
N, M = map(int, input().split())
my_list = list(map(int, input().split()))
queue = deque()
ans = 0
for i in range(1, N+1):
    queue.append(i)

while my_list:
    my_item = my_list.pop(0)
    item_loc = queue.index(my_item)
    if item_loc == 0:
        queue.popleft()
        N -= 1
    elif item_loc <= N//2:
        for _ in range(item_loc):
            ins = queue.popleft()
            queue.append(ins)
            ans += 1
        queue.popleft()
        N -= 1
    else:
        for _ in range(N, item_loc, -1):
            ins = queue.pop()
            queue.appendleft(ins)
            ans += 1
        queue.popleft()
        N -= 1
print(ans)