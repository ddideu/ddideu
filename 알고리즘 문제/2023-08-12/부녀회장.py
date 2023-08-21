def Find(k, n):
    apt = []
    for i in range(k+1):
        # 임시 리스트 생성
        Temp = [0] * (n + 1)
        # i+1만큼 반복
        for j in range(n+1):
            # 만약 i 가 0 혹은 j라면
            if i == 0:
                Temp[j] += j
                # 리스트에 j추가
            # 아니라면
            else:
                for m in range(j+1):
                    Temp[j] += apt[i-1][m]
        apt.append(Temp)
    return apt[k][n]

test = int(input())
for tc in range(test):
    dong = int(input())
    hosu = int(input())
    print(Find(dong,hosu))