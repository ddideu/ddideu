#include <stdio.h>
#include <string.h>

int main() {
    char input[1000001];
    fgets(input, sizeof(input), stdin);
    
    int count = 0;
    char *token = strtok(input, " \n");
    
    while (token != NULL) {
        count++;
        token = strtok(NULL, " \n");  // 다음 토큰으로 넘어갑니다.
    }

    printf("%d\n", count);  // 단어의 개수를 출력합니다.

}