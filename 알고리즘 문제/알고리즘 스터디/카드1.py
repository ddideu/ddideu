import sys

def card(N): # 함수 생성
    stack_1 = []  # 숫자를 저장할 리스트
    stack_2 = []  # 결과를 출력할 리스트
    for i in range(N, 0, -1): # for 문으로
        stack_1.append(i)  # 1번 스택에 입력받은 숫자를 1씩 차감해서 집어 넣는다.
    count = 0  # 해당 문자를 넣을지 말지 판별하는 카운트
    while stack_1:  # stack_1이 비어 있지 않을때까지
        S = stack_1.pop()  # stack_1의 제일 마지막 요소 pop
        if count == 0:  # 0이라면
            count += 1  # 카운트를 하나 증가시키고
            stack_2.append(S)  #  결과 출력 리스트에 추가
        else: # 0이 아니라면
            count += 1  # 카운트를 하나 증가시키고
            stack_1.insert(0, S)  # pop 한 요소를 stack_1의 0번 위치에 추가
        count %= 2  # count 를2로 나눈 나머지가 앞으로 카운트
    return stack_2  # stack_2 반환


Number = int(sys.stdin.readline())  # 숫자 입력받고
print(*card(Number))  # 반환받은 리스트 언패킹 해서 출력