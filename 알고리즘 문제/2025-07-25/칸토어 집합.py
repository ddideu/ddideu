def my_sample(start, end, cnt):
    if cnt == 0:
        return
    mid1 = (end-start)//3 + start
    mid2 = (end-start)//3 * 2 + start
    for idx in range(mid1, mid2):
        arr[idx] = ' '
    my_sample(start, mid1, cnt-1)
    my_sample(mid2, end, cnt-1)

while True:
    try:
        N = int(input())
        my_num = 3**N
        arr = ['-'for _ in range(my_num)]
        my_sample(0, my_num, N)
        print(*arr, sep='')
    except:
        break