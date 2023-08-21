number = int(input())
half = int(input())
something = number%half
real = half - something
if something <= 9:
    print(str(0)+str(real))
else:
    print(something)