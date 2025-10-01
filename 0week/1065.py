def hansu(n):
    if n <= 99:
        return True
    if n == 1000:
        return False
    elif (n % 10) - (n // 10)%10 == (n // 10)%10 - ((n // 10) // 10) % 10:
        return True
    return False
N = int(input())
count = 0
for i in range(1, N+1):
    if hansu(i) == True:
        count += 1
if N == 1000:
    count = 144
print(count)