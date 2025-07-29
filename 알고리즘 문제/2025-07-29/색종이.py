import sys
input = sys.stdin.readline

def color_papers(start_r,start_c,end_r,end_c):
    global blue, white
    my_color = color_paper[start_r][start_c]
    flag = 1
    for row in range(start_r,end_r):
        for col in range(start_c,end_c):
            if my_color != color_paper[row][col]:
                flag = 0
                break
    if flag:
        if my_color == 1:
            blue += 1
        else:
            white += 1
    else:
        mid_r = (start_r + end_r)// 2
        mid_c = (start_c + end_c)//2
        color_papers(start_r,start_c, mid_r,mid_c)
        color_papers(start_r,mid_c,mid_r,end_c)
        color_papers(mid_r,start_c,end_r,mid_c)
        color_papers(mid_r,mid_c,end_r,end_c)
    return

N = int(input())
blue = 0
white = 0
color_paper = [list(map(int,input().split())) for _ in range(N)]
color_papers(0, 0, N, N)
print(white)
print(blue)