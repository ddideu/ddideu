songList, songTime, bellRing = map(int,input().split())
phoneHello = bellRing # 최초 벨 울리는 시간
mySongTime = songTime # 최초 곡이 끝나는 시간
flag = 1 # 플래그
for i in range(songList):
    while phoneHello < mySongTime: # 최초 벨 울리는 시간이 이번 곡이 끝나기 전이라면
        phoneHello += bellRing # 계속 울려
    if mySongTime <= phoneHello < mySongTime + 5: # 음악 종료 시점부터 5초가 되기전
        print(phoneHello)
        flag = 0
        break
    else: #아니면
        mySongTime += 5  #5초 휴식시간이후
        mySongTime += songTime  #다음 곡 진행


if flag:
    print(phoneHello)
