import sys
K = int(sys.stdin.readline())
count_1 = 0
for i in range(K):
	A, B, C = map(int,input().split())
	count_2 = 0
	if A==B==C:
		count_2 = (10000 + A * 1000)
	elif (A==B) or (A==C):
		count_2 = (1000 + A * 100)
	elif (B==C):
		count_2 = (1000 + B * 100)
	else :
		count_2 = (max(A,B,C)*100)

	if count_1<=count_2:
		count_1 = count_2
	
print(count_1)