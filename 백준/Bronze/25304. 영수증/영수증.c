#include <stdio.h>

int main() {
    int total, sum, N;
    sum = 0 ;
    scanf("%d\n", &total);
    scanf("%d\n", &N);
    for (int i = 1; i <=N; i++) {
        int a, b;
        scanf("%d %d\n", &a, &b);
        sum = sum + (a*b);
    }
    if (sum == total) {
        printf("Yes");
    } else {
        printf("No");
    }
}