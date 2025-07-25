def N_M(STACK, TARGET, NUMBER):
    if len(STACK) == TARGET:
        print(*STACK)
        return
    for my_num in range(1, NUMBER+1):
        STACK.append(my_num)
        N_M(STACK, TARGET, NUMBER)
        STACK.pop()

N, M = map(int,input().split())
for i in range(1, N+1):
    stack = [i]
    N_M(stack, M, N)