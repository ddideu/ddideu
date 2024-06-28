#include <stdio.h>

int main() {
    int N = 28;
    int arr[N];
    for (int i = 0 ; i < N; i++) {
        int num;
        scanf("%d", &num);
        arr[i] = num;
    }
    for (int j = 1 ; j <= 30; j++) {
        int flag = 1;
        for (int k = 0; k < N; k++) {
            if (arr[k] == j) {
                flag = 0;
                break;
            } 
        }
        if (flag == 1) {
            printf("%d\n", j);
        }
    }
}