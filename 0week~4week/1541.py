N = input().strip()
groups = N.split('-')
result = sum(map(int, groups[0].split('+')))
for i in groups[1:]:
    result -= sum(map(int, i.split("+")))
print(result)