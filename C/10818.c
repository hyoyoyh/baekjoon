#include <stdio.h>
int main(void) {
    int N;
    scanf("%d",&N);
    int num, max, min;
    scanf("%d",&num);
    max = min = num;
    for (int i = 1; i < N; i++) {
        scanf("%d", &num);
        if (max < num) max = num;
        if (min > num) min = num;
    }
printf("%d %d\n", min,max);
return 0;
}