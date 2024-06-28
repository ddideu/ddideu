#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int arr[N];
    for (int i = 0; i<N; i++){
        scanf("%d", &arr[i]);
    }
    int max, min;
    max = -1000001;
    min = 1000001;
    for (int j = 0 ; j<N; j++){
        if (min > arr[j]) {
            min = arr[j];
        }
        if  (max < arr[j]) {
            max = arr[j];
        }
    }
    printf("%d %d", min, max);
}