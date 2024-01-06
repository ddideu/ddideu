def MY_STACK(number, STACK):
    if len(STACK) == number:
        stack = []
        for check in STACK:
            stack.append(arr[check])

        total_stacks.add(tuple(stack))
        return

    for j in range(len(arr)):
        if j not in STACK:
            STACK.append(j)
            MY_STACK(number, STACK)
            STACK.pop()
    return


N, M = map(int, input() .split())
arr = sorted(map(int, input().split()))
total_stacks = set()

for i in range(len(arr)):
    stack = []
    if i >= 1 and arr[i-1] == arr[i]:
        continue
    stack.append(i)
    MY_STACK(M, stack)
#
for real in sorted(total_stacks):
    print(*real)