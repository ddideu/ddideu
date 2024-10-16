# 시간 초과 식...
# def three_sum(STACK, NUM):
#     global total_cost
#     if len(STACK) == 3:
#         cost = 0
#         for oil in STACK:
#             cost += oil
#         if abs(total_cost) > abs(cost):
#             total_cost = cost
#         return
#
#     if len(STACK) > 3:
#         return
#
#     for idx in range(NUM, N):
#         if arr[idx] not in STACK:
#             STACK.append(arr[idx])
#             three_sum(STACK, idx)
#             STACK.pop()
#
#
# N = int(input())
# arr = list(map(int, input().split()))
# total_cost = 1e9 * 3 + 1
# for i in range(N):
#     stack = []
#     stack.append(arr[i])
#     three_sum(stack, i)
# print(total_cost)

# 메모리 초과 식
# from itertools import combinations

# N = int(input())
# arr = list(map(int, input().split()))
# total_cost = 1e9 * 3 + 1
# three_oil = list(combinations(arr, 3))
# best_combi = []
# for oils in three_oil:
#     now_cost = 0
#     for oil in oils:
#         now_cost += oil
#     if abs(total_cost) > abs(now_cost):
#         best_combi = oils
#         total_cost = now_cost
#         if total_cost == 0:
#             break
#
# print(*best_combi)

N = int(input())
arr = sorted(list(map(int, input().split())))
total_cost = 1e9 * 3 + 1
best_combi = []
flag = 1
for idx in range(N-2):
    left_point = idx + 1
    right_point = N - 1
    while left_point < right_point:
        now_cost = arr[left_point] + arr[idx] + arr[right_point]
        if abs(total_cost) > abs(now_cost):
            total_cost = now_cost
            best_combi = [arr[idx], arr[left_point], arr[right_point]]
        if now_cost < 0:
            left_point += 1
        elif now_cost > 0:
            right_point -= 1
        else:
            flag = 0
            break
    if flag == 0:
        break
print(*best_combi)
