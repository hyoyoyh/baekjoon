import sys
input = sys.stdin.readline

N = int(input())
pap = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0

def paper(x, y, n):
    global white, blue
    color = pap[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if pap[i][j] != color:
                half = n // 2
                paper(x, y, half)               # 왼쪽 위
                paper(x, y+half, half)          # 오른쪽 위
                paper(x+half, y, half)          # 왼쪽 아래
                paper(x+half, y+half, half)     # 오른쪽 아래
                return
    if color == 0:
        white += 1
    else:
        blue += 1

paper(0, 0, N)
print(white)
print(blue)
