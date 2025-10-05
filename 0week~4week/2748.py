import sys
input = sys.stdin.readline
n = int(input())
dp = [-1] * (n+1)
dp[0] = 0
dp[1] = 1
def fibonachi(n):
    if n < 2:
        return n
    if dp[n] != -1:
        return dp[n]    
    dp[n] = fibonachi(n-1) + fibonachi(n-2)
    return fibonachi(n)
print(fibonachi(n))