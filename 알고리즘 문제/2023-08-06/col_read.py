# 2차원 배열 생성
arr = [list(map(str, input())) for _ in range(5)]
word = ''

for row in range(15):
    for col in range(15):
        # 시도하고
        try:
            word += arr[col][row]
        # 안되면 그냥 넘어가라
        except:
            continue
#  word 내용 프린트
print(word)