def password(Word, number):
    if len(Word) == N:
        real_word = ''
        gather_flag = 1
        consonant_flag = 2
        for idx in Word:
            real_word += alpha[idx]
            if alpha[idx] in ['a', 'e', 'i', 'o', 'u']:
                gather_flag -= 1
            else:
                consonant_flag -= 1
        if gather_flag <= 0 and consonant_flag <= 0:
            stacks.append(real_word)
        return
    for next_idx in range(M):
        if next_idx >= number:
            Word.append(next_idx)
            password(Word, next_idx+1)
            Word.pop()
    return


N, M = map(int,input().split())
alpha = sorted(map(str, input().split()))
check = M-N+1
stacks = []
for idx in range(check):
    my_word = [idx]
    password(my_word, idx+1)

for stack in stacks:
    print(*stack, sep='')