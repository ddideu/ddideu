#include <stdio.h>

int main() {
    char strA[4], strB[4];
    scanf("%s %s", &strA, strB);
    char backA[4], backB[4];
    for (int i = 0; i<3; i++) {
        backB[i] = strB[2-i];
        backA[i] = strA[2-i];
    }
    int A = 0;
    int B = 0;
    for (int j = 0; j < 3; j++){
        A = A * 10 + (backA[j] - '0');
        B = B * 10 + (backB[j] - '0');
    }
    if (A > B) {
        printf("%d", A);
    } else {
        printf("%d", B);
    }
}