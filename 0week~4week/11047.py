import sys
input = sys.stdin.readline
N,K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
count = 0
for coin in coins:
    if K == 0:
         break
    if coin <= K:
        count += K // coin
        K -= count * coin
print(count)
# 동전 0