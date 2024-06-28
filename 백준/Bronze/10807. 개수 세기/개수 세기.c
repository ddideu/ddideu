#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int arr[N];
    for (int i = 0; i<N; i++){
        scanf("%d", &arr[i]);
    }
    int v, num;
    num = 0;
    scanf("%d", &v);
    for (int j = 0 ; j<N; j++){
        if (v == arr[j]) {
            num = num +1;
        }
    }
    printf("%d", num);
}