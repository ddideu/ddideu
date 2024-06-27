#include <stdio.h>

int main() {
    int year, flag;
    scanf("%d", &year);
    if  ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        flag = 1;
    } else {
        flag = 0;
    }
    printf("%d", flag);
}