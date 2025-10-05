T = int(input())
for _ in range(T):
    R,S = map(str, input().split())
    for i in S:
        print(i*int(R), end="")
    print()