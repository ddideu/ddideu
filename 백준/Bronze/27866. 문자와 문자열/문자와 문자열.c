#include <stdio.h>

int main() {
    char str[1000];
    int N;
    scanf("%s", &str);
    scanf("%d", &N);
    for (int i = 0; str[i] != '\0'; i++) {
        if (i+1 == N) {
            printf("%c", str[i]);
        }
    }
}