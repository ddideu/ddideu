N, M = map(int,input().split())  # A행렬 크기 입력
A = [list(map(int, input().split())) for _ in range(N)]  # A행렬 입력
m, K = map(int, input().split())  # B행렬 크기 입력
B = [list(map(int, input().split())) for _ in range(m)]  # B행렬 크기 입력
C = [[0]*K for _ in range(N)]  # C행렬(결과값 크기는 N * K 행렬이다.)
for i in range(N):  # 3중 for 문으로
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]  # C행렬의 해당 위치에 저장되는 값

for i in C:  # C의 요소를 for문으로 돌면서
    print(*i)  # 언패킹

