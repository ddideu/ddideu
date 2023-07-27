N = int(input())
word = []
for i in range(N):
    A = str(input())
    word.append(A)
S_word = list(set(word))
S_word.sort()
for i in range(1, 51):
    for j in S_word:
        if i == len(S_word):
            print(S_word[j])
