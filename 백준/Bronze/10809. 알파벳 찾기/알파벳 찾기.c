#include <stdio.h>

int main() {
    char word[100];
    char alpha[26] = "abcdefghijklmnopqrstuvwxyz";
    int arr[26];
    for (int i = 0; i < 26; i++) {
        arr[i] = -1;
    }
    scanf("%s", &word);
    for (int i = 0; word[i] != '\0' ; i++) {
        for (int j = 0; j < 26; j++) {
            if (word[i] == alpha[j] && arr[j] == -1) {
                arr[j] = i;
                break;
            }
        }
    }
    for (int i = 0; i < 26; i++) {
        printf("%d ", arr[i]);
    }
}