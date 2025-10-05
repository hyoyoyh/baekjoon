import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0]*(m+1)
    dp[1] = 1
    for coin in coins:
        for i in range(coin, m+1):
            dp[i] += dp[i-coin]
    print(dp[m])