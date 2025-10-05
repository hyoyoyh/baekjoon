import sys
input = sys.stdin.readline
N, C = map(int, input().split())
X = sorted(int(input()) for _ in range(N))
def wifi():
    s, e = 0, X[-1] - X[0]
    count = 1
    last = X[0]
    while s <= e:
        c = (s+e) // 2
        for i in range(1, N):
            if X[i] - last >= c:
                count += 1
                last = X[i]
        if count >= C:
            ans = c
            s = c + 1
        else:
            e = c - 1
    return ans
print(wifi())