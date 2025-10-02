N = int(input())
towers = list(map(int, input().split()))
a = []
for i in range(1,N+1):
    if towers[-i] <= towers[-i+1]:
        a.append(towers.index(-i+1))
        
