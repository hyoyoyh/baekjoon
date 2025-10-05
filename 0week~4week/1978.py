N = int(input())
prime = list(map(int, input().split()))
print(sum(1 for i in prime if i > 1 and all(i % a for a in range(2, int(i ** 0.5) +1))))
