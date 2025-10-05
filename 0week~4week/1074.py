def z(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n-1)
    if r < half and c < half:
        return z(n - 1, r, c)
    if r < half and c >= half: # 2
        return half*half + z(n - 1, r, c-half)
    if r >= half and c < half:
        return 2 * half*half + z(n - 1, r - half, c)
    else:
        return 3 * half*half + z(n - 1, r, c-half)
N, r, c = map(int, input().split())
print(z(N, r, c))
