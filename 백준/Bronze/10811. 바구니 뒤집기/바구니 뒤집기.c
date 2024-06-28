#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    int arr[N];
    for (int idx = 0; idx<N; idx++){
        arr[idx] = idx + 1;
    }
    for(int i = 0; i<M; i++){
        int A, B;
        int count;
        scanf("%d %d", &A, &B);
        count = (B-A+1)/2;
        for(int j = 0; j < count; j++){
            int tempA = arr[A+j-1];
            int tempB = arr[B-j-1];
            arr[B-j-1] = tempA;
            arr[A+j-1] = tempB;
        }
    }
    for(int i = 0; i<N; i++){
        printf("%d ", arr[i]);
    }
}