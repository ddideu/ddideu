#include <stdio.h>

int main() {
    int N, i;
    scanf("%d" , &N);
    i = 1;
    while (i <= N) {
        int A, B;
        scanf("%d %d" , &A, &B);
        printf("%d\n", A+B);
        i = i + 1;
    }
}