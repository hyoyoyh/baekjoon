#include <stdio.h>
int stack[10000];
int top = -1;
int N;
char str[10];
int x;
int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%s", str);
        if (str[0] == 'p' && str[1] == 'u') {
            scanf("%d", &x);
            stack[++top] = x;
        }
        else if (str[0] == 'p' && str[1] == 'o') {
            if (top == -1) printf("-1\n");
            else printf("%d\n", stack[top--]);
        }
        else if (str[0] == 's') {
            printf("%d\n", top + 1);
        }
        else if (str[0] == 'e') {
            printf("%d\n", (top == -1 ? 1 : 0));
        }
        else if (str[0] == 't') {
            if (top == -1) printf("-1\n");
            else (printf("%d\n", stack[top]));
        }
        
            
        }
    return 0;
}
