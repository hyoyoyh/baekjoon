a = []
for i in range(9):
    a.append(int(input()))
b = max(a)
c = a.index(b)
print(b)
print(c+1)