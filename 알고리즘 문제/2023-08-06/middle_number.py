# 입력 값을 저장할 리스트
Arr = []
# 입력된 값의 합
Arr_sum = 0
# 총 5번 입력을 한다라고 했으니
for i in range(5):
    # 해당 값을 A라는 변수에 입력받고
    A = int(input())
    # 해당 값을 입력 값의 합과 리스트에 저장.
    Arr_sum += A
    Arr.append(A)
# 끝난후 입력 값의 합의 평균을 출력후
print(int(Arr_sum/5))
# 해당 리스트를 오름차순으로 정렬후
Arr.sort()
# 중간값에 해당하는 값을 출력
print(Arr[2])