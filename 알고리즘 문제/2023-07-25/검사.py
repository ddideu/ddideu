import sys
input = sys.stdin.readline

count = 0
while True:
    o, w = map(int, input().split()) 
    life_count = 0
    if o == 0 and w <=0:
        break

    else:        
        while True:
            
            act, n = map(str, input().split())
            n = int(n)

            if act == 'F':
                w += n

            elif act == 'E':
                w -= n
                if w <= 0:
                    count += 1 # 해당 카운트로 RIP의 상태를 출력 해둘것! 
                    print(f'{count} RIP') 
                    act = '#'
                    break # 1. 바로 끝나버린다는점 문제에서는 시나리오에서는 모든 작용 완료후 펫 상태 출력 지시.       
                    

            elif act == '#': # N이 0으로 입력 됐을때로도 조건 설정 해둘것!
                 count += 1
                 if w > o/2 and w < o*2:
                    print(f'{count} :-)') #바로 프린트 하지 말고 리스트를 만들어서 저장 해놓을것!
                    break           
                 elif w <= 0:
                    print(f'{count} RIP')
                    break 
                 else:
                    print(f'{count} :-(')
                    break