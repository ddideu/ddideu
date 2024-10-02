N = int(input())
my_dict = {}
for _ in range(N):
    file = ''
    flag = 0
    for txt in str(input()):
        if flag:
            file = file + txt
        if txt == '.':
            flag = 1
    if file not in my_dict:
        my_dict[file] = 1
    else:
        my_dict[file] += 1

for find_file in sorted(my_dict.items()):
    print(*find_file)