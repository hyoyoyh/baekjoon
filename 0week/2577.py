A = int(input())
B = int(input())
C = int(input())
hab = [int(a) for a in str(A*B*C)]
for i in range(10):
    print(hab.count(i))