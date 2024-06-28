#include <stdio.h>

int main() {
    int N, i;
    scanf("%d" , &N);
    N = N / 4;
    i = 1;
    while (i <= N) {
        printf("long ");
        i = i + 1;
    }
    printf("int");
}