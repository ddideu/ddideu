A = input()
B = input()
C = input()
D = 0

if 'z' not in C:
    D = int(C) + 1
elif 'z' not in B:
    D = int(B) + 2
else:
    D = int(A) + 3

if D % 3 == 0 and D % 5 == 0:
    print('FizzBuzz')
elif D % 3 == 0:
    print('Fizz')
elif D % 5 == 0:
    print('Buzz')
else:
    print(D)