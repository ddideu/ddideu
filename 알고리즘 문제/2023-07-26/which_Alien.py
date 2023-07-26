# 처음에 더듬이수 입력
# 두번째 눈수 입력

# T = 최소 더듬이 4개 최대 눈 4개
# V = 최대 더듬이 4개 최소 눈 2개
# G = 최대 더듬이 2개 최대 눈 3개

# 위 조건에 맞는 외계인 모두 출력
# 없으면 출력 X

D = int(input())
E = int(input())

if D>=3 and E<=4:
    print('TroyMartian')
if D<=6 and E>=2:
    print('VladSaturnian')
if D<=2 and E<=3:
    print('GraemeMercurian')