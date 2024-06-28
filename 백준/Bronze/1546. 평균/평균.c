#include <stdio.h>

int main() {
    int N, max;
    float total = 0;
    max = -1;
    scanf("%d", &N);
    int arr[N];
    for (int i = 0; i<N; i++){
        scanf("%d", &arr[i]);
        if (arr[i]> max) {
            max = arr[i];
        }
        total = total + arr[i];
    }
    total = total / N;
    printf("%f", (total/max)*100);
}