#include <stdio.h>

int main() {
    int hour, min;
    int ovenhour, ovenmin;
    scanf("%d %d\n", &hour, &min);
    scanf("%d", &ovenmin);
    min = min + ovenmin;
    if (min > 59) {
        ovenhour = min / 60;
        min = min % 60;
        hour = hour + ovenhour;
        if (hour > 23) {
            hour = hour - 24;
        }
    }
    printf("%d %d", hour, min);
}