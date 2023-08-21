# 테스트 횟수 입력
test = int(input())
# 테스트 횟수 만큼 반복
for tc in range(1, test+1):
    # 글자를 리스트 형태로 받은후
    word = list(map(str, input().split()))
    # 출력할 문자 생성
    backword = ''
    # 리스트 요소의 수만큼 for 문 반복
    for i in range(len(word)):
        # 만약 i 가 마지막 단어가 아니면
        if i != len(word) - 1:
            # 글자 앞에 여백 생성
            backword = " " + word[i] + backword
            # 만약 마지막 단어라면
        else:
            # 여백 제거
            backword = word[i] + backword
    # 테스트 케이스와 문자 출력
    print(f'Case #{tc}: {backword}')