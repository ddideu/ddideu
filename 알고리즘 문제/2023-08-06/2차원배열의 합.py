import sys
# N은 행 M은 열 입력
N, M = map(int, sys.stdin.readline().split())
# 해당 입력된 숫자로 2차원 배열 생성
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 테스트 수만큼 반복
Test = int(sys.stdin.readline())
for a in range(Test):
    # 왼쪽,오른쪽, 탑, 바닥 입력
    i, j, x, y = map(int, sys.stdin.readline().split())
    # 행렬이므로 왼쪽과 상단의 숫자는 하나씩뺀다
    i, j = i-1, j-1
    # 합계
    Test_sum = 0
    # 2중 for 문으로
    for b in range(N):
        for c in range(M):
            # 해당 범위 내라면
            if i <= b < x and j <= c < y:
                # 해당 하는 숫자 합계에 더한다.
                Test_sum += arr[b][c]
    # 이후 합계출력
    print(Test_sum)
