#include <stdio.h>

int main() {
    int test;
    scanf("%d", &test); 
    for (int tc = 0; tc < test; tc++) {
        char repeat, word[20];
        int num;
        scanf(" %c %s", &repeat, word);  
        num = repeat - '0';  
        for (int i = 0; word[i] != '\0'; i++) {
            for (int j = 0; j < num; j++) {
                printf("%c", word[i]);
            }
        }
        printf("\n"); 
    }
}