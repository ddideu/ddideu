import sys

left_word = list(map(str, sys.stdin.readline().rstrip())) # 글자를 리스트로 받아서 개별로 표현
right_word = []
command = int(sys.stdin.readline()) # 명령 횟수
for _ in range(command): # 명령 반복
    content = list(map(str, sys.stdin.readline().split())) # 무슨 명령 밑 추가 할 단어
    if content[0] == 'L' and left_word:
        right_word.append(left_word.pop())
    elif content[0] == 'D' and right_word: # 오른쪽으로 커서 이동 단 커서가 단어 끝이면 명령 무시
        left_word.append(right_word.pop())
    elif content[0] == 'B' and left_word: # 해당 위치의 문자 제거
        left_word.pop()
    elif content[0] == 'P': # 해당 커서 위치 +1 에 문자 추가
        left_word.append(content[1])
    else:
        continue
print(*left_word, sep='', end='')
right_word.reverse()
print(*right_word, sep='')

### 스택 구조에 대한 이해가 필요한 문제 이다. 후입선출 구조를 잘 이해해야지만 풀수 있다.