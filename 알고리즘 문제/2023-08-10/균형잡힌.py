def balance(L):  # 함수 생성
    stack = []  # 빈 스택리스트
    check = 'yes'  # 일단 무조건 yes
    for alpha in L:  # 리스트 for 문 반복
        if alpha == "(" or alpha == "{" or alpha == "[":  # 만약 검사한 요소가 여는 괄호라면
            stack.append(alpha)  # 스택에 추가

        elif alpha == ")" or alpha == "}" or alpha == "]":  # 만약 검사한 요소가 닫는 요소라면
            if stack:  # 스택이 있을때
                if alpha == ")":  # 검사한 요소가')'라면
                    if stack.pop() != "(":  # stack 에서 꺼내온 요소가 '('가 아니라면
                        check = 'no'  # check 를 no로 한후
                        break  # 탈출
                elif alpha == "}":  # 검사한 요소가'}'라면
                    if stack.pop() != "{":  # stack 에서 꺼내온 요소가 '{'가 아니라면
                        check = 'no'  # check 를 no로 한후
                        break  # 탈출
                else:  # 검사한 요소가']'라면
                    if stack.pop() != "[":  # stack 에서 꺼내온 요소가 '['가 아니라면
                        check = 'no'  # check 를 no로 한후
                        break  # 탈출
            else:  # 스택이 없다면
                check = 'no'  # check 를 no로 한후
                break  # 탈출

        elif alpha == ".":  # 만약 .일때
            if stack:  # 스택에 남아있는 요소 있다면
                check = 'no'  # check 를 no로

    return check # 체크 반환


while True:
    letter = str(input())  # 글자를 입력 받는 동안
    if letter == '.':  # 단독 . 하나가 나오면
        break # 탈출
    else:  # 그외의 경우라면
        print(balance(letter))  # check 값 출력