row, col = map(int, input().split())
pictures = []
for _ in range(row):
    my_pictures = list(map(str, input()))
    for idx in range(col):
        if my_pictures[idx] != '.':
            my_pictures[col-idx-1] = my_pictures[idx]
    pictures.append(my_pictures)
for picture in pictures:
    print(*picture, sep='')
