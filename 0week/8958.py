t = int(input())
for i in range(t):
    a = list(input())
    num = 0
    calc = 0
    for c in a:
        if c == "O":
            num += 1
            calc += num
        else:
            num = 0
    print(calc)

        
    