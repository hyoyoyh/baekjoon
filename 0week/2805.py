import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 입력
H = sorted(map(int, input().split()))
def namoo(s, e):
    while s <= e:
        result = 0
        c = (s+e)//2
        for h in H:
            if h > c:
                result += h - c
        if result >= M:
            ans = c
            s = c + 1
        else:
            e = c - 1
    return ans
print(namoo(0, max(H)))
