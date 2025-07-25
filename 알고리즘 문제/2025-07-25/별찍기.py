# 이문제를 아직 풀기 전이라면 칸토어 집합을 풀어보도록 하자. 해당 문제를 푸는데 많은 도움을 얻을수 있다.
def star_point(start, end, count, now_row):
    if count == 0:
        return
    cnt = (end-start)//3
    real_mid1 = cnt + start
    real_mid2 = cnt * 2 + start
    if real_mid1 <= now_row < real_mid2:
        for i in range(0, number, count):
            for idx in range(cnt,cnt * 2):
                    stars[now_row][idx+i] = ' '

    star_point(start, real_mid1, count//3, now_row)
    star_point(real_mid1, real_mid2, count//3, now_row)
    star_point(real_mid2, end, count//3, now_row)

import sys
input = sys.stdin.readline
number = int(input())
stars = [['*'] * number for _ in range(number)]
for idx in range(number):
    star_point(0, number, number, idx)

for star in stars:
    print(*star, sep='')