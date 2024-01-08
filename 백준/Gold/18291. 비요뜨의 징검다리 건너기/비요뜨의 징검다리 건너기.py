import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    stone = int(input())
    if stone == 1:
        print(1)
    else:
        side = (stone-2)
        number = 2
        ans = 10**9 + 7
        cnt = 1
        while side:
            if side % 2:
                cnt *= number
                cnt %= ans
            side //= 2
            number *= number
            number %= ans
        print(cnt)