#include <stdio.h>

int main() {
    char str[100];
    int N = 0;
    scanf("%s", &str);
    for (int i = 0; str[i] != '\0'; i++) {
        N = N + 1;
    }
    printf("%d", N);
}