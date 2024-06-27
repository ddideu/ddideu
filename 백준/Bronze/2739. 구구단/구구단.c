#include <stdio.h>

int main() {
    int N;
    int number = 1;
    scanf("%d", &N);
    while (number < 10) {
        printf("%d * %d = %d\n", N, number, N*number);
        number = number + 1;
    }
}