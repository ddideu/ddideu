import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    stack.append(int(input()))
stack.sort()
if N == 1:
    print(4)
else:
    total_need = 5
    for idx in range(N-1):
        flag = 1
        pointer = 1
        while idx + pointer < N:
            if stack[idx + pointer] - stack[idx] <= 4 and pointer != 5:
                pointer += 1
            else:
                if 5 - pointer < total_need:
                    total_need = 5 - pointer
                break
        if 5 - pointer < total_need:
            total_need = 5 - pointer
    print(total_need)
