#include <stdio.h>
long long store[1000];

long long fibo(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (store[n] != -1) return store[n];
    return store[n] = fibo(n-1) + fibo(n-2);

}

int main() {
    int n;
    scanf("%d", &n);
    store[0] = 0;
    store[1] = 1;
    for (int i = 2; i <= n; i++) store[i] = -1;
    printf("%lld", fibo(n));
    return 0;
}