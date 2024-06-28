#include <stdio.h>

int main() {
    int N;
    scanf("%d" , &N);
    int i = 1;
    while (i <= N) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
    i = i + 1;
    printf("\n");
    }
}