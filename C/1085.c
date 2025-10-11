#include <stdio.h>
int main() {
    int x,y,w,h;
    scanf("%d %d %d %d", &x,&y,&w,&h);
    //w - x, w, h - y, y
    int l = w - x;
    int r = x;
    int u = h - y;
    int d = y;
    int rlmin = (l < r ? l : r);
    int udmin = (u < d ? u : d);
    int result = (rlmin < udmin ? rlmin : udmin);
    printf("%d", result);
}