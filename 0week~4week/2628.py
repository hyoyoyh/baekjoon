N,M = map(int, input().split())
X = [0, N] # 0 2 3 10 
Y = [0, M] # 0 4 10
C = int(input())
for _ in range(C):
    A,B = map(int, input().split())
    if A == 0:
        Y.append(B)
    else:
        X.append(B)
    X.sort()
    Y.sort()
    W = [(X[i+1] - X[i]) for i in range(len(X)-1)]
    H = [(Y[o+1] - Y[o]) for o in range(len(Y)-1)]
print(max(W)*max(H))



    