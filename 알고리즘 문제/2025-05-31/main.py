N, R, Q = map(int, input().split())
my_node = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)
my_node[R] = R
stack = []
stack.append(R)
start = R
while True:
    for my_next in graph[start]:
        if my_node[my_next] == 0:
            if start not in stack:
                stack.append(start)
            my_node[my_next] = start
            stack.append(my_next)
            start = my_next
            break
    else:
        if stack:
            start = stack.pop()
        else:
            break
for my_visit in range(Q):
    target = int(input())
    ans = 1
    my_stack = []
    my_stack.append(target)
    my_start = target
    while True:
        for i in graph[my_start]:
            if i != my_node[my_start] and visited[i] != my_visit:
                if my_start not in my_stack:
                    my_stack.append(my_start)
                visited[i] = my_visit
                my_stack.append(i)
                start = i
                ans += 1
                break
        else:
            if my_stack:
                my_start = my_stack.pop()
            else:
                break
    print(ans)