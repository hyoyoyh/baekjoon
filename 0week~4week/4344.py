C = int(input())
for i in range(C):
    data = list(map(int, input().split()))
    amount = data[0]
    scores = data[1:]
    avg = sum(scores) / amount
    count = sum(1 for s in scores if s > avg)
    per = count / amount * 100
    print(f"{per:.3f}%")
 