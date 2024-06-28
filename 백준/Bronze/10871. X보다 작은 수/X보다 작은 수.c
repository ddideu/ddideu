#include <stdio.h>

int main() {
    int N, X;
    scanf("%d %d", &N, &X);
    int arr[N];
    for (int i = 0; i<N; i++){
        scanf("%d", &arr[i]);
    }
    for (int j = 0 ; j<N; j++){
        if (X > arr[j]) {
            printf("%d ", arr[j]);
        }
    }
    
}