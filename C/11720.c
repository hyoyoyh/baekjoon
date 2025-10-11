#include <stdio.h>
int main() {
    int N, result = 0;
    char str[101];
    scanf("%d", &N);
    scanf("%s", str);
    for (int i = 0; i < N; i++) {
        result += str[i] - '0';
    }
    printf("%d", result);
    return 0;
}