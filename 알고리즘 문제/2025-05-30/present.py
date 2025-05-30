import sys
input = sys.stdin.readline()
def my_length(start_length, end_length):
    ans = 0
    ## while 문에서 for문으로 바꾼이유.
    # while은 탈출조건을 만족시키기가 쉽지 않았다. 
    for _ in range(100000):
        mid = (start_length + end_length)/ 2
        if (L // mid) * (W // mid) * (H // mid) >= N:
            start_length = mid
            ans = mid
        else:
            end_length = mid
    return ans


N, L, W, H = map(int, input.split())
max_lenght = max(L, W, H)
print("%.10f" % my_length(0, max_lenght))