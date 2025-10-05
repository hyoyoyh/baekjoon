A,B = map(str, input().split())
print(int(max(A[::-1],B[::-1])))