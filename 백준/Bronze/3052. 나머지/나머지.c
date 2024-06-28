#include <stdio.h>

int main() {
    int arr[10];
    int unique_count = 0;
    for (int i = 0; i<10; i++){
        int A;
        scanf("%d", &A);
        arr[i] = A % 42;
    }
    int unique[42] = {};
    for (int j = 0; j<10; j++) {
        unique[arr[j]] = 1;
    }
    for (int k = 0; k<42; k++) {
        if (unique[k]==1) {
            unique_count = unique_count + 1;
        }
    }
    printf("%d", unique_count);
}