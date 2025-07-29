keyboard, my_press = map(int,input().split())
input_alpha = []
my_word = ''
for idx in range(my_press):
    keyboard_num, press_time, alpha = map(str, input().split())
    input_alpha.append([int(keyboard_num), int(press_time), alpha])
input_alpha.sort(key=lambda x: [x[1], x[0]])
for idx_1, idx_2, word in input_alpha:
    my_word += word
print(my_word)
