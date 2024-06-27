#include <stdio.h>

int main() {
    int hour, min;
    scanf("%d %d", &hour, &min);
    if (min < 45) {
        min = min + 15;
        hour = hour - 1;
        if (hour == -1) {
            hour = 23;
        }
    } else {
        min = min - 45;
    }
    printf("%d %d", hour, min);
}