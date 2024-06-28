#include <stdio.h>

int main() {
    while (1) {
        int A, B;
        if (scanf("%d %d", &A, &B) == EOF) {
            break;
        } else {
            printf("%d\n", A+B);
        }
    }
}