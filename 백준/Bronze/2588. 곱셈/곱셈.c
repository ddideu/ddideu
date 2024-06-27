#include <stdio.h>

int main() {
    int num1, num2;
    int num2_one, num2_ten, num2_hunderd;
    scanf("%d\n%d", &num1, &num2);
    num2_one = num2 % 10 ;
    num2_ten = (num2 / 10) % 10;
    num2_hunderd = num2 / 100 ;
    printf("%d\n", num1 * num2_one);
    printf("%d\n", num1 * num2_ten);
    printf("%d\n", num1 * num2_hunderd);
    printf("%d\n", num1 * num2);
}