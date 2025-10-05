import sys
input = sys.stdin.readline

n = int(input())
X = [list(map(int, input().split())) for _ in range(n)]

last = float('inf')

for i in range(n):
    for j in range(i+1, n):
        d = (X[i][0] - X[j][0])**2 + (X[i][1] - X[j][1])**2
        if d < last:
            last = d

print(last)