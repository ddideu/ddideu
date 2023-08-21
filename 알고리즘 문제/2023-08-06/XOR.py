import sys
# 해당 변수 생성
A, B, C = map(int, sys.stdin.readline().split())
# 만약 C가 2로 나눈 나머지가 0일 경우
if C % 2 == 0:
    # A는 Xor연산자를 한번 한후 한번 더한다.
    A = (A ^ B) ^ B
    # 만약 아닐경우
else:
    # Xor 연산자를 한번만 한다.
    A = A ^ B
print(A)
#
# # i = 0
# # while i < C:
# #     A = A ^ B
# #     i += 1
# print(A)