#include <stdio.h>

int main() {
    int i = 1;
    while (i == 1) {
        int A, B;
        scanf("%d %d", &A, &B);
        if (A == 0 && B == 0) {
            i = 0;
        } else {
            printf("%d\n", A+B);
        }
    }
}